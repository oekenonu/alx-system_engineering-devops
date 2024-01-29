#!/usr/bin/python3
"""Returns information on TODO list for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(uri + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(stat)) for stat in completed]
