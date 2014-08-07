from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
	return "Hello Seoul"

if __name__ == "__main__":
	app.debug = True
	app.run()