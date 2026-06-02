import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("capstone_weather.db")

# Read CSV files
weather_df = pd.read_csv("weather_data.csv")

# Save CSV data into SQLite table
weather_df.to_sql("weather_data", conn, if_exists="replace", index=False)

# Check if it worked
print("Data saved to SQLite database successfully!")

# Close connection
conn.close()