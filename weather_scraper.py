from selenium import webdriver
import pandas as pd
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

url = "https://www.timeanddate.com/weather/"
driver.get(url)

sleep(2)

print(driver.title)

rows = driver.find_elements("xpath", "//table//tr")

weather_data = []

for row in rows:
    cells = row.find_elements("tag name", "td")

    if len(cells) >= 3:
        city_links = row.find_elements("xpath", ".//a")

        if city_links:
            city = city_links[0].text
            time = cells[1].text
            temperature = cells[-1].text

            weather_data.append({
                "City": city,
                "Time": time,
                "Temperature": temperature
            })

df = pd.DataFrame(weather_data)

print(df.head(10))

df.to_csv("weather_data.csv", index=False)

driver.quit()