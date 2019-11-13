#!/bin/sh

# Setting up virtual environment search path
export WORKON_HOME=/Users/rishabhojha/py3eg/Flask/VirtualEnv/CS50

# DATABASE URL for flask connecting to heruko remote db
export DATABASE_URL=postgres://zqhcevceeozhxe:a83aa2b5c263e8a3bbaa084b95e8cb74c08dd7bd6ad3bd822bb95e128526fad7@ec2-54-235-246-201.compute-1.amazonaws.com:5432/d1a0orptvtu5a7

# Flask application variables
export FLASK_APP=application.py
export FLASK_DEBUG=1
