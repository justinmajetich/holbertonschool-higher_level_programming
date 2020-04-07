#!/usr/bin/env bash
# Make request and display response
url="$1"
curl -sI "$url" | grep "Content-Length" | cut -d ' ' -f 2
