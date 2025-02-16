import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
db_params = {
    "dbname": "ecommerce_db",
    "user": "postgres",
    "password": "post",  # Replace with your actual password
    "host": "localhost",
    "port": "5432"
}
conn = psycopg2.connect(**db_params)

# Load data
df = pd.read_sql("SELECT latitude, longitude, city, state FROM ecommerce_data", conn)
conn.close()

# ✅ Scatter Plot of Geolocation Data
plt.figure(figsize=(10, 6))
plt.scatter(df["longitude"], df["latitude"], alpha=0.5, c='red')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographical Distribution of Locations")
plt.show()

# ✅ Bar Plot of Cities
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="city", order=df["city"].value_counts().index)
plt.xticks(rotation=90)
plt.title("Number of Entries Per City")
plt.show()
