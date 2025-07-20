from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
