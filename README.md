# YaYa Wallet Webhook Integration

This project provides a webhook endpoint for receiving real-time transaction notifications from YaYa Wallet. The webhook verifies the authenticity of incoming notifications, prevents replay attacks, and stores the transaction details in a PostgreSQL database.

## Features
- Webhook endpoint built with Flask
- HMAC SHA256 signature verification to ensure notifications are from YaYa Wallet
- Replay attack prevention by timestamp validation
- Data persistence using PostgreSQL
- Containerized environment using Docker

## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+](https://www.python.org/downloads/)
- PostgreSQL

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/amlaksil/webhook-integration
    cd webhook-integration
    ```

2. Set up environment variables:
    - Create a `.env` file in the project root with the following contents:
      ```bash
      DATABASE_URL=postgresql://your_user:your_password@db/your_db
      WEBHOOK_SECRET=your_secret_key
      ```

3. Build and start the Docker containers:
    ```bash
    docker-compose up -d
    ```
The webhook endpoint will be available at `http://localhost:5000/webhook`.


### Testing the Endpoint
You can test the endpoint by sending a POST request with the expected JSON payload and the `YAYA-SIGNATURE` header. Here's an example using `curl`:

```bash
curl -X POST http://localhost:5000/webhook \
     -H "Content-Type: application/json" \
     -H "YAYA-SIGNATURE: <calculated-signature>" \
     -d '{
          "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
          "amount": 100,
          "currency": "ETB",
          "created_at_time": 1673381836,
          "timestamp": 1701272333,
          "cause": "Testing",
          "full_name": "Abebe Kebede",
          "account_name": "abebekebede1",
          "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
        }'
```
