#!/usr/bin/python3

"""
    Write a Python script that takes in a URL,
    sends a request to the URL
    and displays the value of the X-Request-Id variable
        found in the header of the response.

    - You must use the packages urllib and sys
    - You are not allow to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script
    - You must use a with statement

    Example:
    g@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
    g@ubuntu:~/0x11$ 
    g@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
    g@ubuntu:~/0x11$ 
"""


import urllib.request as request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as r:
        print(r.getheader("X-Request-Id"))
