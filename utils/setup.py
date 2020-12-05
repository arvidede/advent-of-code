from distutils.dir_util import copy_tree
from dotenv import load_dotenv
from pathlib import Path
import requests
import datetime
import os


def get_input(day):
    url = f'https://adventofcode.com/2020/day/{day}/input'
    response = requests.get(
        url, cookies={'session': os.getenv('SESSION_COOKIE')})
    if response.status_code == 200:
        return response.text


def setup():
    load_dotenv()
    root_dir = Path(__file__).absolute().parent
    today = str(datetime.datetime.today().day)
    data = get_input(today)

    if data:
        path = root_dir.joinpath(f"../solutions/{today}").__str__()
        copy_tree(root_dir.joinpath('template').__str__(),
                  path)
        with open(path + '/data.txt', 'w+') as f:
            f.write(data)


if __name__ == "__main__":
    setup()
