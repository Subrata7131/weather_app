# 🌦️ Weather App CLI

A **command-line weather and air quality application** built in Python 🐍 using [WeatherAPI](https://www.weatherapi.com/).  
It fetches **real-time weather conditions, air quality data, and environmental metrics** for any location you enter.  

With optional **Rich** integration, results are displayed in a **colorful table** for a better CLI experience.  

---

## ✨ Features

- 🌍 Real-time weather by city or location name  
- 🌡️ Temperature in °C / °F with “feels like” values  
- 💨 Wind speed (kph & mph) with directional arrows and gusts  
- 💧 Humidity, pressure, precipitation, UV index, and visibility  
- 🏭 Air Quality Index (EPA) with pollutant breakdown (PM2.5, PM10, CO, NO₂, SO₂, O₃)  
- 🌈 Weather condition icons (☀️, ☁️, 🌧️, ❄️, etc.)  
- 🎨 Pretty tables with [Rich](https://github.com/Textualize/rich) (optional)  

---

## 🚀 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/weather-cli.git
   cd weather-cli
   ```

2. **Create and activate a virtual environment** (recommended)  
   - **Windows (PowerShell)**  
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux**  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your WeatherAPI key**  
   Create a `.env` file in the project root:  
   ```env
   API_KEY=your_api_key_here
   ```

---

## 🛠️ Usage

Run the app:  
```bash
python main.py
```

Example interaction:  
```
Enter location (or 'q' to quit): London
```

Output (with Rich installed):  

```
┌───────────────┬───────────────────────────────┐
│ Location      │ London, City of London, UK    │
│ Local Time    │ 2025-10-02 12:00              │
│ Condition     │ ☁️  Partly Cloudy             │
│ Temperature   │ 18.0 °C / 64.4 °F             │
│ Feels Like    │ 17.5 °C / 63.5 °F             │
│ Humidity      │ 70%                           │
│ Wind          │ 12.0 kph (7.5 mph) ↑          │
│ Gust          │ 20.0 kph (12.4 mph)           │
│ Pressure      │ 1015 mb                       │
│ Precipitation │ 0.0 mm                        │
│ UV Index      │ 3                             │
│ Visibility    │ 10 km                         │
│ AQI (EPA)     │ 2 (Fair)                      │
│ PM2.5         │ 12.3 µg/m³                    │
│ PM10          │ 20.1 µg/m³                    │
│ CO            │ 0.4 µg/m³                     │
│ NO₂           │ 5.2 µg/m³                     │
│ SO₂           │ 1.1 µg/m³                     │
│ O₃            │ 30.5 µg/m³                    │
└───────────────┴───────────────────────────────┘
```

---

## 📦 Dependencies

- [requests](https://pypi.org/project/requests/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  
- [rich](https://pypi.org/project/rich/) *(optional, for colorful tables)*  

Install them all with:  
```bash
pip install -r requirements.txt
```

---

## 📸 Demo

![Weather CLI Demo](https://via.placeholder.com/800x400.png?text=Weather+CLI+Demo)

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## 🤝 Contributing

Pull requests are welcome! Open an issue for suggestions or bug reports 🐛.  

---

## 💡 Author

Made with 💖 by **SUBRATA PAL**  

---


