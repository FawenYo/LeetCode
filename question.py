import os
import sys
import subprocess
import pkg_resources
import re
from typing import List, Tuple


# Check if required packages installed
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

import html2markdown
import rich, rich.progress, rich.table, rich.console
import requests


class Question:
    def __init__(self, slug: str) -> None:
        self.slug: str = slug  # LeetCode question slug
        self.folder_path: str = ""  # Folder path
        self.question_data: dict = {}  # LeetCode question data
        self.question_content: str = (
            ""  # LeetCode question content (str, Markdown format)
        )

    def get_problem_content(self) -> None:
        self.fetch_question()

        try:
            os.makedirs(self.folder_path)
        except FileExistsError:
            pass

        # Question markdown file
        self.create_question_md()
        # Question python3 file
        self.create_solution_py()

    def fetch_question(self) -> None:
        """Fetch question data using graghql"""
        url = "https://leetcode.com/graphql"
        json = {
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
        response = requests.post(url=url, json=json).json()
        self.question_data = response["data"]["question"]
        self.question_content = html2markdown.convert(
            html=self.question_data["content"]
        )

        self.folder_path = (
            f"{self.question_data['questionId']}. {self.question_data['title']}"
        )

    def python_snippets(self, codeSnippets: List[dict]) -> str:
        """Find LeetCode question's Python3 code snippets

        Args:
            codeSnippets (List[dict]): All languages snippets

        Returns:
            str: Python3 code snippets
        """
        for each in codeSnippets:
            if each["lang"] == "Python3":
                return each["code"]

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
            markdown_content = self.adjust_markdown(
                markdown_content=self.question_content
            )
            question_file.writelines(
                title + "\n\n" + "## Question" + "\n\n" + markdown_content + "\n"
            )

    def create_solution_py(self) -> None:
        """Create {question_name}.py for Python3 solution"""
        question_title: str = self.question_data["title"].lower() + ".py"
        python_filename = question_title.replace(" ", "_")
        try:
            with open(
                f"{self.folder_path}/{python_filename}", mode="x"
            ) as question_file:
                code = (
                    'import sys\n\nsys.path.append(".")\nfrom model import *\n\n\n'
                    + self.python_snippets(
                        codeSnippets=self.question_data["codeSnippets"]
                    )
                )
                question_file.writelines(code)
        except FileExistsError:
            pass


if __name__ == "__main__":
    DATE = "2021-04-25"  # End date of the work. Format: "%Y-%m-%d".
    OPTIONAL = True  # Fetch optional question. Defaults to True.

    def fetch_questions(date: str) -> Tuple[List[str]]:
        """Fetch week questions from server

        Args:
            date (str): End date of work

        Returns:
            Tuple[List[str]]: ([required_questions], [optional_questions])
        """
        rich.print(f":truck: Fetching {DATE} questions from server...")
        server_url = f"https://leetcode-bot.ml/get_question?date={date}"
        response = requests.get(url=server_url).json()

        if response["code"] == 200:
            rich.print(":o: Successfully fetched questions list!")
            return (response["required_questions"], response["optional_questions"])
        else:
            problems = ([], [])
            rich.print(f":x: {response['error']['message']}")
        return problems

    def show_questions(
        required_questions: List[str], optional_questions: List[str]
    ) -> None:
        """Show week questions

        Args:
            required_questions (List[str]): Required questions
            optional_questions (List[str]): Optional questions
        """
        table = rich.table.Table(title=f"{DATE} 題目")
        table.add_column("類型", justify="right", style="green", no_wrap=True)
        table.add_column("題目名稱", style="magenta")
        table.add_column("題目網址", justify="right", style="blue")

        for question in required_questions:
            info, slug = question.split("__||__")
            table.add_row("必寫", info, f"https://leetcode.com/problems/{slug}/")

        for question in optional_questions:
            info, slug = question.split("__||__")
            table.add_row("選寫", info, f"https://leetcode.com/problems/{slug}/")

        rich.console.Console().print(table)

    required_questions, optional_questions = fetch_questions(date=DATE)

    problems = (
        (required_questions + optional_questions) if OPTIONAL else required_questions
    )
    if problems:
        for question in rich.progress.track(
            problems, description=":page_with_curl: Fetching question info..."
        ):
            info, slug = question.split("__||__")
            Question(slug=slug).get_problem_content()
        rich.print(":white_check_mark: Job done!")

        show_questions(
            required_questions=required_questions, optional_questions=optional_questions
        )
    else:
        exit()
