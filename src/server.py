import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

#finds file 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_FILE = os.path.join(BASE_DIR, "loginInfo.txt")

current_items = [
    {
        "id": 1,
        "photo": "/static/products/cars/product1.jpg",
        "name": "Jaguar XE",
        "price": 10000,
        "description": "For sale, in good condition with full service history",
    },
    {
        "id": 2,
        "photo": "/static/products/cars/product2.jpg",
        "name": "McLaren Senna",
        "price": 3000000,
        "description": "McLaren Senna for sale, full service history 2,000 miles",
    },
    {
        "id": 3,
        "photo": "/static/products/cars/product3.jpg",
        "name": "Audi TT RS",
        "price": 20000,
        "description": "Audi TT newer model for sale, partial service history 50,000 miles 1 Owner",
    },
    {
        "id": 4,
        "photo": "/static/products/cars/product4.jpg",
        "name": "Porsche Cayman",
        "price": 30000,
        "description": "Ex Dealership car, low miles 1 owner",
    },
    {
        "id": 5,
        "photo": "/static/products/technology/product1.jpg",
        "name": "Google Pixel 6a",
        "price": 299.99,
        "description": "For sale, brand new, open box never used",
    },
    {
        "id": 6,
        "photo": "/static/products/technology/product2.jpg",
        "name": "Meta Quest 3",
        "price": 395,
        "description": "Meta Quest 3 for sale used lighly only for a few hours",
    },
    {
        "id": 7,
        "photo": "/static/products/technology/product3.jpg",
        "name": "Focusrite Scarlett Solo",
        "price": 85,
        "description": "4th Generation Focusrite Scarlett Solo good condition used for a few months ",
    },
    {
        "id": 8,
        "photo": "/static/products/technology/product4.jpg",
        "name": "Intel i9 13900KF",
        "price": 300,
        "description": "Used Intel I9 13th Generation processor, works perfectly 24 cores 32 threads",
    }
]

current_items = {str(v["id"]): v for v in current_items}

#runs in browser
@app.route("/")
def home():
    return render_template("index.html", items=current_items.values())

@app.route("/buy/<id>")
def buy(id):
    item = current_items.get(id)

    if item is None:
        return redirect("/")

    return render_template("buy.html", item=item)

@app.route("/do-buy/<id>", methods=["POST"])
def do_buy(id):
    if id in current_items:
        del current_items[id]
        return "Success"

    else:
        return "Fail"

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