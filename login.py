#!/usr/bin/python
#coding=utf-8

from flask import Flask,session,redirect,url_for,request

app=Flask(__name__)
app.secret_key='\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'    #配置secret_key,否则不能实现session对话
# or
# app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
# or
# app.config.update(SECRET_KEY='\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\')

@app.route("/")
def index():
    if session.get('username')=='shiyanlou' and session.get('password')=='shiyanlou':
        return "hello shiyanlou"
    return "you are not logged in"

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        session['password']=request.form['password']
        print ('>>>>>>>>>>>>>>>>>>>>>')
        print (session)
        return redirect(url_for('index'))
    return """
    <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=text name=password>
        <p><input type=submit value=Login>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port = 8017)