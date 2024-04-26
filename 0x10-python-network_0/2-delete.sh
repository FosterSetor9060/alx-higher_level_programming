#!/bin/bash
# sending a DELETE request => URL passed as the first argument
curl -s "$1" -X DELETE
