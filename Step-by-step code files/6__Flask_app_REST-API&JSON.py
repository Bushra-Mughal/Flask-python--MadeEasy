#lesson 6: REST API and JSON
## This will directly help you build: 💠AI chatbot 💠AI tools 💠dashboards 💠mobile apps.
## REST APIs are those who: POST/GET JSON data using URLs
## API don use HTML,they return JSON data

#Add "jsonify" to "return JSON data" (otherwise dictionary is returned):
from flask import Flask,render_template, jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return "\tThis is 'Flask REST API' program"
@app.route("/about")
def about():
    return render_template("about.html")

#Create your Flask REST API endpoint/route:
## Run: http://127.0.0.1:5000/api/return:
@app.route("/api/return")
def api_return():
    return jsonify({
        "status": "Hello I am active!",
        "version": "1.0",
        "author": "Bushra Mughal"
        })

app.run( debug=True)