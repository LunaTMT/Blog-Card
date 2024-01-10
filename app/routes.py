from flask import render_template
from app import app  # Import the Flask app instance

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
