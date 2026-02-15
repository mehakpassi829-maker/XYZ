from flask import Flask , render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import pyrebase





# app.register_blueprint(email_bp)






app = Flask(__name__, template_folder="frontend/html", static_folder="frontend")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


CORS(app)

firebase_config = {
    "apiKey": os.getenv("firebase_apiKey"),
    "authDomain": os.getenv("firebase_authDomain"),
    "projectId": os.getenv("firebase_projectId"),
    "storageBucket": os.getenv("firebase_storageBucket"),
    "messagingSenderId": os.getenv("firebase_messagingSenderId"),
    "appId": os.getenv("firebase_appId"),
    "measurementId": os.getenv("firebase_measurementId"),
    "databaseURL": os.getenv("firebase_db_URL")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()



@app.route("/")
def home():
    
    modules = [
        {"title": "Budget Basics", "desc": "Learn how to manage money", "icon": "💰"},
        {"title": "Saving Skills", "desc": "Build strong saving habit", "icon": "📈"},
        {"title": "Banking Basics", "desc": "Understand bank & UPI", "icon": "🏦"},
        {"title": "Investment", "desc": "Grow your money smartly", "icon": "📊"},
        {"title": "Crypto Intro", "desc": "Learn blockchain basics", "icon": "🪙"},
        {"title": "AI Finance", "desc": "Use AI for saving", "icon": "🤖"},
    ]

    return render_template("index.html", name="Flask" , modules=modules)


@app.route("/auth")
def auth_page():
    return render_template("auth.html", name="Flask")

@app.route("/signup", methods=["POST"])
def signup():
    print("Headers:", request.headers)
    print("Body:", request.data)
    data = request.get_json()
    print("Parsed JSON:", data)

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    email = data.get("email")
    password = data.get("password")
    try:
        # user = auth.create_user_with_email_and_password(email, password)
        user = auth.create_user_with_email_and_password(email, password)
        
        return jsonify({"message": "User created", "uid": user['localId']})
    except Exception as e:
        print("🔥 Firebase FULL error:", e) 
        return jsonify({"error": str(e)}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return jsonify({
            "message": "Login successful",
            "idToken": user['idToken'],
            "refreshToken": user['refreshToken']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True)


