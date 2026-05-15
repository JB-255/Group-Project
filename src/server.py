import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

#finds the txt file wherever it may be
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