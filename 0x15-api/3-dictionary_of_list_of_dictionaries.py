#!/usr/bin/python3
"""Script for restful api"""
import requests
import sys
import json

if __name__ == "__main__":

    """export in json format"""

    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"

    employee = requests.get(url + "users/")
    employee = employee.json()

    work_tasks = {}
    for worker in employee:
        employee_id = employee.get('id')
        tasks = requests.get(url + "todos?userId=" + str(employee_id))
        tasks = tasks.json()

    task_list = []
    for x in tasks:
        task_list.append(x)

    stuff[employee_id] = task_list

    with open(filename, mode="w") as json_file:
        json.dump(stuff, json_file)
