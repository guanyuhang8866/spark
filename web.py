import time

import pymongo
from flask import Flask, request, render_template,session,redirect,url_for

app = Flask(__name__)
app.secret_key='\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'    #配置secret_key,否则不能实现session对话
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['test']

@app.route("/")
def index():
    if session.get('username')=='shiyanlou' and session.get('password')=='shiyanlou':
        return render_template("index.html")
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET',"POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == "POST":
        session['username'] = request.form['Name']
        session['password'] = request.form['Password']
        return redirect(url_for('index'))
@app.route('/save_to_mongo', methods = ["POST"])
def index2():
    s = request.form.get("s")
    mydb.orders.insert({"name":s,"createData":int(time.time()*1000)})
    return "Saved"

app.run(host='0.0.0.0', port=5004, debug=True, use_reloader=False)

