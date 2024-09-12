#!/usr/bin/python3

"""
    Write a Python script that fetches https://alx-intranet.hbtn.io/status

        You must use the package urllib
        You are not allowed to import any packages other than urllib
        The body of the response must be displayed like the following example (tabulation before -)
        You must use a with statement

        Example:
            guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
            Body response:$
                - type: <class 'bytes'>$
                - content: b'OK'$
                - utf8 content: OK$
            guillaume@ubuntu:~/0x11$ 
"""

import urllib.request

URL = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(URL) as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
