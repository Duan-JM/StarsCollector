"""Core.py contains core functions for stars_collecter module

    Author: Duan-JM
    Email: vincent.duan95@outlook.com
    ChangeLog:
        2020-09-27: get StarredRepo and print them out with github api
"""

from argparse import ArgumentParser, Namespace
import requests


def getStarsFrom(githubID: str) -> list:
    url = f'https://api.github.com/users/{githubID}/starred'
    results = requests.get(url)
    if results.status_code == 200:
        return results.json()
    raise RuntimeError('Failed to fetch starred repo with {}'.format(url))

def getUserCommandInputs() -> Namespace:
    inputParser = ArgumentParser(description='Welcome to Stars Collecter')
    inputParser.add_argument('-id', '--github_id', action='store',
                            type=str, help='The target githubID')
    userInputs = inputParser.parse_args()
    return userInputs

def printSingleRepoInfo(singleRepoInfo: dict):
    print(f'repo_name:{singleRepoInfo["full_name"]}')
    print(f'description: {singleRepoInfo["description"]}')
    print(f'repo_url: {singleRepoInfo["html_url"]}')
    print(f'is_fored: {singleRepoInfo["fork"]}')
    print('='*40)

def printResults():
    userInputs = getUserCommandInputs()
    fullInformationForStarredRepo = getStarsFrom(userInputs.github_id)
    for singleRepoInfo in fullInformationForStarredRepo:
        printSingleRepoInfo(singleRepoInfo)
