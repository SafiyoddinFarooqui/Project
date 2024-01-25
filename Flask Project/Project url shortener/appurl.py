from flask import Flask, render_template, request, jsonify
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('shortner.html')

@app.route('/convert', methods=['POST'])
def convert():
    long_url = request.form['long_url']
    short_url = shorten_url(long_url)
    return jsonify({'short_url': short_url})

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

if __name__ == '__main__':
    app.run(debug=True)
