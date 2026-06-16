import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("Weather Around the World Dashboard")

conn = sqlite3.connect("capstone_weather.db")

df = pd.read_sql_query("SELECT * FROM weather_data", conn)

df["Temperature"] = df["Temperature"].str.replace("°F", "", regex=False)
df["Temperature"] = pd.to_numeric(df["Temperature"])
conn.close()

st.write("This dashboard shows weather data collected from the Weather Around the World website.")

st.subheader("Weather Data")
st.dataframe(df)

city = st.selectbox("Select a city", df["City"].unique())

filtered_df = df[df["City"] == city]

st.subheader(f"Weather Information for {city}")
st.dataframe(filtered_df)

fig1 = px.bar(df, x="City", y="Temperature", title="Temperature by City")
st.plotly_chart(fig1)

#fig2 = px.bar(df, x="City", y="Humidity", title="Humidity by City")
#st.plotly_chart(fig2)

#fig3 = px.scatter(df, x="Temperature", y="Humidity", color="City",
                  #title="Temperature vs Humidity")
#st.plotly_chart(fig3)