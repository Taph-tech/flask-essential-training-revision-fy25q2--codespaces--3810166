from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Mustapha'} # Example user data
    return render_template('index.html', title = 'Home', user = user) # Render the index.html template with user data

if __name__ == '__main__':
    app.run(debug=True)
