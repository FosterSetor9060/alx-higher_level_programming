#!/bin/bash
# This script takes a URL as input and sending request to the URL

# Send a GET request to the provided URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

