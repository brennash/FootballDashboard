from flask import Flask, render_template
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse
import csv
import os
app = Flask(__name__)

@app.route('/')
def index():
	print request.url 
	return render_template('index.html', country='NULL', season='NULL', homeTeam='NULL', awayTeam='NULL', homeTeamList=None, awayTeamList=None)

@app.route('/api/v1.0/league', methods=['GET'])
def getTask():
	if request.method == "GET":
		country = request.args.get('country')
		season = request.args.get('season')
		homeTeam = request.args.get('homeTeam')
		awayTeam = request.args.get('awayTeam')

		print 'HOMETEAM:',homeTeam
		print 'AWAYTEAM:',awayTeam

		homeTeamList = []
		awayTeamList = []
		countryList = {}
		seasonList = {}
		
		seasonList['2015-2016'] = '1615'
		seasonList['2014-2015'] = '1514'
		seasonList['2013-2014'] = '1413'
		seasonList['2012-2013'] = '1312'
		seasonList['2011-2012'] = '1211'
		seasonList['2010-2011'] = '1110'
		seasonList['2009-2010'] = '1009'
		seasonList['2008-2009'] = '0908'       
		countryList['Belgium']  = 'B1'
		countryList['England']  = 'E0'
		countryList['France']   = 'F1'
		countryList['Holland']  = 'N1'
		countryList['Germany']  = 'D1'
		countryList['Greece']   = 'G1'
		countryList['Italy']    = 'I1'
		countryList['Spain']    = 'SP1'
		countryList['Scotland'] = 'SC0'
		countryList['Turkey']   = 'T1'

		if country != 'NULL' and season != 'NULL':
			seasonPath = seasonList[season]
			countryPath = countryList[country]
			filePath = 'data/{0}/{1}.csv'.format(seasonPath, countryPath)
			print 'opening file...'
			if os.path.exists(filePath):
				inputFile = open(filePath, 'r')
				for index, line in enumerate(inputFile):
					if index > 0:
						elements = line.rstrip().split(',')
						homeTeam = elements[2]
						awayTeam = elements[3]
						if homeTeam not in homeTeamList:
							homeTeamList.append(homeTeam)
						if awayTeam not in awayTeamList:
							awayTeamList.append(awayTeam)
							
			homeTeamList.sort()
			awayTeamList.sort()

			return render_template('index.html', country=country, season=season, homeTeam=homeTeam, awayTeam=awayTeam, homeTeamList=homeTeamList, awayTeamList=awayTeamList)
		else:
			return render_template('index.html', country=country, season=season, homeTeam=None, awayTeam=None, homeTeamList=None, awayTeamList=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
