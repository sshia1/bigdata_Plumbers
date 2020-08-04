#!/bin/sh

python3.8 test-yelp-api.py | tr "{" "\n" | tr "}" "\n" | tr "," "\n" | more
