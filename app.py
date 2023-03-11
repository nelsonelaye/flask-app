# app
from flask import Flask

app = Flask(__name__)

# the main route app.route is linked to the index function
@app.route('/')
def index():
    return "Hello people!"

@app.route('/admin')
def admin():
    return "Hello admin!"