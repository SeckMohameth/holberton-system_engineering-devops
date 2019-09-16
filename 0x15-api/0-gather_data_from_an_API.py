#!/usr/bin/python3
"""Script for restful api"""
import requests
import sys

if __name__ == "__main__":

    """Get info about user"""

    user_id = sys.argv[1]
    employee_name = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(employee_name)
    user_dict = req.json()
    for user in user_dict:
        if int(user.get('id')) == int(user_id):
            name = user.get('name')
            break

    todos = "https://jsonplaceholder.typicode.com/todos"
    req1 = requests.get(todos)
    list_of_task = req1.json()
    completed_task = 0
    total_task = 0
    task_names = []
    for tasks in list_of_task:
        if int(tasks.get("userId")) == int(user_id):
            total_task += 1
            if tasks.get("completed") is True:
                completed_task += 1
                task_names.append(tasks.get("title"))

    print("Employee {} is done with tasks {}/{}:".format(
        name, completed_task, total_task))
    for task in task_names:
        print("\t {}".format(task))
