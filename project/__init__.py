from flask import Flask
from project import views

def create_app():
    app = Flask(__name__)
    # Connects our views to the main instance of "app"
    app.register_blueprint(views.bp) 
    return app