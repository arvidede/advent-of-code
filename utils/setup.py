from distutils.dir_util import copy_tree
from dotenv import load_dotenv
from pathlib import Path
from sys import argv
import requests
import datetime
import os


def get_year_day():
    if len(argv) > 1:
        return int(argv[1]), int(argv[2])
    today = datetime.datetime.today()
    return str(today.year), str(today.day)


def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(
        url, cookies={"session": os.getenv("SESSION_COOKIE")}
    )
    if response.status_code == 200:
        return response.text


def setup():
    load_dotenv()
    root_dir = Path(__file__).absolute().parent
    year, day = get_year_day()
    data = get_input(year, day)

    if data:
        path = root_dir.joinpath(f"../solutions/{year}/{day}").__str__()
        copy_tree(root_dir.joinpath("template").__str__(), path)
        with open(path + "/data.txt", "w+") as f:
            f.write(data)


if __name__ == "__main__":
    setup()
