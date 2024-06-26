#!/usr/bin/python3
"""A python script that sends a POST request to a given URL with a given email
as parameter and finally displays the body of the response.
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
