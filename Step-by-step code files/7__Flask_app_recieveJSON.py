from flask import Flask,render_template,jsonify,request
app=Flask(__name__)

#Create "chat.html" in "templates"

@app.route("/")
def home():
    return "I am home page"

#Create "/api/show_prompt" API route and allow HTTP "POST methods" to recieve client JSON data:
@app.route("/api/show_prompt",methods=["POST"])
def show_prompt():

#Get & store "JSON data" which is "posted" by HTML
    data = request.get_json()

#Store "message" in JSON data:
    user_msg = data.get("message","")

#HHTP  that JSON message :
    return jsonify({
        "reply": f"You said: {user_msg}"
    })

#Create a new route/endpoint:
## Run this URL: "http://127.0.0.1:5000/chat"
@app.route("/chat")
def chat():
    return render_template("chat.html")

app.run(debug=True)