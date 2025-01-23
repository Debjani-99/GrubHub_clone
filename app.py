from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("login.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

# @app.route("/menu")
# def render_menu():
#     return "<ul> <li> Coffee </li> <li> Tea </li> </ul>"

if __name__ == "__main__":
    app.run()

