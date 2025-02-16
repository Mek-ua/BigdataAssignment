import pandas as pd

# Load extracted data
df = pd.read_csv("data/ecommerce_raw.csv")

# Data Cleaning
df.dropna(inplace=True)  # Remove missing values
df.drop_duplicates(inplace=True)  # Remove duplicates
df["geolocation_zip_code_prefix"] = df["geolocation_zip_code_prefix"].astype(str)  # Ensure zip codes are strings

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Save cleaned data
df.to_csv("data/ecommerce_cleaned.csv", index=False)

print("✅ Data Transformation Complete!")
