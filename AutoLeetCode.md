# Auto LeetCode

![release](https://img.shields.io/badge/Latest%20release-1.0.0-blue)

![Demo Image](https://i.imgur.com/lBW5v3U.png)
The project is aimed to automate the LeetCode exercise process.

## Features

* Docs: Auto create `./{Question}/` folder that contains `QUESTION.md` and `{question}.py`
* Answer checking: Check code correct with simple one click

## Usage

### Requirements

* Python 3.7 or newer version (below version might encounter f-string error or asyncio error)

### Steps

1. Download project files

Make sure to download the latest build from [Release Page](https://github.com/FawenYo/LeetCode/releases). Remember to extract it after downloading the file.

2. Configure `run.py`

You can edit the download option in `run.py`.

> ❗ If you are members of LINE group "LeetCode 刷刷鍋", make sure to change `FETCH_FROM_SERVER` to `True`

3. Run the tool

Simply open your terminal app and navigate to project, type

```shell
python3 run.py
```

and it will automatically fetch the problems and create related files.

4. Check Solution (Optional)

After writing up your Python solution, simply just run your python script, and it will check if your code output is correct or not.

## TODO

* [ ] Add option to check solution with LeetCode server
