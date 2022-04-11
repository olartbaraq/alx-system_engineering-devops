#!/usr/bin/python3
""" necessary mudules to import"""

if __name__ == "__main__":

    import csv
    import json
    import requests
    import sys

    employee_id = int(sys.argv[1])
    emp_data = ("https://jsonplaceholder.typicode.com/users/{}".
                format(employee_id))
    emp_name = requests.get(emp_data)
    names = json.loads(emp_name.text)
    name = names['name']
    user_name = names['username']
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(employee_todo.text)

    export_file = '{}.csv'.format(employee_id)
    with open(export_file, 'w') as file:
        for todo in todos:
            if todo['userId'] == employee_id:
                task_status = todo['completed']
                task_title = todo['title']
                user_id = todo['userId']
                csv_data = '"{}","{}","{}","{}"\n'\
                    .format(user_id, user_name, task_status, task_title)
                file.write(csv_data)
