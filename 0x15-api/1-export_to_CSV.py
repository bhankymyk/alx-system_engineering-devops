#!/usr/bin/python3
"""
This script to export task done in task #0 to CSV format
"""

import csv
import requests
from sys import orig_argv

if __name__ == "__main__":
    user_id = argv[1]

    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id))
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(
            user_id))

    with open('{}.csv'.format(user_id), "w") as output:
        writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL)
        for tarea in todos.json():
            data = [
                user.json().get('id'),
                user.json().get('username'),
                tarea.get('completed'),
                tarea.get('title')
            ]
            writer.writerow(data)
