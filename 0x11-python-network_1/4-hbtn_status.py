#!/usr/bin/python3
"""
    Write a Python script that fetches https://alx-intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests'
    The body of the response must be display like the
        following example (tabulation before -)
    
    Example:
    guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'str'>$
        - content: OK$
    guillaume@ubuntu:~/0x11$ 
"""

import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    _type = type(response.text)
    text = response.text

    print(f"Body response:\n\t- type: {_type}\n\t- content: {text}")
