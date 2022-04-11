#!/usr/bin/python3
""" necessary mudules to import"""

if __name__ == "__main__":

    import csv
    import json
    import requests
    import sys

    # employee_id = int(sys.argv[1])
    emp_data = ("https://jsonplaceholder.typicode.com/users")
    emp_name = requests.get(emp_data)
    names = json.loads(emp_name.text)
    # name = names['name']
    # user_name = names['username']
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(employee_todo.text)
    export_file = 'todo_all_employees.json'

    json_data = {}
    for user in names:
        username = user['username']
        employee_id = user['id']

        overall_list = []
        for todo in todos:
            if todo['userId'] == employee_id:
                dict_to_append = {}
                dict_to_append['task'] = todo['title']
                dict_to_append['completed'] = todo['completed']
                dict_to_append['username'] = user['username']
                overall_list.append(dict_to_append)
        json_data[str(employee_id)] = overall_list
    with open(export_file, 'w') as file:
        json.dump(json_data, file)
