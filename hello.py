$ pip install Flask
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/

 from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"