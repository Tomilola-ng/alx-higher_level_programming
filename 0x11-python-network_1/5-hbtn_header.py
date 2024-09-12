#!/usr/bin/python3

"""
    Write a Python script that takes in a URL,
    sends a request to the URL
    and displays the value of the variable X-Request-Id
        in the response header

    - You must use the packages requests and sys
    - You are not allow to import other packages than requests and sys
    - The value of this variable is different for each request
    - You don’t need to check script arguments (number and type)

    Example:
    g@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
    5e52e160-c822-4669-8b3a-8b3bbca7b090
    g@ubuntu:~/0x11$ 
    g@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
    eaceaf35-bc0f-4f74-994a-7be0728ec654
    g@ubuntu:~/0x11$ 
"""

import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
