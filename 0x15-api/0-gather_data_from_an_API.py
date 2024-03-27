#!/usr/bin/python3
"""Python script that, using this REST API, for agiven employee
ID, returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        user_id = int(argv[1])
        user_url = (
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(user_id))
        todos_url = (
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user_id))

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code == 200 and \
                todos_response.status_code == 200:
            user = user_response.json()
            todos = todos_response.json()

            total_tasks = len(todos)
            completed_tasks = sum(task["completed"] for task in todos)
            completed_task_titles = [
                task["title"] for task in todos if task["completed"]
            ]

            print(
                "Employee {} is done with tasks({}/{}):".format(
                    user["name"], (completed_tasks), (total_tasks)
                )
            )
            for title in completed_task_titles:
                print("\t {}".format(title))
        else:
            print("Failed to retrieve DATA for user ID: {}".format(user_id))
    else:
        print("Usage: {} <employee ID>".format(argv[0]))
