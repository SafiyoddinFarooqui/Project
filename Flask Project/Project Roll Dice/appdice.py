from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

dice_image = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
]

@app.route("/")
def dice_game():
    return render_template("index.html", dice_image=url_for("static", filename=dice_image[0]))

@app.route("/roll", methods=["POST"])
def roll():
    random_num = random.randint(0, 5)
    return render_template("index.html", dice_image=url_for("static", filename=dice_image[random_num]))

if __name__ == '__main__':
    app.run(debug=True)
