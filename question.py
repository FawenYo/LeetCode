import os
import re
from typing import List

import html2markdown
import requests


class Question:
    def __init__(self) -> None:
        self.slug: str = ""  # LeetCode question slug
        self.folder_path: str = ""  # Folder path
        self.question_data: dict = {}  # LeetCode question data
        self.question_content: str = (
            ""  # LeetCode question content (str, Markdown format)
        )

    def get_problem_content(self, slug: str) -> None:
        print(f"{slug} fetching...")
        self.fetch_question()

        try:
            os.makedirs(self.folder_path)
        except FileExistsError:
            pass

        # Question markdown file
        self.create_question_md()
        # Question python3 file
        self.create_solution_py()

        print("done!")

    def fetch_question(self) -> None:
        """Fetch question data using graghql"""
        url = "https://leetcode.com/graphql"
        json = {
            "operationName": "questionData",
            "variables": {"titleSlug": slug},
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
            question_url = f"https://leetcode.com/problems/{slug}/"
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
                code = self.python_snippets(
                    codeSnippets=self.question_data["codeSnippets"]
                )
                question_file.writelines(code)
        except FileExistsError:
            pass


if __name__ == "__main__":
    problems = [
        "Merge Two Binary Trees",
    ]
    for question in problems:
        slug = question.lower().replace(" ", "-")
        Question().get_problem_content(slug=slug)
