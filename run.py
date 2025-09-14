from flask import Flask, render_template, request
from handlers import Handlers


app = Flask(__name__)


@app.route("/about")
def version():
    return {"device": "Rob Studio", "version": "1.0.0", "status": "active"}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/devices")
def devices():
    return render_template("devices.html")


@app.route("/record-play")
def record_play():
    return render_template("recordplay.html")


@app.route("/move-to-position", methods=["POST", "GET"])
def robot_position():
    if request.method == "POST":
        response = Handlers().robot_position()
        return render_template("home.html", response=response)


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        # Handle settings form submission here
        pass
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
