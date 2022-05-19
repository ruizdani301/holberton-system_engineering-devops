#!/usr/bin/python3
"""using this REST API, for a given employee ID, return list progress"""
import requests
from sys import argv

if __name__ == "__main__":

    i = 0
    j = 0
    user = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
    user_json = user.json()
    task = ""
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            if t['completed']:
                task += '\t' + t['title'] + '\n'
                i += 1
            j += 1
    print("Employee {} is done with tasks({}/{}):".format(user_json["name"], i, j))
    print(task, end='')
