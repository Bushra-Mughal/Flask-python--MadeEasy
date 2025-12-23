#LESSON 5: FORMS + USER INPUT (GET & POST)
## This lesson is the foundation of: ◾Login systems◾Chatbots◾Search bars◾AI prompts◾Feedback systems
## we will create a "CHATBOT UI" to take user input and display it:

#Update your "index.html"
#Import "request" to read client data :
from flask import Flask,render_template,request
app=Flask(__name__)

#Update your home route:
## The route allows both HTTP methods so the "same URL" can accept either: a browser/URL request (GET) or a client sending "data" from frontend(POST).
## HTTP methods ---> verbs that tell the server what action to perform 
##      ie:  POST--> send data , GET--> fetch data 
@app.route("/", methods = ["GET","POST"])
def home():

#Create a variable to store what index.html posted
    message = None
#Check if HTTP method == POST:
    if request.method =='POST':
#Store whatever the 'user_message' of 'form' holds:
        message = request.form["user_message"].upper()
#Give dynamic data (data from python to HTML):
    return render_template("index.html", message = message)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/profile")
def profile():
    return render_template("profile.html",user_name="Bushra Mughal",skill="problem-solving")

app.run( debug=True )