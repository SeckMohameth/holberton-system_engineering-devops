#!/usr/bin/python3
"""Script for restful api"""
import requests
import sys
import json

if __name__ == "__main__":

    """Get info about user"""

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    filename = user_id + ".json"

    employee = requests.get(url + "users/" + user_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + user_id)
    tasks = tasks.json()

    task_list = []
    for x in tasks:
        task_list.append(x)

    stuff = {}
    stuff[user_id] = task_list

    with open(filename, mode="w") as json_file:
        json.dump(stuff, json_file)
