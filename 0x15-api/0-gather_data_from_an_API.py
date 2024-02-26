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

    totalTasks = 0

    for tasks in json_:
        if tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_)))

    for tasks in json_:
        if tasks['completed']:
            print("\t " + tasks.get('title'))
