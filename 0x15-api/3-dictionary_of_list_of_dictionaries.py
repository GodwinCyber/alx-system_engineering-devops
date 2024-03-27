#!/usr/bin/python3
"""Python script to export data in the JSON format:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
"USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""
import json
import requests


def export_all_tasks_to_json():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Cannot fetch data from the API.")
        return

    users = users_response.json()
    todos = todos_response.json()

    user_tasks = {}
    for user in users:
        user_id = user["id"]
        user_tasks[str(user_id)] = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
            if task["userId"] == user_id
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)


export_all_tasks_to_json()
