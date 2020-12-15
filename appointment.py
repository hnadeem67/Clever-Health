from flask import Flask, render_template, request
import sqlite3
import os
currentdirectory= os.path.dirname(os.path.abspath(__file__))
app = Flask (__name__)

@app.ruoute("/"):
def main():
    return reder_template("Appointment.html")

@app.route("/", methods = ["POST"])





if __name__=="__main__":
    app.run()