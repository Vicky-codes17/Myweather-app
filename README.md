# 🌤️ ClimeCast - Modern Weather Forecast Application

<div align="center">

![ClimeCast Logo](assets/icon.png)

**A beautiful, cross-platform weather application with dark/light mode support**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey)](https://github.com/yourusername/climecast)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/climecast)

</div>

## 📖 **Table of Contents**

- [About ClimeCast](#about-climecast)
- [Features](#features)
- [Planned Features](#planned-features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Building the Application](#building-the-application)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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
├── 📁 src/                          # Source code
│   ├── 📄 main.py                   # Main application entry point
│   ├── 📄 version.py                # Version information
│   └── 📁 src/                      # Core modules
│       ├── 📄 __init__.py           # Package initialization
│       ├── 📄 uv_index.py          # UV index calculations
│       ├── 📄 temperature.py       # Temperature handling
│       ├── 📄 rainfall.py          # Rainfall predictions
│       ├── 📄 air_pressure.py      # Air pressure metrics
│       ├── 📄 wind.py              # Wind data processing
│       ├── 📄 sun_times.py         # Sunrise/sunset calculations
│       └── 📄 hourly_forecast.py   # Hourly forecast logic
├── 📁 assets/                       # Application assets
│   ├── 🖼️ icon.png                  # Application icon (PNG)
│   ├── 🖼️ icon.ico                  # Application icon (ICO)
│   ├── 🖼️ light.png                 # Light theme assets
│   └── 🖼️ dark.png                  # Dark theme assets
├── 📁 build/                        # UI build files
│   ├── 📁 assets/                   # Generated UI assets
│   ├── 📁 frame0/                   # Dark mode images
│   └── 📁 frame1/                   # Light mode images
├── 📁 releases/                     # Distribution packages
│   ├── 📁 v1.0.0/                  # Version 1.0.0
│   │   ├── 📁 linux/                # Linux distribution
│   │   └── 📁 windows/              # Windows distribution
│   └── 📁 latest/                   # Latest stable release
├── 📁 docs/                         # Documentation
│   ├── 📄 CONTRIBUTING.md           # Contribution guidelines
│   ├── 📄 CHANGELOG.md              # Version history
│   └── 📄 API.md                    # API documentation
├── 📁 tests/                        # Test suite
│   ├── 📄 test_main.py              # Main application tests
│   └── 📄 test_modules.py           # Module unit tests
├── 📄 README.md                     # This file
├── 📄 LICENSE                       # MIT License
├── 📄 requirement.txt               # Python dependencies
├── 📄 version.txt                   # Current version
├── 📄 .gitignore                    # Git ignore rules
└── 📄 build_climecast.sh            # Build script
```

## 🚀 **Getting Started**

### **Prerequisites**

- **Python 3.7 or higher**
- **Internet connection** (for weather data)
- **Linux with GUI** or **Windows 7+**

### **Quick Start**

#### **Option 1: Download Pre-built Application**
1. Go to [Releases](releases/latest/)
2. Download the appropriate version for your system:
   - **Linux**: `releases/latest/linux/ClimeCast`
   - **Windows**: `releases/latest/windows/ClimeCast.exe`
3. Run the application

#### **Option 2: Run from Source**
```bash
# Clone the repository
git clone https://github.com/yourusername/climecast.git
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
git clone https://github.com/yourusername/climecast.git
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

## 🏗️ **Building the Application**

### **For Linux**
```bash
# Make build script executable
chmod +x build_climecast.sh

# Build the application
./build_climecast.sh

# Find your executable in:
releases/v1.0.0/linux/ClimeCast
```

### **For Windows**
```cmd
REM Install dependencies
pip install pyinstaller requests

REM Build executable
cd src
pyinstaller --onefile --windowed --name="ClimeCast" main.py

REM Find your executable in:
src\dist\ClimeCast.exe
```

## 🤝 **Contributing**

We welcome contributions from the community! Here's how you can help:

### **How to Contribute**

1. **🍴 Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/climecast.git
   cd climecast
   ```

2. **🌿 Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b bugfix/fix-issue-123
   ```

3. **✨ Make Your Changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed
   - Add tests for new features

4. **🧪 Test Your Changes**
   ```bash
   # Run the application
   cd src && python3 main.py
   
   # Test different scenarios
   # - Light/dark mode switching
   # - Different weather conditions
   # - Various locations
   ```

5. **📝 Commit Your Changes**
   ```bash
   git add .
   git commit -m "✨ Add amazing new feature"
   
   # Use conventional commit messages:
   # ✨ feat: new feature
   # 🐛 fix: bug fix
   # 📚 docs: documentation
   # 🎨 style: formatting
   # ♻️ refactor: code refactoring
   # 🧪 test: adding tests
   ```

6. **🚀 Push to Your Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **📬 Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill out the PR template
   - Wait for review and feedback

### **What We're Looking For**

- 🐛 **Bug Fixes**: Help us squash bugs
- ✨ **New Features**: Implement features from our roadmap
- 📚 **Documentation**: Improve docs and comments
- 🧪 **Tests**: Add unit tests and integration tests
- 🎨 **UI/UX**: Improve the user interface
- 🌍 **Localization**: Add support for more languages

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

```
MIT License

Copyright (c) 2024 ClimeCast Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE