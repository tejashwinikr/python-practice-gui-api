from GUI.gui import create_window
from GUI.anime import anime_window
from APIS.api_handler import get_weather

def main():
    print("Hello, project is running!buddy")

    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    #print(os.path.join(os.path.dirname(__file__), '..', 'png-icons'))
    #C:\Users\ahwin\Python projects\my_python_demo\src\..\png-icons

# C:\Users\ahwin\Python projects\my_python_demo\src
    #api call
    # api_key = 'your_api_key'
    # city_name = 'London'
    # weather_data = get_weather(city_name, api_key)

    # if weather_data:
    #     print(f"Weather in {city_name}:")
    #     print(f"Temperature: {weather_data['main']['temp']}°C")
    #     print(f"Weather: {weather_data['weather'][0]['description']}")
    # else:
    #     print("Failed to retrieve weather data")

    create_window()
    # anime_window()

if __name__ == "__main__":
    main()




# import os

# def main():
#     print("Hello, project is running!123")
#     #print(os.path.join(os.path.dirname(__file__), '..', 'png-icons'))

# # C:\Users\ahwin\Python projects\my_python_demo\src
#     create_window()

# if __name__ == "__main__":
#     main()
