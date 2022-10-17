#!/usr/bin/python3
"""
This scripts returns information about a TO DO list progress.
for a given employee ID using a given REST API.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo_list = requests.get(url + "todo", params={"userId": argv[1]}).json()

    EMPLOYEE_NAME = user.get('name')
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0

    for task in todo_list:
        if task.get('completed') is True:
            TASK_TITLE.append(task.get('title'))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(todo_list)
    print("Employee {} is done with task({}/{}):")
    format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)

    for t in TASK_TITLE:
        print("\task {}".format(t))
