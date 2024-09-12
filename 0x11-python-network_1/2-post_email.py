#!/usr/bin/python3
# pylint: disable=line-too-long

"""
    Write a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)

    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
    - Please test your script in the sandbox provided, using the
        web server running on port 5000

    Example:
        guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
        Your email is: hr@holbertonschool.com
        guillaume@ubuntu:~/0x11$ 
"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    DATA = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], DATA)

    with urllib.request.urlopen(req) as r:
        html = r.read()
        print(f"{format(html.decode('utf-8'))}")
