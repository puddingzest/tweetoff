"""Main application for twitoff"""

# imports
from flask import Flask, render_template


# TODO
# Create landing page/home page in HTML/CSS. Use Danny Choo's site as an example. Just don't plagiarize you donkey.

def create_app():
    """create and configures an instance of a flask app"""
    app: Flask = Flask(__name__)

    @app.route('/')
    def home():
        """Home page."""
        home_page = render_template('home.html', template_folder="templates")
        return home_page

    @app.route('/contact')
    def contact():
        contact = render_template('contact.html', template_folder="templates")
        return contact

    # TODO - Finish up projects and HTML for the page.
    # def projects():
    #     projects() = render_template()




    return app
