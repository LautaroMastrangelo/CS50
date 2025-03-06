import os

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Returns true if the month and day ingresed are valid
# Works with the current year
def validDate(month, day):
    try:
        datetime(datetime.now().year, month, day)
        return True
    except ValueError:
        return False


# Returns true if month and day are numbers
def isNumber(month, day):
    try:
        int(month)
        pass
    except ValueError:
        return False
    try:
        int(day)
        return True
    except ValueError:
        return False

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        if name and month and day and isNumber(month, day) and (validDate(int(month), int(day))):
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return redirect("/")
    else:
        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


"""
Features added:
-can delete birthdays
-doesn't work without correct input
-prevents negative even with user' html editing
-checks if the month and day ingresed are valid (for example 2/31 is invalid)
-checks if the month and day are really numbers

Extra notes:
I wanted to do a query for selecting the month and day but I found it quite harder than I expected
I also couldn't think a way of letting the user edit the birthdays, that's why it isn't implemented
"""
