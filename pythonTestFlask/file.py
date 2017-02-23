from flask import Flask
from flask import render_template
from flask import request
import Contact

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	error = None
	contact = Contact();
	if request.method == 'POST':
		contact = Contact(request.form['firstName'], request.form['lastName'], request.form['phone'], request.form['address'], request.form['email'])
		contact.validate()

	return render_template('index.html', contact = contact)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/file')
def file():
	return 'Hello, World'