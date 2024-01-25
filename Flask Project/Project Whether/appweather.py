#f8c3fdde8d3e264a3094d170d698cea1
# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    data = get_weather_data(city_name)
    return render_template('weather.html', data=data)

def get_weather_data(city):
    api_key = 'f8c3fdde8d3e264a3094d170d698cea1'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return {
        'weather_main': data["weather"][0]["main"],
        'weather_description': data["weather"][0]["description"],
        'temperature': round(data["main"]["temp"] - 273.15, 2),
        'pressure': data["main"]["pressure"]
    }

if __name__ == '__main__':
    app.run(debug=True)
