#!/usr/bin/python3

"""
    Write a Python script that takes in a URL,
    sends a request to the URL and displays the body of the response.

    g@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
    Index
    g@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
    Error code: 401
    g@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
    Error code: 404
    g@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
    Error code: 500
    g@ubuntu:~/0x11$ 
"""

import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
