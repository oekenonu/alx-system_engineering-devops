#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her TODO list progress.
'''

if __name__ == '__main__':
    import requests
    import sys

    task_done = 0
    task_title = []
    u_id = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(u_id)).json()
    uname = req.get("username")
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(u_id)).json()
    for item in req:
        if item.get('completed') is True:
            task_title.append(item.get('title'))
            task_done += 1
    total_task = len(req)

    print('Employee {} is done with tasks({}/{}):'.
          format(uname, task_done, total_task))
    for title in task_title:
        print('\t {}'.format(title))
