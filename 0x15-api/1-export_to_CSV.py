#!/usr/bin/python3
"""using this REST API, for a given employee ID, return list progress"""
import requests
import csv
from sys import argv

if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1]
                        )
    user_dic = user.json()
    user = user_dic["username"]

    taskarr = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    labels = ['user_id', 'username', 'completed', 'title']
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            task = {}
            task["user_id"] = t["userId"]
            task["username"] = user
            task["completed"] = t["completed"]
            task["title"] = t["title"]
            taskarr.append(task)

    try:
        id = argv[1] + ".csv"
        with open(id, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=labels,
                                    quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for elem in taskarr:
                writer.writerow(elem)
    except IOError:
        print("I/O error")
