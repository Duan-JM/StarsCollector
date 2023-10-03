"""Core.py contains core functions for stars_collecter module

    Author: Duan-JM
    Email: vincent.duan95@outlook.com
    ChangeLog:
        2020-09-27: get StarredRepo and print them out with github api
"""

from argparse import ArgumentParser, Namespace
from typing import List

import requests
from retry import retry

MAX_PAGE_CNT = 10000
REQUEST_TIMEOUT = 5


def check_if_results_avaliable(results: List):
    for result in results:
        for key in ["full_name", "description", "html_url", "fork"]:
            if key in result:
                continue
            else:
                print(result)
                return False
    return True


@retry(tries=3, delay=1)
def request_github(page_cnt: int, github_id: str):
    url = f"https://api.github.com/users/{github_id}/starred?page={page_cnt}"
    results = requests.get(url, timeout=REQUEST_TIMEOUT)
    return results


def getStarsFrom(github_id: str) -> list:
    combined_results = list()
    page_cnt = 1
    while True or page_cnt > MAX_PAGE_CNT:
        results = request_github(page_cnt=page_cnt, github_id=github_id)
        if results.status_code == 200 and check_if_results_avaliable(results.json()):
            fetched_results = results.json()
            if fetched_results:
                combined_results = combined_results + results.json()
                page_cnt += 1
                print(f"SC Fetching: {page_cnt} page.")
            else:
                break
        else:
            assert RuntimeError, f"{results.status_code} with results.json()"

    print(f"[INFO] Fetched {page_cnt}, fecthed {len(combined_results)}")
    return combined_results


def getUserCommandInputs() -> Namespace:
    inputParser = ArgumentParser(description="Welcome to Stars Collecter")
    inputParser.add_argument(
        "-id", "--github_id", action="store", type=str, help="The target githubID"
    )
    userInputs = inputParser.parse_args()
    return userInputs


def printSingleRepoInfo(singleRepoInfo: dict):
    print(f'repo_name:{singleRepoInfo["full_name"]}')
    print(f'description: {singleRepoInfo["description"]}')
    print(f'repo_url: {singleRepoInfo["html_url"]}')
    print(f'is_fored: {singleRepoInfo["fork"]}')
    print("=" * 40)


def printResults():
    userInputs = getUserCommandInputs()
    fullInformationForStarredRepo = getStarsFrom(userInputs.github_id)
    for singleRepoInfo in fullInformationForStarredRepo:
        printSingleRepoInfo(singleRepoInfo)
    print(f"[INFO] SC fetched {len(fullInformationForStarredRepo)} repos successfully")
