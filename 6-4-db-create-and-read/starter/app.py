from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    
    

    def __repr__(self):
        return f'<User {self.username}>'
@app.route('/')
def index():
    return redirect(url_for('form'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        
        new_user = User(username=username, email= email) # Create a new user instance
        if(User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()):
            return "User with this username or email already exists!"
        db.session.add(new_user) # Add the new user to the db session
        db.session.commit()   # Save the new user to the database
        return redirect(url_for('success', username=username, email=email)) # Redirect to success page
    return render_template('form.html', form=form) # Render the form template add .html with render_template

@app.route('/success')
def success():
    username = request.args.get('username')
    email = request.args.get('email')
    return render_template('success.html', username=username, email=email) # Render the success template add .html with render_template

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    app.run(debug=True)

