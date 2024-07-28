from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Process the form data as needed
    return f"Thank you, {name}! Your email ({email}) has been received."

if __name__ == '__main__':
    app.run(debug=True)
