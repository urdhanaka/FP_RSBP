from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    welcome_message = "RSBP D Final Project"
    return render_template('index.html', title='Pattern Matching', welcome_message=welcome_message)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
