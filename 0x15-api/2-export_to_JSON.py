#!/usr/bin/python3
"""Python script to export data in the JSON format:
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "
completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + "/" + employee_id

    response = requests.get(user_url)
    username = response.json().get('username')

    todo_url = user_url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    task_list = []
    for task in tasks:
        task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                }
        task_list.append(task_dict)

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump({employee_id: task_list}, jsonfile)
