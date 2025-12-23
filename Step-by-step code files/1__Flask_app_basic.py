#Importing flask:
from flask import Flask

#Setting-up our application:
##here 'app' is the IMP. flask object which:STORES routes,GET requests
##'__name__' is written to show that it is __main__ file
app = Flask(__name__)

#Create index route so that when search the URL don pop-up 404 (file not found):
## this decorator is telling "WHEN THE USER TYPE THIS URL , RUN THE FUNCTION BELOW"
## '/' is the ROOT URL (ie: http://127.0.0.1:5000"/" <-- this one )
## when URL hits "/" , below logic should execute
@app.route("/")

#Create our first VIEW or "ENDPOINT function":
def home():

#This is your HTTP response/that Chrome displays/that your server sends back:
## ITS IS NOT print(), its a RESPONSE PACKET send through HTTP
    return "Hello world"

#File guard to make sure "app is run from our main file":
if __name__=="__main__":

#Start the server/backend:
## 'debug' is only for dev purpose , not production.It will show errors(if exist) on your browser
## 'run' will open port 5000
    app.run(debug=True)
