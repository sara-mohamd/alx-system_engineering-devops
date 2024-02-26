#!/usr/bin/python3
"""for a given employee ID, this script returns
information about his/her TODO list progress."""

import json
import requests
from sys import argv


if __name__ == "__main__":

    session = requests.Session()

    id_ = argv[1]
    id_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)
    name_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)

    employeeID = session.get(id_URL)
    employeeName = session.get(name_URL)

    json_ = employeeID.json()
    name = employeeName.json()['name']
    usrname = employeeName.json()['username']

    totalTasks = []
    updatedUser = {}

    for tasks in json_:
        totalTasks.append(
            {
                "task": tasks.get('title'),
                "completed": tasks.get('completed'),
                "username": usrname,
            })

    updatedUser[id_] = totalTasks

    jsonFile = id_ + ".json"
    with open(jsonFile, 'w') as f:
        json.dump(updatedUser, f)
