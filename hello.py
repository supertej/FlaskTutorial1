from flask import Flask, request, jsonify, json # imported the flask entry

app = Flask("__name__") #created a flask instance

@app.route('/')

def helloWorld(): #the only function in our boilerplate program
	return 'Hello World'


