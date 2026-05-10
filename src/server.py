import os
from flask import Flask, request, render_template

app = Flask(__name__)

#finds the txt file wherever it may be
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_FILE = os.path.join(BASE_DIR, "loginInfo.txt")

#runs in browser
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    #gets the username and pword from the js
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    login_successful = False
    f = open(LOGIN_FILE, "r")
    for line in f:
        #reads line of file and turns to list
        line = line.strip()
        splitted = line.split(",")
        #sees if the inputted data matches with the file
        if (splitted[0] == username) and (splitted[1] == password):
            login_successful = True 
            break
    f.close()
    #returns result to js
    if login_successful:
        return "Success"
    else:
        return "Fail"
    
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    #turns data into a string and writes to file
    string = username + "," + password + "\n"
    f = open(LOGIN_FILE, "a")
    f.write(string)
    f.close()
    return "Registered"

#starts code when file ran
if __name__ == "__main__":
    app.run(debug=True)