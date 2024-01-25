try:
    from flask import Flask, render_template, jsonify
    import requests
    print("All modules loaded")
except Exception as e:
    print("Error: {}".format(e))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    try:
        url = "https://demo-live-data.highcharts.com/aapl-ohlcv.json"
        response = requests.get(url)
        data = response.json()
        return jsonify({"res": data})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

