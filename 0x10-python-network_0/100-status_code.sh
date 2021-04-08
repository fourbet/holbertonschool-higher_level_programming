#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the status code of the response
curl -o /dev/null -sw "%{response_code}" "$1"
