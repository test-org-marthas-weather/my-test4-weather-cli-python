# Weather CLI Tool 🌤️

A simple Python command-line interface (CLI) tool that fetches the current weather for a given city.

## Overview

This project provides an easy-to-use CLI tool for checking weather conditions in any city around the world. Built with Python and leveraging the popular `requests` library for HTTP API calls.

## Features

- 🌍 Fetch current weather for any city
- 📊 Display temperature, conditions, and other weather metrics
- 🖥️ Simple command-line interface
- ⚡ Fast and lightweight

## Prerequisites

- Python 3.7 or higher
- `requests` library
- A weather API key (e.g., from [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/test-org-marthas-weather/my-test4-weather-cli-python.git
cd my-test4-weather-cli-python
```

2. Install required dependencies:
```bash
pip install requests
```

3. Set up your API key:
   - Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
   - Create a `.env` file or configure your API key as needed

## Usage

```bash
python main.py --city "London"
```

Example output:
```
Weather in London:
Temperature: 15°C
Conditions: Partly Cloudy
Humidity: 65%
```

## Project Structure

```
my-test4-weather-cli-python/
├── .gitignore
├── README.md
├── main.py              # Main CLI application
├── docs/
│   └── reference_guide.md  # API documentation reference
└── requirements.txt     # Python dependencies (to be added)
```

## Documentation

For detailed information about the `requests` library used in this project, see [docs/reference_guide.md](docs/reference_guide.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Roadmap

See the [Issues](https://github.com/test-org-marthas-weather/my-test4-weather-cli-python/issues) section for planned features and improvements.

---

Built with ❤️ using Python and the Requests library
