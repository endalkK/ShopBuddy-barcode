from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message)