"""
Registers the webhook blueprint to handle incoming webhook requests.
"""
from flask import Flask
from api.webhook import webhook_blueprint

app = Flask(__name__)
app.register_blueprint(webhook_blueprint)
