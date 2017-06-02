import flask from Flask # imported the flask entry 

app = Flask("__name__") #created a flask instance

@app.route('/')

def helloWorld(): #the only function in our boilerplate program
	return 'Hello World'


