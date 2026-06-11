import sqlite3
import pandas as pd


conn = sqlite3.connect("capstone_weather.db")


weather_df = pd.read_csv("weather_data.csv")


weather_df = weather_df.drop_duplicates()

weather_df.columns = weather_df.columns.str.strip()

weather_df = weather_df.fillna("Unknown")


weather_df.to_sql(
    "weather_data",
    conn,
    if_exists="replace",
    index=False
)

print("Cleaned data saved to SQLite database successfully!")


conn.close()