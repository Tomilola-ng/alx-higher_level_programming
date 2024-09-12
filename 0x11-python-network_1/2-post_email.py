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


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    DATA = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make the POST request
    with urllib.request.urlopen(url, DATA) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
