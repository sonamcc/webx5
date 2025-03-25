from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Dynamic User Page
@app.route('/user/<username>')
def user(username):
    return render_template("user.html", username=username)

# About Page
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
