#!/bin/bash
# Make request and display response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
