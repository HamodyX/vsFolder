from flask import Flask, render_template, url_for, redirect, request, jsonify
import smtplib
from email.mime.text import MIMEText
from currencyE import currency


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", content= "Testing")

@app.route('/second_page')
def second_page():
    return render_template("sec.html", content="testing")

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received data:", data)
    result = {'message': currency()}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

