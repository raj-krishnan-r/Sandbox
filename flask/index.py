from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def index():	
	print(request)
	print(request.accept_charsets)
	return "Hi"
@app.route('/a')
def a():
	print(request)
	return "A"


