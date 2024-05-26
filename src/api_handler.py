import requests

# Example function to fetch weather data from OpenWeatherMap API
def get_weather(city_name, api_key):
    """
    Fetch the weather data for a given city.

    Args:
        city_name (str): The name of the city to get weather for.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: The weather data for the city, or None if the request fails.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
