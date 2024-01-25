from flask import Flask, render_template
import pyjokes

app = Flask(__name__)

@app.route("/")
def home():
    joke = pyjokes.get_joke()
    return render_template('home.html', joke=joke)

@app.route("/MultipleJokes")
def jokes():
    jokes = pyjokes.get_jokes()
    return render_template('multiple_jokes.html', jokes=jokes)

if __name__ == "__main__":
    app.run(debug=True)
