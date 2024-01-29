#!/usr/bin/python3
"""Export to-do list information to JSON format."""
import json
import requests

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com/"
    users = requests.get(uri + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(uri + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, f)
