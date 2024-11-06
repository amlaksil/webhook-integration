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
- [PostgreSQL](https://www.postgresql.org/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/amlaksil/webhook-integration && cd webhook-integration
    ```

2. Set up environment variables:
    - Create a `.env` file in the project root with the following contents:
      ```bash
      # Application settings
      WEBHOOK_SECRET=your_secret_key
	  CORS_ALLOWED_ORIGIN=your_origin

      # Database settings
      POSTGRES_USER=your_user
      POSTGRES_PASSWORD=your_password
      POSTGRES_DB=your_db
      DATABASE_HOST=db
      DATABASE_PORT=5432
      ```

3. Update `setup.sql` with database credentials:
    - Replace the placeholders in `setup.sql` with the values from your `.env` file:
      - `<POSTGRES_USER>` -> `your_user`
      - `<POSTGRES_PASSWORD>` -> `your_password`
      - `<POSTGRES_DB>` -> `your_db`

4. Run the setup script to configure the database and user:
    ```bash
    sudo -u postgres psql -f setup.sql
    ```

5. Build and start the Docker containers:
    ```bash
    docker-compose up -d
    ```
The webhook endpoint will be available at `http://localhost:5000/webhook`.

### Generating a Test Payload and Signature
To test the webhook, you can use the `signature.py` script to generate a test payload (`payload.json`) and the corresponding HMAC SHA256 signature.

1. Run the following command to generate `payload.json`:
    ```bash
    python3 signature.py
    ```
    This script generates a JSON payload and writes it to `payload.json` in the project directory. It also prints the HMAC SHA256 signature to the console, which you can use for testing.

### Testing the Endpoint

1. **Manual Testing with `curl`:** You can test the endpoint by sending a POST request with the `payload.json` file and the `YAYA-SIGNATURE` header containing the generated signature. Here’s an example using `curl`:

    ```bash
    curl -X POST http://localhost:5000/webhook \
         -H "Content-Type: application/json" \
         -H "YAYA-SIGNATURE: <generated-signature>" \
         -d @payload.json
    ```

    Replace `<generated-signature>` with the signature printed by the `signature.py` script.

2. **Automated Testing with `unittest`:** You can also test the app by running the unit tests included in the project. Run the following command:

    ```bash
    python3 -m unittest discover
    ```

    This command will discover and run all tests in the project, helping you verify that the application functions as expected.
