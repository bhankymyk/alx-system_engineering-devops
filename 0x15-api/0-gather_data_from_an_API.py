#!/usr/bin/python3
"""
This scripts returns information about a TO DO list progress.
for a given employee ID using a given REST API.
"""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]

    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id))
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(
            user_id))

    if len(user.json()):
        total = 0
        completed = 0
        tasks_list = []
        for tarea in todos.json():
            total += 1
            if tarea.get("completed") is True:
                completed += 1
                tasks_list.append(tarea.get("title"))

        print(
            "Employee {} is done with tasks({}/{}):".format(
                user.json().get("name"), completed, total))
        for task in tasks_list:
            print("\t {}".format(task))
