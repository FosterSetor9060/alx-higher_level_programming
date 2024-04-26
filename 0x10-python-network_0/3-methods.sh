#!/bin/bash
# the valid script displaying all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
