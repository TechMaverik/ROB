from flask import Flask, render_template, request
from handlers import Handlers
from Firmware import prepositions
import json


app = Flask(__name__)


@app.route("/about")
def version():
    return {"device": "Rob Studio", "version": "1.0.0", "status": "active"}


@app.route("/")
def home():
    return render_template("home.html", feedback=prepositions.HOME_POS)


@app.route("/devices")
def devices():
    return render_template("devices.html")


@app.route("/record-play")
def record_play():
    return render_template("recordplay.html")


@app.route("/move-to-position", methods=["POST", "GET"])
def robot_position():
    if request.method == "POST":
        if request.form["action"] == "move":
            feedback = Handlers().robot_position()
            return render_template("home.html", feedback=feedback["received"])
        elif request.form["action"] == "home":
            payload = prepositions.HOME_POS
            feedback = Handlers().robot_home_position(payload)
            return render_template("home.html", feedback=feedback["received"])


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        # Handle settings form submission here
        pass
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2025, debug=True)
