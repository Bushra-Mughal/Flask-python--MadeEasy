from flask import Flask

app = Flask(__name__)

# 'Home page' route:
## route is a "path" of the URL
@app.route("/")
def home_fun():
    return"This is my home page"

#Add 'about' page's route:
## when URL hits "/about" , below logic should execute as "it's the route for this page"
## these function are also called "CONTROLLER FUNCTION"
## copy: http://127.0.0.1:5000/about and run it on browser
@app.route("/about")
def about_fun():
    return " 'ABOUT' route called.Opening About page"

#Add contact page's route:
## copy: http://127.0.0.1:5000/contact to your browser
@app.route("/contact")
def contact_fun():
    return """This is my "contact" page"""

@app.route("/profile")
def profile_fun():
    return "I am profile page🙂😁 "
    
app.run( debug=True )