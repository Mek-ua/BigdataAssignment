import pandas as pd
import psycopg2
import os

# Define CSV path
csv_path = os.path.join("data", "ecommerce_data.csv")

# Check if file exists
if not os.path.exists(csv_path):
    print(f"❌ Error: File not found at {csv_path}")
    exit()

# Load CSV
df = pd.read_csv(csv_path)

# Rename columns to match the PostgreSQL table
df.rename(columns={
    "geolocation_zip_code_prefix": "zip_code_prefix",
    "geolocation_lat": "latitude",
    "geolocation_lng": "longitude",
    "geolocation_city": "city",
    "geolocation_state": "state"
}, inplace=True)

# Database connection
db_params = {
    "dbname": "ecommerce_db",
    "user": "postgres",
    "password": "post",  # Replace with your actual password
    "host": "localhost",
    "port": "5432"
}

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Insert data row by row
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO ecommerce_data (zip_code_prefix, latitude, longitude, city, state)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (row["zip_code_prefix"], row["latitude"], row["longitude"], row["city"], row["state"])
        )

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data loaded successfully!")

except Exception as e:
    print("❌ Error:", e)
