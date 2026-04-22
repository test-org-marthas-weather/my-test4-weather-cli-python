#!/usr/bin/env python3
"""
Weather CLI Tool
A simple command-line interface for fetching current weather information.
"""

import argparse
import sys
import requests


def get_weather(city, api_key=None):
    """
    Fetch weather data for a given city.
    
    Args:
        city (str): Name of the city to fetch weather for
        api_key (str): API key for the weather service (optional for now)
    
    Returns:
        dict: Weather data or None if request fails
    """
    # TODO: Implement actual API call to weather service
    # For now, this is a placeholder structure
    
    if not api_key:
        print("⚠️  Warning: No API key provided. Please configure your weather API key.")
        print("   Sign up at: https://openweathermap.org/api")
        return None
    
    # Example API endpoint (OpenWeatherMap format)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }
    
    try:
        # Make GET request to weather API
        response = requests.get(base_url, params=params)
        
        # Check if request was successful
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print(f"❌ Error: API request failed with status code {response.status_code}")
            if response.status_code == 401:
                print("   Invalid API key. Please check your credentials.")
            elif response.status_code == 404:
                print(f"   City '{city}' not found.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print("❌ Error: Invalid JSON response from API")
        return None


def display_weather(weather_data):
    """
    Display weather information in a user-friendly format.
    
    Args:
        weather_data (dict): Weather data from API
    """
    if not weather_data:
        return
    
    try:
        city = weather_data.get("name", "Unknown")
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"].capitalize()
        
        print("\n" + "="*50)
        print(f"🌤️  Weather in {city}")
        print("="*50)
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Conditions: {description}")
        print(f"Humidity: {humidity}%")
        print("="*50 + "\n")
        
    except KeyError as e:
        print(f"❌ Error parsing weather data: Missing key {e}")


def main():
    """
    Main entry point for the CLI application.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Fetch current weather information for a city",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --city London
  python main.py --city "New York" --api-key YOUR_API_KEY
  
Get your free API key at: https://openweathermap.org/api
        """
    )
    
    parser.add_argument(
        "--city",
        type=str,
        required=True,
        help="Name of the city to fetch weather for"
    )
    
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="API key for OpenWeatherMap (or set WEATHER_API_KEY environment variable)"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Fetch and display weather
    print(f"🔍 Fetching weather for {args.city}...")
    weather_data = get_weather(args.city, args.api_key)
    
    if weather_data:
        display_weather(weather_data)
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
