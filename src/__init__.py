from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        welcome_message = "RSBP D Final Project"
        return render_template('index.html', title='Pattern Matching', welcome_message=welcome_message) 
    else:
        pat = request.form.get['pattern']
        seq = request.form.get['sequence']
        data = {'pattern': pat, 'sequence': seq}
        response_json = json.dumps(data, default=lambda o: o.encode(), indent=4)
        response = requests.post("http://127.0.0.1:5000/api/regex/ssr_new", response_json)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)