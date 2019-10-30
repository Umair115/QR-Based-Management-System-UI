from flask import Flask, render_template,request
import pyrebase
app = Flask(__name__)
import pyqrcode  as qr
import png 


config = {
    "apiKey": "AIzaSyC8JGX3tvNDH9pkTVQiXHhcXB35xIV29tk",
    "authDomain": "superman-a1a14.firebaseapp.com",
    "databaseURL": "https://superman-a1a14.firebaseio.com",
    "projectId": "superman-a1a14",
    "storageBucket": "superman-a1a14.appspot.com",
    "messagingSenderId": "954864727176",
    "appId": "1:954864727176:web:63e981126c974f76995b3d"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

@app.route("/", methods=['GET', 'POST'])
def signin():
    unsuccessful = 'Please check your credentials'
    successful = "Login Successful"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('index.html', s=successful)
        except:
            return render_template('signin.html', us=unsuccessful)
    return render_template('signin.html')





    
            


@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/team.html")
def doctors():
    return render_template("team.html")

@app.route("/records.html")
def view_records():
    return render_template("records.html")

@app.route("/emergency.html")
def emergency():
    return render_template("emergency.html")

@app.route("/opd.html")
def opd():
    return render_template("opd.html")

@app.route("/ipd.html", methods = ["GET","POST"])
def ipd():
    if (request.method == "POST"):
        
        cnic = request.form.get("CNIC")
        dataqr = qr.create(cnic)
        dataqr.png("Patient1.png", scale = 15)
        data = {
        "name" : request.form.get("Name"),
        "phone" : request.form.get("Phone"),
        "room" : request.form.get("Rooms"),
        "date" : request.form.get("Date"),
        "doctor" : request.form.get("Doctor"),
        "disorder" : request.form.get("any_disorder")

        }

        db.child(cnic).set(data)
        
    return render_template("ipd.html")

app.run(debug=True)




