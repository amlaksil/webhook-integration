#!/usr/bin/python3
"""
Main entry point for the webhook integration application.
"""
from os import getenv
from api import app
from models.db import init_db

if __name__ == '__main__':
    host = getenv('HOST', '0.0.0.0')
    port = int(getenv('PORT', '5000'))
    init_db()  # Ensure the database is initialized
    app.run(host, port)
