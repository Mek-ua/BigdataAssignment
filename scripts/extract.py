import pandas as pd

# Load dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Display sample data
print(df.head(20))

# Save a copy
df.to_csv("data/ecommerce_raw.csv", index=False)
