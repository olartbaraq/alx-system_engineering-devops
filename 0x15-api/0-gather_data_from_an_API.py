#!/usr/bin/python3
""" necessary mudules to import"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    
    employee_id = int(sys.argv[1])
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(employee_todo.text)
    emp_data = ("https://jsonplaceholder.typicode.com/users/{}".
                format(employee_id))
    emp_name = requests.get(emp_data)
    names = json.loads(emp_name.text)
    name = names['name']

    num_tasks = 0
    total_tasks = 0
    for todo in todos:
        if todo['userId'] == employee_id:
            total_tasks += 1
            if todo['completed']:
                num_tasks += 1
    print("Employee {:s} is done with tasks({}/{}):".
          format(name, num_tasks, total_tasks))
    for todo in todos:
        if todo['userId'] == employee_id and todo['completed']:
            print("\t {}".format(todo['title']))
