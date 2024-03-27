#!/usr/bin/python3
""" Python script to export data in the CSV format:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        with open("{}.csv".format(employee_id), mode="w", newline="") as file:
            write = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos:
                write.writerow(
                    [employee_id, user["username"],
                     task["completed"], task["title"]]
                )
