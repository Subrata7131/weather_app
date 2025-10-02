# 🌦️ Weather App CLI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Made with](https://img.shields.io/badge/Made%20with-💖-ff69b4.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)  

A simple **command-line weather application** 🌍 built using **Python** 🐍 and the [WeatherAPI](https://www.weatherapi.com/).  
It fetches and displays the current weather 🌦️, temperature 🌡️, wind 💨, and humidity 💧 for any location entered by the user.

---

## ✨ Features
- 🌍 Get real-time weather info by location name.  
- 🌡️ Shows temperature in Celsius along with "feels like".  
- 💨 Displays wind speed in km/h.  
- 💧 Shows humidity percentage.  
- 📝 Weather condition description.  

---

## 🚀 Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weather-cli.git
   cd weather-cli
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate     # Mac/Linux
   .\venv\Scripts\Activate.ps1  # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your **WeatherAPI key**:

   ```env
   API_KEY=your_api_key_here
   ```

---

## 🛠️ Usage

Run the app:

```bash
python main.py
```

Enter a city name when prompted:

```
Enter Location: London
Weather of London, City of London
--------------------------------------------
Temp: 18.0 °C  | Feels: 17.5 °C |
Wind: 12.0 km/h |
Humidity: 70%  | Description: Partly cloudy
```

Type `q` to exit ❌.

---

## 📦 Dependencies

* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [requests](https://pypi.org/project/requests/)

Install with:

```bash
pip install -r requirements.txt
```

---

## 📸 Example

![Weather CLI Demo](https://img.shields.io/badge/Demo-CLI-lightblue?style=for-the-badge)

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to **open an issue** for suggestions or bugs 🐛.

---

## 💡 Author

Made with 💖 by [Your Name](https://github.com/your-username)

```

👉 You just need to:  
1. Save this as `README.md`.  
2. Create a `requirements.txt` with:  
```

requests
python-dotenv


