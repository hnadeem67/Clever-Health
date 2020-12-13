import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, session, flash
import backend

app = Flask(__name__)
host = 'http://127.0.0.1:5000/'


@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = sql.connect('Clever_health.db')

    if request.method == 'POST':
        if "SignUp" in request.form:
            CreateUser(request.form['name'], request.form['email'], request.form['password'])

            return render_template('Registration.html', url=host)

    return render_template("Registration.html", error=None)


def CreateUser(FullName, Email, Password):
    conn = sql.connect('Clever_health.db')
    conn.execute('INSERT INTO Users (FullName, Email, Password) VALUES (?,?,?)',
                 (FullName, Email, Password))
    conn.commit()



if __name__ == '__main__':
    app.run(debug=True)
