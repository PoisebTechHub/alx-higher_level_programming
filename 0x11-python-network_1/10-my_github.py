#!/usr/bin/python3
"""A python script that uses the GitHub API to display your GitHub ID
based on given credentials.
Use Basic Authentication with a personal access token
as password to access to your information
(only read:user permission is needed)
"""
import requests
from requests.auth
import sys
import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
