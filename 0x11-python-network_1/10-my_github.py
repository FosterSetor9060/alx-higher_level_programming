#!/usr/bin/python3
"""
Python script taking GitHub credentials
and uses the GitHub API to display the user id
"""
import requests
import sys

def get_github_id(username, password):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    auth = (username, password)
    
    try:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            return user_data.get("id")
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 10-my_github.py <username> <token>")
        sys.exit(1)
    
    username = sys.argv[1]
    token = sys.argv[2]
    
    github_id = get_github_id(username, token)
    print(github_id)

