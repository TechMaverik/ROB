from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route('/about')
def version():
    return {"device":"Rob Studio","version":"1.0.0","status":"active"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/configurations')
def configurations():
    return render_template('configurations.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)