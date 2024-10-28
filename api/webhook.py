#!/usr/bin/python3
"""
API endpoint to handle incoming webhooks and verify their authenticity.
"""
import hmac
import hashlib
import os
import datetime
from flask import Blueprint, request, jsonify
from models.db import get_session, Transaction
from api import webhook_blueprint

webhook_blueprint = Blueprint('webhook', __name__)

def verify_signature(payload, received_signature, secret_key):
    """
    Verify the HMAC SHA256 signature of the incoming payload.
    """
    signed_payload = ''.join(str(payload[key]) for key in payload)
    expected_signature = hmac.new(
            secret_key.encode(),
            signed_payload.encode(),
            hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, received_signature)

@webhook_blueprint.route('/webhook', methods=['POST'])
def webhook():
    """
    Handle incoming webhook requests by verifying the signature,
    checking for replay attacks, and storing the data if valid.
    """
    request_data = request.get_json()
    signature = request.headers.get('YAYA-SIGNATURE')
    timestamp = request_data.get('timestamp')

    # Check for replay attacks
    time_difference = datetime.datetime.utcnow() - \
            datetime.datetime.fromtimestamp(timestamp)
    if time_difference > datetime.timedelta(minutes=5):
        return jsonify({'status': 'Replay attack detected'}), 400

    secret_key = os.getenv('WEBHOOK_SECRET', '')
    if not verify_signature(request_data, signature, secret_key):
        return jsonify({'status': 'Invalid signature'}), 403

    # Store the payload in the database
    with get_session() as session:
        transaction = Transaction(**request_data)
        session.add(transaction)
        session.commit()

    return jsonify({'message': 'Transaction recorded successfully'}), 200