#!/usr/bin/python3

"""
    Write a Python script that takes in a URL, sends a request to the URL
        and displays the body of the response (decoded in utf-8).

    - You have to manage urllib.error.HTTPError exceptions
        and print: Error code: followed by the HTTP status code
    - You must use the packages urllib and sys
    - You are not allowed to import other packages than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
    - Please test your script in the sandbox provided,
        using the web server running on port 5000

    g@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
    Index
    g@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
    Error code: 401
    g@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
    Error code: 404
    g@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
    Error code: 500
    g@ubuntu:~/0x11$ 
"""

import urllib.request as request
from urllib import error
from sys import argv

if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
