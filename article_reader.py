from source_controller import SourceController
import json
import sys
import requests
from bs4 import BeautifulSoup

class ArticleReader:
	def __init__(self, sourcefile):
		self.sc = SourceController(sourcefile)

	def get_articles(self, source):
		articles = self.sc.get_articles(source)
		url = []
		for art in articles['articles']:
			url.append(art['url'])
		return url

	def scrape_page(self, url):
		html = requests.get(url)
		soup = BeautifulSoup(html.text)
		print(soup.prettify())

reader = ArticleReader('sources.json')
ta = reader.get_articles('The New York Times')[3]
print(ta)
reader.scrape_page(ta)