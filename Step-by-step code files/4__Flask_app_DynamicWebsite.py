## A "dynamic website" takes data from backend(PYTHON) and pass it to Frontend(HTML)

#Update your "index.html"
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/profile")
def profile():
#Update your "profile page" logic:
    return render_template(
        "profile.html",
#Give dynamic data (data from python to HTML):
        user_name = "Bushra Mughal",
        skill = "problem-solving"
                           )

app.run( debug=True )
