import asyncio
import time
from asyncio.tasks import Task
from datetime import datetime
from typing import Coroutine, List, Tuple

import requests
import rich.progress
import rich.table
from aiohttp import ClientSession

from auto_code.actions import Question
from auto_code.setting_model import Setting, console


class AutoLeetCode:
    def __init__(self) -> None:
        self.setting: Setting = Setting

    def run(self, setting: Setting) -> None:
        self.setting = setting
        if self.setting.FETCH_FROM_SERVER:
            required_questions, optional_questions = self.fetch_questions(
                date=self.setting.DATE
            )

            if self.setting.OPTIONAL:
                problems = required_questions + optional_questions
            else:
                problems = required_questions
                optional_questions = []

        else:
            problems = []
            required_questions = []
            questions = self.setting.QUESTIONS
            for each in questions:
                temp = each.lower().replace(" ", "-")
                problems.append(temp)
                required_questions.append(temp)
            optional_questions = []

        if problems:
            start_time = time.time()
            asyncio.run(self.start(problems=problems))
            console.print(
                f":white_check_mark: Job done! Elapsed time: {time.time() - start_time} seconds"
            )
            if self.setting.SHOW_QUESTIONS:
                self.show_questions(
                    required_questions=required_questions,
                    optional_questions=optional_questions,
                )
        else:
            exit()

    def fetch_questions(self, date: str) -> Tuple[List[str]]:
        """Fetch week questions from server

        Args:
            date (str): End date of work

        Returns:
            Tuple[List[str]]: ([required_questions], [optional_questions])
        """
        console.print(f":truck: Fetching {date} questions from server...")
        server_url = f"https://leetcode-bot.ml/get_question?date={date}"
        response = requests.get(url=server_url).json()

        if response["code"] == 200:
            console.print(":o: Successfully fetched questions list!")
            return (response["required_questions"], response["optional_questions"])
        else:
            problems = ([], [])
            console.print(f":x: {response['error']['message']}")
        return problems

    def show_questions(
        self, required_questions: List[str], optional_questions: List[str]
    ) -> None:
        """Show week questions

        Args:
            required_questions (List[str]): Required questions
            optional_questions (List[str]): Optional questions
        """
        current_date = datetime.now()
        table = rich.table.Table(
            title=f"{current_date.year}/{current_date.month}/{current_date.day} questions"
        )
        table.add_column("Type", style="green")
        table.add_column("Title", style="magenta")
        table.add_column("URL", style="blue")

        for question in required_questions:
            if "__||__" in question:
                info, slug = question.split("__||__")
            else:
                info = ""
                for each_phrase in question.split("-"):
                    info += each_phrase[0].capitalize() + each_phrase[1:] + " "
                info.strip(" ")
                slug = question
            table.add_row("Required", info, f"https://leetcode.com/problems/{slug}/")

        for question in optional_questions:
            if "__||__" in question:
                info, slug = question.split("__||__")
            else:
                slug = question
            table.add_row("Optional", info, f"https://leetcode.com/problems/{slug}/")

        rich.console.Console().print(table)

    async def start(self, problems: List[str]) -> Coroutine:
        jobs: List[Task] = []
        async with ClientSession() as session:
            for question in problems:
                if "__||__" in question:
                    info, slug = question.split("__||__")
                else:
                    slug = question
                jobs.append(
                    asyncio.create_task(
                        Question(slug=slug).fetch_question(session=session)
                    )
                )
            for job in rich.progress.track(
                jobs, description=":page_with_curl: Fetching question info..."
            ):
                await job
