import json
from flask import *
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__, static_url_path='/static', template_folder='static', )


# a route where we will display a welcome message via an HTML template
@app.route("/")
def home():
    return render_template("index.html")


# run the application
if __name__ == "__main__":
    app.run(debug=True)
