import os
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
	errors = []
	results = {}
	if request.method == "POST":
		# get url that the person has entered
		try:
			url = request.form['url']
			r = requests.get(url).text
		except:
			errors.append(
				"Unable to get URL. Please make sure it's valid and try again."
			)
			return render_template('index.html', errors=errors)
		if r:
			# scraping
			raw = BeautifulSoup(r, 'lxml')
			table = raw.find('table', attrs={'class': 'wikitable'})
			table_rows = table.find_all('tr')
			dic = {}
			for tr in table_rows[1:-1]:
				td = tr.find_all('td')
				row = [i.text for i in td]
				dic[row[0].strip()] = row[3].strip()

			# save the results to be rendered in html
			results = dic.items()

			# add results to database
			try:
				for key, value in dic.items():
				    result = Result(
				        siege_weapon=key,
				        HP=f'{value}',
				    )
				    db.session.add(result)
				db.session.commit()
			except Exception as e:
				errors.append(e)
				errors.append("Unable to add item to database.")
	return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
	app.run()

