#!/usr/bin/python3
"""
Python script takes in a URL,
sends a request to the URL and displays the body of the response.
Usage: ./7-error_code.py <URL>
"""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    response = get(url)
    ERR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERR_TXT.format(status) if (status >= 400) else response.text)
