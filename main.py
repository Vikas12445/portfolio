import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Use environment variable for secret key (set in your system or a .env file)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', 'dev_key')  # Fallback for local testing

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save the message to a file
        with open('message.txt', "a") as file:
            file.write(f"{name} | {email} | {message}\n")

        return render_template('success.html', name=name, email=email)
    return redirect('/')

# Only run the server if this is the main script
if __name__ == '__main__':
    app.run(debug=False)

