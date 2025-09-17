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
    records=Handlers().read_robot_position_records()
    return render_template("recordplay.html",records=records)

@app.route("/memorized-movements",methods=["POST", "GET"])
def record_play_repeat():    
    records=Handlers().read_robot_position_records()
    if request.method == "POST":
        if request.form["action"] == "play": 
            Handlers().play_recorded()           
            return render_template("recordplay.html",records=records)
        elif request.form["action"] == "repeat":           
            return render_template("recordplay.html",records=records)
        elif request.form["action"] == "clear":   
            Handlers().robot_position_clear()        
            return render_template("recordplay.html",records=records)
    
@app.route("/move-to-position", methods=["POST", "GET"])
def robot_position():
    if request.method == "POST":
        if request.form["action"] == "move":
            feedback = Handlers().robot_position()
            return render_template("home.html", feedback=feedback["received"])
        elif request.form["action"] == "home":
            payload = prepositions.HOME_POS
            feedback = Handlers().robot_position_payload(payload)
            return render_template("home.html", feedback=feedback["received"])
        elif request.form["action"] == "test":
            payload = prepositions.TEST_BASE_MIN
            feedback = Handlers().robot_position_payload(payload)
            payload = prepositions.TEST_BASE_MAX
            feedback = Handlers().robot_position_payload(payload)
            payload = prepositions.HOME_POS
            feedback = Handlers().robot_position_payload(payload)
            return render_template("home.html", feedback=feedback["received"])
        elif request.form["action"] == "record":
            savedposition = Handlers().robot_position_storage()
            print(savedposition)
            return render_template("home.html", feedback=savedposition)
        elif request.form["action"] == "clear":
            Handlers().robot_position_clear()                      
            return render_template("home.html", feedback=prepositions.HOME_POS)


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        # Handle settings form submission here
        pass
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2025, debug=True)
