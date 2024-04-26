#!/bin/bash
# vthe script showcase URL as an argument, sent GET request and displays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"
