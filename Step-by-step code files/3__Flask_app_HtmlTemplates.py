from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
#CONNECT your route to "HTML templates" using "render_template()":
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__=="__main__":
    app.run( debug=True )

## Congrats!🚀 This is your "full-stack" development: Backend(python)+Frontend(HTML) using Flask !