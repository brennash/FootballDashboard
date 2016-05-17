from flask import Flask, render_template
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse
from tasks.League import League
from tasks.Fixture import Fixture
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

		if country != 'NULL' and season != 'NULL' and homeTeam != 'NULL' and awayTeam != 'NULL':
			teamList = getTeamList(country, season)
			htmlTable = processLeague(season, country, homeTeam, awayTeam)
			return render_template('league.html', country=country, season=season, homeTeam=homeTeam, awayTeam=awayTeam, homeTeamList=teamList, awayTeamList=teamList, htmlTable=htmlTable)

		elif country != 'NULL' and season != 'NULL' and (homeTeam == 'NULL' or awayTeam == 'NULL'):
			teamList = getTeamList(country, season)
			return render_template('index.html', country=country, season=season, homeTeam=homeTeam, awayTeam=awayTeam, homeTeamList=teamList, awayTeamList=teamList)

		else:
			return render_template('index.html', country=country, season=season, homeTeam='NULL', awayTeam='NULL', homeTeamList=None, awayTeamList=None)
		
def processLeague(season, country, homeTeam, awayTeam):
	fixtureList = getFixtureList(country, season)
	teamList = getTeamList(country, season)
	league = League(country, season)
	league.addFixtures(fixtureList)
	htmlTable = league.getHTMLTable()
	return htmlTable

def getTeamList(country, season):
	countryList = {}
	seasonList = {}
	teamList = []
		
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

	seasonPath = seasonList[season]
	countryPath = countryList[country]
	filePath = 'data/{0}/{1}.csv'.format(seasonPath, countryPath)
	if os.path.exists(filePath):
		inputFile = open(filePath, 'r')
		for index, line in enumerate(inputFile):
			if index > 0:
				elements = line.rstrip().split(',')
				if elements[2] not in teamList:
					teamList.append(elements[2])
			
		teamList.sort()
		return teamList
	else:
		return None
		
def getFixtureList(country, season):
	countryList = {}
	seasonList = {}
	fixtureList = []
		
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

	seasonPath = seasonList[season]
	countryPath = countryList[country]
	filePath = 'data/{0}/{1}.csv'.format(seasonPath, countryPath)
	if os.path.exists(filePath):
		inputFile = open(filePath, 'r')
		header = None
		for index, line in enumerate(inputFile):
			if index == 0:
				header = line.rstrip().split(',')
			else:
				tokens = line.rstrip().split(',')
				fixture = Fixture(header, tokens)
				fixtureList.append(fixture)
	return fixtureList


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
