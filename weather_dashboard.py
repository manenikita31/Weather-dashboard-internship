import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")
# Set style for seaborn
sns.set(style="whitegrid")

#Configuration
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Check response status
if response.status_code != 200:
    print("Error fetching data:", data)
    exit()

# Parse data
timestamps = []
temperatures = []
humidity = []
wind_speeds = []

for entry in data['list']:
    dt = datetime.datetime.fromtimestamp(entry['dt'])
    timestamps.append(dt)
    temperatures.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speeds.append(entry['wind']['speed'])

# Visualization dashboard
plt.figure(figsize=(14, 10))

# Temperature line plot
plt.subplot(3, 1, 1)
sns.lineplot(x=timestamps, y=temperatures, marker="o", color="orange")
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity bar plot
plt.subplot(3, 1, 2)
sns.barplot(x=timestamps, y=humidity, color="skyblue")
plt.title("Humidity Forecast")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

# Wind speed line plot
plt.subplot(3, 1, 3)
sns.lineplot(x=timestamps, y=wind_speeds, marker="x", color="green")
plt.title("Wind Speed Forecast")
plt.ylabel("Wind Speed (m/s)")
plt.xlabel("Date/Time")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
