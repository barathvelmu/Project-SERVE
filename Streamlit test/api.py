from flask import Flask
from flask_cors import CORS
from flask import request
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return """You aren't supposed to be here.
    
    
    Leave."""

@app.route('/test', methods = ['GET', 'POST'])
def test():
    con = sqlite3.connect("SERVE.db")
    res = con.execute("SELECT Faculty, count(*) from S24_Members group by Faculty")
    results = {}
    for row in res:
        results[row[0]] = [row[1]]
    return results