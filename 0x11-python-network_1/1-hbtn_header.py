#!/usr/bin/python3

"""
    Write a Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable found in the header of the response.

    - You must use the packages urllib and sys
    - You are not allow to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
    - You must use a with statement

    Example:
    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
    guillaume@ubuntu:~/0x11$ 
    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
    guillaume@ubuntu:~/0x11$ 
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
