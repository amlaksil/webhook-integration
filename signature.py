#!/usr/bin/python3
from os import getenv
import json
import hmac
import hashlib
import time
from uuid import uuid4
import json


def generate_signature(payload, secret_key):
    # Concatenate the payload values in the required order
    signed_payload = ''.join(str(payload[key]) for key in payload)

    # Generate the HMAC SHA256 signature
    signature = hmac.new(
            secret_key.encode(),
            signed_payload.encode(),
            hashlib.sha256).hexdigest()
    return signature


if __name__ == "__main__":
    payload = {
        "id": str(uuid4()),
        "amount": 100,
        "currency": "ETB",
        "created_at_time": 1673381836,
        "timestamp": int(time.time()),
        "cause": "Testing",
        "full_name": "Abebe Kebede",
        "account_name": "abebekebede1",
        "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
    }
    with open('payload.json', 'w') as f:
        f.write(json.dumps(payload))
    secret_key = getenv('WEBHOOK_SECRET', '')

    # Generate the signature
    signature = generate_signature(payload, secret_key)
    print(f"Generated Signature\n{signature}")
