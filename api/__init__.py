"""
Registers the webhook blueprint to handle incoming webhook requests.
"""
from os import getenv
from flask import Flask
from flask_cors import CORS
from api.webhook import webhook_blueprint

app = Flask(__name__)
app.register_blueprint(webhook_blueprint)

allowed_origin = getenv("CORS_ALLOWED_ORIGIN", "*")
CORS(app, origins=[allowed_origin], methods=["POST"])
