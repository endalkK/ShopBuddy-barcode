from flask import Flask, render_template, request 
 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 
 
@app.route('/process_data', methods=['POST']) 
def process_data(): 
    # call your Python function here 
    
    return 'Success'