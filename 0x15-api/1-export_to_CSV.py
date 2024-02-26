#!/usr/bin/python3
"""for a given employee ID, this script returns
information about his/her TODO list progress."""

import csv
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
#    name = employeeName.json()['name']
    usrname = employeeName.json()['username']

    totalTasks = 0

    for tasks in json_:
        if tasks['completed']:
            totalTasks += 1

    csvFile = id_ + ".csv"

    with open(csvFile, "w", newline='') as f:
        fileWriting = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for line in json_:
            fileWriting.writerow([id_, usrname,
                                  line.get('completed'), line.get('title')])
