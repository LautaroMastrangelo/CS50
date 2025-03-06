import datetime
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userId = session.get("user_id")
    stocks = db.execute(
        "SELECT symbol, price, ROUND(SUM(CASE WHEN shares > 0 THEN total ELSE -total END), 2) AS finalTotal, SUM(shares) AS finalShares FROM stocks WHERE user_id = ? GROUP BY symbol ", userId)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", userId)
    cash = int(cash[0]["cash"])
    total = 0.0
    for stock in stocks:
        if int(stock['finalShares']) > 0:
            total += stock['finalTotal']
    total += cash
    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Missing symbol")
        elif not shares:
            return apology("Missing symbol")
        elif not lookup(symbol):
            return apology("Invalid symbol")
        elif not shares.isnumeric():
            return apology("Nice try")
        elif (int(shares) < 0 or int(shares) > 99):
            return apology("Invalid amount")
        else:
            # Added a feature to avoid web breaking if founds aren't enough to buy
            userId = session.get("user_id")
            data = db.execute("SELECT cash FROM users WHERE id = ?", userId)
            founds = int(data[0]['cash'])
            shares = int(shares)
            price = float(lookup(symbol)["price"])
            total = price * shares
            if founds < total:
                return apology("Not enough founds")
            else:
                time = datetime.datetime.now()
                time = time.strftime("%Y/%m/%d")
                founds = founds - total
                db.execute("UPDATE users SET cash = ? WHERE id = ?", founds, userId)
                hour = datetime.datetime.now()
                hour = hour.strftime('%H:%M:%S')
                db.execute("INSERT INTO stocks (user_id, symbol, shares, price, total, date, hour) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           userId, symbol, shares, price, total, time, hour)
            # please note that i created a sold.html file to render here, can't use it cause of the check50 requirments
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userId = session.get("user_id")
    stocks = db.execute("SELECT * FROM stocks WHERE user_id = ? ORDER BY DATE DESC, HOUR DESC", userId)
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")
        elif not lookup(symbol):
            return apology("invalid symbol")
        else:
            return render_template("quoted.html", symbol=lookup(symbol))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password or not username or not confirmation:
            return apology("Please fulfill the form")
        elif password != confirmation:
            return apology("passwords don't match")
        else:
            # Search if the username already existe
            existingUser = db.execute("SELECT username FROM users WHERE username = ?", username)
            if existingUser:
                return apology("Username already used")
            else:
                hpass = generate_password_hash(password)
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hpass)
                currentID = db.execute("SELECT id FROM users WHERE username = ?", username)
                session["user_id"] = currentID
                return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    userId = session.get("user_id")
    currentStock = db.execute("SELECT symbol FROM stocks WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) <> 0", userId)
    stocks = db.execute("SELECT symbol, shares FROM stocks WHERE user_id = ? GROUP BY symbol ", userId)
    if request.method == "POST":
        requestedSymbol = request.form.get("symbol")
        requestedShares = request.form.get("shares")
        # Check if incomplete/hacked
        if not requestedShares:
            return apology("No shares")
        elif not requestedSymbol:
            return apology("No symbol")
        elif not requestedShares.isnumeric():
            return apology("nice try")
        else:
            # Check if enough stuff
            for stock in stocks:
                if requestedSymbol in stock["symbol"]:
                    break
            else:
                return apology("Symbol not owned")
            shares = db.execute("SELECT SUM(shares) AS finalShares FROM stocks WHERE (user_id = ? and symbol = ?)",
                                userId, requestedSymbol)
            if int(requestedShares) > int(shares[0]["finalShares"]):
                return apology("Not enough shares")
            else:
                # Prepare to updte sell to the db
                data = db.execute("SELECT cash FROM users WHERE id = ?", userId)
                founds = int(data[0]['cash'])
                price = float(lookup(requestedSymbol)["price"])
                total = price * int(requestedShares)
                requestedShares = -int(requestedShares)
                time = datetime.datetime.now()
                time = time.strftime("%Y/%m/%d")
                founds = founds + total
                db.execute("UPDATE users SET cash = ? WHERE id = ?", founds, userId)
                hour = datetime.datetime.now()
                hour = hour.strftime('%H:%M:%S')
                db.execute("INSERT INTO stocks (user_id, symbol, shares, price, total, date, hour) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           userId, requestedSymbol, requestedShares, price, total, time, hour)
                # please note that i created a bought.html file to render here, can't use it cause of the check50 requirments
                return redirect("/")
    else:
        return render_template("sell.html", stock=currentStock)

# Feature added, lets users delete their account
# Automatically cleans the database.


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password:
            return apology("Please enter your password")
        elif not confirmation:
            return apology("Please confirm your password")
        elif password != confirmation:
            return apology("Passwords don't match")
        else:
            userId = session.get("user_id")
            ph = db.execute("SELECT hash FROM users WHERE id = ?", userId)
            if check_password_hash(str(ph[0]["hash"]), password):
                db.execute("DELETE FROM users WHERE id = ?", userId)
                db.execute("DELETE FROM stocks WHERE user_id = ?", userId)
                session.clear()
                return render_template("deleted.html")
            else:
                return apology("Incorrect password")
    else:
        return render_template("delete.html")


"""
I just wanted to mention that I created two extra HTML files.
bought and sold, since I didn't really understand how to use
pop-up messages, and I was struggling so hard with the rest of
the code, so I decided to take the easy way, but that didn't
fit with checks50, so I have to change to a redirect into the index.
I think the page is good enough, so I'll leave it like this,
although I would like to make it like the staff solution.
Apart from that, it was a really hard, challenging and fun task.
And I know I could have done even better by learning how to use messages.
"""
