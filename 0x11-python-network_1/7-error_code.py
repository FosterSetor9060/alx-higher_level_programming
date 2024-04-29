#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""
import requests
import sys

def fetch_url_content(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 7-error_code.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_url_content(url)

