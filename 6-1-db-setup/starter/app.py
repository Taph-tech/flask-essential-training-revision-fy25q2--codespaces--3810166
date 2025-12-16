from flask import Flask, render_template, request
from forms import MyForm
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__) # Initialize the Flask application
app.secret_key = 'supersecretkey'  # Needed for CSRF protection in forms

basedir = os.path.abspath(os.path.dirname(__file__))    # Get the absolute path of the directory where the script is located
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "health_tracker.db") # Or 'sqlite:///health_tracker.db'
#app.config['SQLAlchemy_DATBASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False # To suppress a warning message from SQLAlchemy

db = SQLAlchemy(app) # Initialize the database

@app.route('/form', methods=['GET', 'POST']) # Define the route for the form
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        return render_template('success.html', username=username, email=email)
    return render_template('form.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)

