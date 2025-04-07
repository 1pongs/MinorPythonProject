import pandas as pd

# Read the CSV file
df = pd.read_csv("C:/Users/Juanito Encinas/Downloads/Restaurant+Orders+CSV/order_details.csv")

# Convert 'order_date' into a proper datetime format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Format the dates as "YYYY-MM-DD"
df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

# Save the cleaned data as a new CSV file
df.to_csv("order_details_fixed.csv", index=False)

# No print statement here—just saving the file.
