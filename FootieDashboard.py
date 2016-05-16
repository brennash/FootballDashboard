from flask import Flask, render_template
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)

@app.route('/')
def index():
	print request.url 
	return render_template('index.html', initialSelection=True)

@app.route('/api/v1.0/tasks', methods=['GET'])
def getTask():
	if request.method == "GET":
		league = request.args.get('league')
		season = request.args.get('season')
		homeTeam = request.args.get('homeTeam')
		awayTeam = request.args.get('awayTeam')
		urlPath = request.path
		
	return render_template('stats.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
