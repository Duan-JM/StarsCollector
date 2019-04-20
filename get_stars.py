"""
File: get_stars.py
Author: VDeamoV
Email: vincent.duan95@outlook.com
Github: https://github.com/VDeamoV
Description: This Script is to get the Repo you Stared
    and then write it into the README
"""
import argparse
import requests


def get_stars(your_name):
    """
    params: USER_NAME <string> your github names
    return: <json> Stars Repo information
    """
    url = f'https://api.github.com/users/{your_name}/starred'
    results = requests.get(url)
    if results.status_code == 200:
        print("Stars Repo Gets")
    return results.json()

def get_exist_stars(path_file):
    """
    Get the existing repos in README
    """
    output_results = []
    with open(path_file, 'r') as f:
        results = f.readlines()
        for item in results:
            if item[0] == '+':
                output_results.append(item[2:-1])
    return output_results

def write_new(file_path):
    """
    Add new Starred Repo to the READMEME
    """
    full_inform = get_stars(USER_NAME)
    exist_inform = get_exist_stars(README_PATH)
    with open(file_path, 'a') as f:
        print("Now Add Use Stared Repo to README")
        for item in full_inform:
            if item['full_name'] not in exist_inform:
                print(item['full_name'])
                f.writelines(f"+ {item['full_name']}\n")

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Welcome to AutoStar Collecter')
    PARSER.add_argument('-u', dest='user', action='store', type=str,
                        help='input your user name')
    PARSER.add_argument('-p', dest='file_path', default='../README.md', action='store', type=str,
                        help='input your user name')
    ARGS = PARSER.parse_args()
    if ARGS.user:
        USER_NAME = ARGS.user
    else:
        raise Exception("Please input your Github Names")
    README_PATH = ARGS.file_path
    write_new(README_PATH)
