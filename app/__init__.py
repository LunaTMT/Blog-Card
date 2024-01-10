from flask import Flask
from dotenv import load_dotenv
import os
from livereload import Server

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set Flask configurations
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', False)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')

# Import and register routes from routes.py
from app import routes

if __name__ == '__main__':
    # Create an instance of the livereload server
    server = Server(app.wsgi_app)

    # Watch directories for changes and trigger browser refresh
    server.watch('app/templates/*.*')  # Monitor changes in template files
    server.watch('app/static/*.*')  # Monitor changes in static files

    # Start the server with livereload enabled
    server.serve(port=5000, host='127.0.0.1', debug=True)
