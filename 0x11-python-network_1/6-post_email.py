#!/usr/bin/python3
"""
Python script taking in a URL and an email address,
sends a POST request to the passed URL with the email,
and displaying the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
