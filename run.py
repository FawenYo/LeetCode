from auto_code.main import AutoLeetCode
from auto_code.setting_model import Setting

setting = Setting()

"""Download Settings

Args:
    setting.QUESTIONS (List[str]): Self-selected questions. ex. ["Two Sum", "Add Two Numbers"].
    setting.FETCH_FROM_SERVER (bool): Fetch questions of LINE group from server. Defaults to False.
    setting.SHOW_QUESTIONS (bool): Show downloaded question info. Defaults to True.
"""
setting.QUESTIONS = ["Rotate Image"]
setting.FETCH_FROM_SERVER = True
setting.SHOW_QUESTIONS = True

"""Fetch from Server Settings

Args:
    setting.DATE (str): End date of the work. Format: "%Y-%m-%d".
    setting.OPTIONAL (bool): Fetch optional question. Defaults to True.
"""
setting.DATE = "2021-05-16"
setting.OPTIONAL = True


if __name__ == "__main__":
    AutoLeetCode().run(setting=setting)
