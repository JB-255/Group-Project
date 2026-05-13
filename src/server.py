import os
from flask import Flask, render_template, request

app = Flask(__name__)

#finds file 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_FILE = os.path.join(BASE_DIR, "loginInfo.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    login_uname = data["uname"]
    login_pword = data["pword"]
    login_successful = False
    try:
        f = open(LOGIN_FILE, "r")
    except:
        print("File not found")
        return "Fail"
    for l in f:
        #check file
        l = l.strip()
        splitted = l.split(",")
        if (splitted[0] == login_uname) and (splitted[1] == login_pword):
            login_successful = True 
            break
    f.close()
    if login_successful:
        return "Yay"
    else:
        return "Nay"
    
@app.route("/register", methods=["POST"])
def register():
    repeat = False
    info = request.get_json()
    reg_uname = info["uname"]
    reg_pword = info["pword"]
    string = reg_uname + "," + reg_pword + "\n"
    try:
        f = open(LOGIN_FILE, "r")
        #check no repeated username
        for l in f:
            l = l.strip()
            splitted = l.split(",")
            if splitted[0] == reg_uname:
                repeat = True
        f.close()
        if repeat:
            return "Un"
        else:
            try:
                f = open(LOGIN_FILE, "a")
                f.write(string)
                f.close()
            except:
                return "Nay"
        return "Yay"
    except:
        return "Nay"

if __name__ == "__main__":
    app.run(debug=True)