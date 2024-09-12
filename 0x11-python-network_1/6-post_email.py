#!/usr/bin/python3

"""
    Write a Python script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.

    - The email must be sent in the variable email
    - You must use the packages requests and sys
    - You are not allowed to import packages other
        than requests and sys
    - You don’t need to error check arguments
    passed to the script (number or type)

    g@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email
    Your email is: hr@holbertonschool.com
    g@ubuntu:~/0x11$ 
"""

import requests
from sys import argv


if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
