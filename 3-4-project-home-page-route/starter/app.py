from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST']) # Route to handle form display and submission
def form():
      if request.method == 'POST':  # Check if the form is submitted posted
          # Process form data here
          return redirect(url_for('dashboard')) # Redirect to dashboard after form submission
                                                # dashboard should not have dashboard.html
      return render_template('form.html') # Render the form template for GET requests
  
@app.route('/dashboard') # Dashboard route to display after form submission
def dashboard():
    return render_template('dashboard.html') # Render the dashboard template

if __name__ == '__main__':
    app.run(debug=True)
