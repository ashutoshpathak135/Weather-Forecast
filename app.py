from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    city = request.form.get("city")

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            return "City not found"

        data = response.json()

        temperature = round(data["main"]["temp"], 1)
        weather = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return render_template(
            "index.html",
            city=city,
            temperature=temperature,
            weather=weather,
            icon=icon,
            humidity=humidity,
            wind_speed=wind_speed
        )

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)