from flask import Flask, request,render_template,redirect, url_for, session,logging
import os
import sqlite3

app = Flask(__name__)

@app.route("/")
def loggingin():
    return render_template("login.html")

@app.route("/", methods = ["POST"])
def login():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection("Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        session["log"] = True
        return render_template("home.html")
    else:
        return redirect("/register")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/photo",methods = ["GET"])
def photo():
    return render_template("photo.html")

@app.route("/logout")
def logout():
    session.clear()
    
    return redirect("/")


@app.route("/register", methods= ["GET", "POST"])
def register():
    if request.method == "POST":
        dN = request.form['Dname']
        dUN = request.form['DUsername']
        dPW = request.form['Dpassword']
        cPW = request.form['Cpassword']
        Uemail = request.form['EmalUser']
        if dPW == cPW:
            sqlconnection = sqlite3.Connection("Login.db")
            cursor = sqlconnection.cursor()
            query1 = "INSERT INTO Users VALUES('{n}','{u}','{p}','{cp}','{e}')".format(n = dN, u = dUN, p = dPW, cp = cPW, e = Uemail)
            cursor.execute(query1)
            sqlconnection.commit()
            session["log"] = True
            
            return redirect("/")
        else:
            
            return redirect("/register")
    return render_template("register.html")

@app.route("/flag")
def flagsample():
    from flag import flag
    flag()
    exit()
    return render_template("flag.html")

if __name__=="__main__":
    app.run()
