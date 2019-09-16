#!/usr/bin/python3
"""Script for restful api"""
import requests
import sys
import csv

if __name__ == "__main__":

    """Get info about user"""

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    filename = user_id + ".cvs"

    employee = requests.get(url + "users/" + user_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + user_id)
    tasks = tasks.json()

    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for item in tasks:
            writer.writerow((item.get('userId'), employee.get('username'),
                            item.get('completed'), item.get('title')))
