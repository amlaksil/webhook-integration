-- Check if user exists, and create if it doesn't
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '<POSTGRES_USER>') THEN
      CREATE USER "<POSTGRES_USER>" WITH PASSWORD '<POSTGRES_PASSWORD>';
   END IF;
END
$$;

-- Check if database exists, and create if it doesn't
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = '<POSTGRES_DB>') THEN
      CREATE DATABASE "<POSTGRES_DB>";
   END IF;
END
$$;

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON DATABASE "<POSTGRES_DB>" TO "<POSTGRES_USER>";
