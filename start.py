from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
title = "Site Title"

@app.route("/")
def index():
    return render_template('index.html', title=title)
@app.route("/about")
def about():
    return "<h1>About</h1>"


if __name__ == "__main__":
    app.run(debug=True)
