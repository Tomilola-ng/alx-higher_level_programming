#!/usr/bin/python3
"""
    Write a Python script that takes in a letter
        and sends a POST request to http://0.0.0.0:5000/search_user
        with the letter as a parameter.

    The letter must be sent in the variable q

    g@ubuntu:~/0x11$ ./8-json_api.py 
    No result
    guillaume@ubuntu:~/0x11$ ./8-json_api.py a
    [8446] amnirqhtfjq
    guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
    No result
    guillaume@ubuntu:~/0x11$ ./8-json_api.py b
    [7094] bmofakakhke
    guillaume@ubuntu:~/0x11$
"""

import requests
from sys import argv

if __name__ == '__main__':
    URL = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(URL, data=data)
    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
