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
    #user_name = names['username']
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(employee_todo.text)

    export_file = '{}.json'.format(employee_id)
    overall_list = []
    with open(export_file, 'w') as file:
        for todo in todos:
            if todo['userId'] == employee_id:
                dict_to_append = {}
                dict_to_append['task'] = todo['title']
                dict_to_append['completed'] = todo['completed']
                dict_to_append['username'] = names['username']
                overall_list.append(dict_to_append)
        json_data = {}
        json_data[str(employee_id)] = overall_list
        json.dump(json_data, file)
