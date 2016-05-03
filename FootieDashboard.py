from flask import Flask, render_template
from flask import request
from flask.ext import restful

app = Flask(__name__)

@app.route('/')
def index():
	print request.url 
	return render_template('index.html', initialSelection=True)

@app.route('/league/<string:league>/<string:season>', methods=['GET'])
def get_task(league, season):
	print league, season
	return render_template('index.html', initialSelection=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
