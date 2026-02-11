# 🌤️ ClimeCast - Modern Weather Forecast Application

<div align="center">

![ClimeCast Logo](assets/icon.png)

**A beautiful, cross-platform weather application with dark/light mode support**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey)](https://github.com/yourusername/climecast)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/climecast)

</div>

## 🌟 **About ClimeCast**

ClimeCast is a modern, intuitive weather application built with Python and Tkinter. It provides real-time weather information with a beautiful user interface that adapts to both dark and light themes. Whether you're planning your day or checking the weekly forecast, ClimeCast delivers accurate weather data in an elegant, easy-to-use interface.

### **Why ClimeCast?**
- 🎨 **Beautiful UI**: Clean, modern interface with dark/light mode
- 🌍 **Global Coverage**: Weather data for locations worldwide
- 📱 **Lightweight**: Fast, responsive application
- 🔄 **Real-time Updates**: Live weather data from OpenWeatherMap
- 🚀 **Cross-platform**: Works on Linux and Windows

## ✨ **Features**

### **Current Features**
- 🌡️ **Real-time Weather Data**
  - Current temperature, humidity, and conditions
  - "Feels like" temperature
  - Weather descriptions and icons

- 📊 **7-Hour Forecast**
  - Hourly weather predictions
  - Temperature trends
  - Weather condition changes

- 🌓 **Dark/Light Mode Toggle**
  - Automatic theme switching
  - Eye-friendly interface
  - Persistent theme preference

- 📈 **Comprehensive Weather Metrics**
  - UV Index with safety recommendations
  - Atmospheric pressure
  - Wind speed and direction
  - Rainfall probability and intensity

- 🌅 **Solar Information**
  - Sunrise and sunset times
  - Visual timeline display
  - Daylight duration

- 🗺️ **Location Services**
  - City-based weather lookup
  - Geolocation support
  - Global city database

## 🚀 **Planned Features**

### **Version 1.1.0 (Q1 2025)**
- [ ] 📅 **Extended Forecast**
  - 7-day weather forecast
  - Weekly weather patterns
  - Historical weather data

- [ ] 🔔 **Weather Alerts**
  - Severe weather notifications
  - Custom alert thresholds
  - Push notification system

- [ ] 📍 **Enhanced Location**
  - GPS auto-detection
  - Multiple location favorites
  - Location-based recommendations

### **Version 1.2.0 (Q2 2025)**
- [ ] 📊 **Weather Analytics**
  - Weather trend graphs
  - Historical comparisons
  - Climate data visualization

- [ ] 🎯 **Personalization**
  - Customizable widgets
  - Personal weather preferences
  - Activity recommendations

- [ ] 🌐 **Advanced Features**
  - Weather radar maps
  - Satellite imagery
  - Air quality index

### **Version 2.0.0 (Q3 2025)**
- [ ] 📱 **Mobile Version**
  - Android app development
  - iOS app development
  - Cross-platform synchronization

- [ ] 🤖 **AI Integration**
  - Weather prediction ML models
  - Smart recommendations
  - Voice assistant integration

## 📸 **Screenshots**

| Light Mode | Dark Mode |
|------------|-----------|
| ![Light Mode](assets/screenshots/light-mode.png) | ![Dark Mode](assets/screenshots/dark-mode.png) |

## 🏗️ **Project Structure**

```
climecast/
├──  src/                   
│   ├──  main.py             
│   ├──  version.py          
│   └──  src/              
│       ├──  __init__.py     
│       ├──  uv_index.py       
│       ├──  temperature.py       
│       ├──  rainfall.py      
│       ├──  air_pressure.py   
│       ├──  wind.py         
│       ├──  sun_times.py  
│       └──  hourly_forecast.py 
├──  assets/            
│   ├──  icon.png          
│   ├──  icon.ico                
│   ├──  light.png               
│   └──  dark.png                  
├──  build/                
│   ├──  assets/           
│   ├──  frame0/       
│   └──  frame1/           
├──  releases/              
│   ├──  v1.0.0/         
│   │   ├──  linux/           
│   │   └──  windows/             
│   └──  latest/            
├──  docs/                   
│   ├──  CONTRIBUTING.md         
│   ├──  CHANGELOG.md         
│   └──  API.md         
├──  tests/                
│   ├──  test_main.py      
│   └──  test_modules.py  
├──  README.md                    
├──  LICENSE                     
├──  requirement.txt         
├──  version.txt          
├──  .gitignore              
└──  build_climecast.sh     
```

## 🚀 **Getting Started**

### **Prerequisites**

- **Python 3.7 or higher**
- **Internet connection** (for weather data)
- **Linux with GUI** or **Windows 7+**

### **Quick Start**

#### **Option 1: Download Pre-built Application**
1. Go to Releases
2. Download the appropriate version for your system:
   - **Linux**: `releases/latest/linux/ClimeCast`
   - **Windows**: `releases/latest/windows/ClimeCast.exe`
3. Run the application

#### **Option 2: Run from Source**
```bash
# Clone the repository
git clone https://github.com/Vicky-Codes17/Myweather-app.git
cd climecast

# Install dependencies
pip3 install -r requirement.txt

# Run the application
cd src
python3 main.py
```

## 💻 **Development Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/Vicky-Codes17/Myweather-app.git
cd climecast
```

### **2. Set Up Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
# Install all required packages
pip install -r requirement.txt

# Or install individually:
pip install geopy timezonefinder pytz requests pyinstaller
```

### **4. Configure API Keys**
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the API key in [`src/main.py`](src/main.py)

### **5. Run Development Version**
```bash
cd src
python3 main.py
```

## 🤝 **Contributing**

We welcome contributions from the community! Here's how you can help:

### **How to Contribute**

1. **🍴 Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/Vicky-Codes17/Myweather-app.git
   cd climecast
   ```

2. **🌿 Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b bugfix/fix-issue-123
   ```
For more in detail [Contributing.md](CONTRIBUTING.md) file for details,...

### **Development Guidelines**

- **Code Style**: Follow PEP 8 Python style guidelines
- **Documentation**: Add docstrings to all functions and classes
- **Testing**: Include tests for new functionality
- **Commits**: Use clear, descriptive commit messages
- **Issues**: Link PRs to related issues

### **Reporting Issues**

Found a bug? Have a feature request? Please open an issue with:
- **Clear description** of the problem/feature
- **Steps to reproduce** (for bugs)
- **Expected behavior**
- **Screenshots** (if applicable)
- **System information** (OS, Python version)

## 📄 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
