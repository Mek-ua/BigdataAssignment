CREATE DATABASE ecommerce_db;

CREATE TABLE ecommerce_data (
    id SERIAL PRIMARY KEY,
    zip_code_prefix TEXT,
    latitude FLOAT,
    longitude FLOAT,
    city TEXT,
    state TEXT
);
