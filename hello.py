# import flask package. flask makes app objects.
from flask import Flask, render_template

# create Flask web server, makes the application
app = Flask(__name__, template_folder='templates')


# routes determine location
@app.route("/")
# Define simple function
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()


def contact():
    return render_template('contact.html')
