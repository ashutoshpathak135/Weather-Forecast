# Weather Forecast

A simple Weather Forecast web application built using Python and Flask.

## Features

- Search weather by city name
- Display current temperature
- Display weather condition
- Display humidity
- Display wind speed
- Display dynamic weather icon
- Handles invalid city names

## Technologies Used

- Python
- Flask
- HTML
- CSS
- OpenWeatherMap API

## Project Structure

```text
Weather-Forecast/
├── app.py
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
## How to Run

1. Install the required Python packages.
2. Create a `.env` file and add your OpenWeatherMap API key:

WEATHER_API_KEY=your_api_key_here

3. Run the application:

python app.py

4. Open the application in your browser:

http://127.0.0.1:5000

## Note

The `.env` file contains the API key and should not be uploaded to GitHub.
