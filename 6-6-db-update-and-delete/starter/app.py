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
    return redirect(url_for('users'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        new_user = User(username=username, email=email)
        db.session.add(new_user) # stage the new user for addition
        db.session.commit() # save the new user to the database

        return redirect(url_for('success', username=username, email=email))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    #retrieve username and email from the URL query string
    username = request.args.get('username') 
    email = request.args.get('email')
    return render_template('success.html', username=username, email=email)

@app.route('/users', methods =['GET', 'POST'])
def users():
    if request.method == 'POST':    #handle update requests
        user_id = request.form.get('user_id')   #get the user ID from the form
        new_email = request.form.get('new_email') #get the new email from the form
        user_to_update = User.query.get(user_id)  #find the user by ID
        if user_to_update:   #if user exists, update the email
            user_to_update.email = new_email #update the email field
            db.session.commit() #save changes to the database
        return redirect(url_for('users'))
     # Get request to display all users below   
    #retrieve all records from the User table in the db
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/delete_user/<int:id>', methods= ['POST'])
def delete_user(id):
      user = User.query.get(id)  #get the user ID from the form
      if user:
          db.session.delete(user) #delete the user from the database
          db.session.commit()  #save changes to the database
          return redirect(url_for('users')) #redirect to the users page
      elif not user:  #if user does not exist
          return "User not found", 404  #return 404 error if user not found
    

if __name__ == '__main__':
    app.run(debug=True)

