#!/usr/bin/python3
"""for a given employee ID, this script returns
information about his/her TODO list progress."""

import json
import requests


if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_do = to_do.json()
    all_todo = {}

    for user in users:
        tasks = []
        for task in to_do:
            if task.get('userId') == user.get('id'):
                tDict_ = {"username": user.get('username'),
                          "task": task.get('title'),
                          "completed": task.get('completed')}
                tasks.append(tDict_)
        all_todo[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
