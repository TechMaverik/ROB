from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/about')
def version():
    return {"device":"Rob Studio","version":"1.0.0","status":"active"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/devices')
def devices():
    return render_template('devices.html')

@app.route('/record-play')
def record_play():
    return render_template('recordplay.html')

@app.route('/move-to-position', methods=['POST','GET'])
def move_to_position():
    if request.method == 'POST':
        base = request.form.get('slider1')
        shoulder = request.form.get('slider2')
        elbow = request.form.get('slider3')
        wrist_pitch = request.form.get('slider4')
        wrist_roll = request.form.get('slider5')
        gripper = request.form.get('slider6')
        payload = {
            "base": base,
            "shoulder": shoulder,
            "elbow": elbow,
            "wrist": wrist_pitch,
            "end_effector": wrist_roll,
            "pick": gripper 
        } 
        external_url = "http://10.120.3.169/rob/move/"
        response = requests.post(external_url, json=payload)

        return render_template('home.html', response=response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)