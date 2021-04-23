import json
import os
import re
import subprocess
import sys
from typing import List

import html2markdown
import pkg_resources
from aiohttp import ClientSession

from auto_code.setting_model import console


def check_packages() -> None:
    # Check if all required packages installed
    required = {"html2markdown", "rich", "requests"}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print(f"Installing missing packages...")
        python = sys.executable
        subprocess.check_call(
            [python, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL
        )
        print("Packages installed!")


class Question:
    def __init__(self, slug: str) -> None:
        self.slug: str = slug  # LeetCode question slug
        self.folder_path: str = ""  # Folder path
        self.question_data: dict = {}  # LeetCode question data
        self.question_content: str = (
            ""  # LeetCode question content (str, Markdown format)
        )
        self.args_type: List[List[str], str] = [
            [],
            "",
        ]  # [[Input arg type, ], Output type]
        self.function_name: str = ""  # Solution function name

    async def fetch_question(self, session: ClientSession) -> None:
        """Fetch question data using graghql"""
        url = "https://leetcode.com/graphql"
        param = {
            "operationName": "questionData",
            "variables": {"titleSlug": self.slug},
            "query": """query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    content
                    difficulty
                    codeSnippets {
                        lang
                        code
                    }
                }
            }""",
        }
        async with session.post(url=url, json=param) as r:
            response = json.loads(await r.text())
            if "errors" in response:
                console.print(f":x: Error: question {self.slug} not found!")
                exit()
            else:
                self.question_data = response["data"]["question"]
                self.question_content = html2markdown.convert(
                    html=self.question_data["content"]
                )

                self.folder_path = (
                    f"{self.question_data['questionId']}. {self.question_data['title']}"
                )
                try:
                    os.makedirs(self.folder_path)
                except FileExistsError:
                    pass

                # Question markdown file
                self.create_question_md()
                # Question python3 file
                self.create_solution_py()
                # Question testing data
                self.create_testing_data()

    def python_snippets(self, codeSnippets: List[dict]) -> str:
        """Find LeetCode question's Python3 code snippets

        Args:
            codeSnippets (List[dict]): All languages snippets

        Returns:
            str: Python3 code snippets
        """
        for each in codeSnippets:
            if each["lang"] == "Python3":
                code = each["code"]
                self.parse_args_type(code=code)
                return code

    def adjust_markdown(self, markdown_content: str) -> str:
        """Adjust markdown content for linting

        Args:
            markdown_content (str): markdown content

        Returns:
            str: formatted markdown content
        """
        markdown_content = markdown_content.replace("*   ", "* ")
        markdown_content = re.sub(
            pattern="(\d+).   ", repl=r"\1. ", string=markdown_content
        )
        markdown_content = re.sub(
            pattern="``(.*)&lt;(.*)``",
            repl=r"<code>\1&lt;\2</code>",
            string=markdown_content,
        )
        return markdown_content

    def create_question_md(self) -> None:
        """Create QUESTION.MD for question info"""
        with open(f"{self.folder_path}/QUESTION.MD", mode="w+") as question_file:
            question_url = f"https://leetcode.com/problems/{self.slug}/"
            title = f"# [{self.question_data['questionId']}. {self.question_data['title']}]({question_url}) - {self.question_data['difficulty']}"
            self.question_content = self.adjust_markdown(
                markdown_content=self.question_content
            )
            question_file.writelines(
                title + "\n\n" + "## Question" + "\n\n" + self.question_content + "\n"
            )

    def create_solution_py(self) -> None:
        """Create {question_name}.py for Python3 solution"""
        # Code template
        template: str = ""
        with open("auto_code/template.py") as f:
            template = f.read()
        question_title: str = self.question_data["title"].lower() + ".py"
        python_filename = question_title.replace(" ", "_")
        try:
            with open(
                f"{self.folder_path}/{python_filename}", mode="x"
            ) as question_file:
                code_snippets = self.python_snippets(
                    codeSnippets=self.question_data["codeSnippets"]
                )
                template = template.replace("{Solution}", code_snippets)
                question_file.write(template)
        except FileExistsError:
            pass

    def parse_args_type(self, code: str) -> None:
        self.function_name = re.findall("def (.*)\(", string=code)[-1]
        split_result = re.findall("(.*)def (.*)\(self, (.*)\)(.*)", string=code)[-1]
        # Input args type
        for i in split_result[2].split(", "):
            arg, arg_type = i.split(": ")
            self.args_type[0].append(arg_type)
        # Return args type
        returns_type = re.findall("(.*)-> (.*):", string=split_result[3])[0][1]
        self.args_type[1] = str(returns_type)

    def create_testing_data(self) -> None:
        import rich

        testing_data: List[str] = []
        examples = re.findall("<pre>((.|\n)*?)<\/pre>", string=self.question_content)
        for each in examples:
            string = each[0].strip(" \n")
            input_args = re.findall("<strong>Input:<\/strong> (.*)", string=string)[0]
            output_value = re.findall("<strong>Output:<\/strong> (.*)", string=string)[
                0
            ]
            input_values = []
            for arg in input_args.split(", "):
                if arg:
                    in_value = arg.split("=")[1].strip(" ")
                    input_values.append(in_value)
            testing_data.append(f"{input_values}\n{output_value}")

        try:
            with open(f"{self.folder_path}/test_data.txt", mode="x") as test_file:
                # Function name
                test_file.write(self.function_name + "\n")
                # Args type
                args_type_text = ""
                input_args, output_args = self.args_type
                for each in input_args:
                    args_type_text += each + "|"
                args_type_text += output_args + "\n"
                test_file.write(args_type_text)
                # Testing data
                test_file.write("\n\n".join(testing_data))
        except FileExistsError:
            pass
