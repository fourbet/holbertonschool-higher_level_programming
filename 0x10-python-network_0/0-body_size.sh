#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -o /dev/null -sw "%{size_download}" "$1"
