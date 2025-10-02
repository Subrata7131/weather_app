import os
import sys
from dotenv import load_dotenv
from requests import get, RequestException

# Try to import rich for pretty tables; fallback if not installed
try:
    from rich.console import Console
    from rich.table import Table

    console = Console()
    USE_RICH = True
except ImportError:
    USE_RICH = False

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Error: API_KEY not set in environment.")
    sys.exit(1)

API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather_data(location: str) -> dict:
    params = {"key": API_KEY, "q": location, "aqi": "yes"}
    try:
        resp = get(API_URL, params=params, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"Network/API error: {e}")
        sys.exit(1)


def weather_icon(cond_text: str) -> str:
    t = cond_text.lower()
    if "clear" in t or "sun" in t:
        return "☀️"
    if "cloud" in t:
        return "☁️"
    if "rain" in t or "drizzle" in t:
        return "🌧️"
    if "thunder" in t:
        return "⛈️"
    if "snow" in t:
        return "❄️"
    if "mist" in t or "fog" in t:
        return "🌫️"
    return "🌈"  # default fallback icon


def wind_arrow(direction: str) -> str:
    arrows = {"N": "↑", "S": "↓", "E": "→", "W": "←"}
    return "".join(arrows.get(c, "") for c in direction.upper())


from typing import Tuple


def format_air_quality(aq: dict) -> Tuple[int, str]:
    idx = int(aq.get("us-epa-index", 0))
    labels = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor",
        6: "Hazardous",
    }
    return idx, labels.get(idx, "Unknown")


def display(data: dict):
    loc = data["location"]
    cur = data["current"]
    aqi = cur["air_quality"]
    epa_idx, epa_label = format_air_quality(aqi)

    # Prepare metrics
    metrics = {
        "Location": f"{loc['name']}, {loc['region']}, {loc['country']}",
        "Local Time": loc["localtime"],
        "Condition": f"{weather_icon(cur['condition']['text'])}  {cur['condition']['text']}",
        "Temperature": f"{cur['temp_c']} °C  /  {cur['temp_f']} °F",
        "Feels Like": f"{cur['feelslike_c']} °C  /  {cur['feelslike_f']} °F",
        "Humidity": f"{cur['humidity']}%",
        "Wind": f"{cur['wind_kph']} kph ({cur['wind_mph']} mph) {wind_arrow(cur['wind_dir'])}",
        "Gust": f"{cur['gust_kph']} kph ({cur['gust_mph']} mph)",
        "Pressure": f"{cur['pressure_mb']} mb",
        "Precipitation": f"{cur['precip_mm']} mm",
        "UV Index": f"{cur['uv']}",
        "Visibility": f"{cur['vis_km']} km",
        "AQI (EPA)": f"{epa_idx}  ({epa_label})",
        "PM2.5": f"{aqi['pm2_5']:.1f} µg/m³",
        "PM10": f"{aqi['pm10']:.1f} µg/m³",
        "CO": f"{aqi['co']:.1f} µg/m³",
        "NO₂": f"{aqi['no2']:.1f} µg/m³",
        "SO₂": f"{aqi['so2']:.1f} µg/m³",
        "O₃": f"{aqi['o3']:.1f} µg/m³",
    }

    if USE_RICH:
        table = Table(show_header=False, box="SIMPLE")
        for key, val in metrics.items():
            table.add_row(key, val)
        console.print(table)
    else:
        print("-" * 40)
        for key, val in metrics.items():
            print(f"{key:<15}: {val}")
        print("-" * 40)


def main():
    while True:
        loc = input("Enter location (or 'q' to quit): ").strip()
        if loc.lower() == "q":
            break
        data = get_weather_data(loc)
        display(data)


if __name__ == "__main__":
    main()

