import requests
import json
import sys


class SourceController:
	
	def __init__(self, sourcefile, key='785390bcf5cd458d8dd187081b5bb1db'):
		self.sourcefile = sourcefile
		self.sources = {}
		self.key = key

	def get_sourcefile(self):
		return self.sourcefile

	def get_sources(self):
		return self.sources

	def load_sources(self):
		with open(self.sourcefile, 'r') as src_json:
			self.sources = json.load(src_json)
			return 0
		print('failed to read file')
		return -1

	def dump_sources(self):
		with open(self.sourcefile, 'w') as src_json:
			json.dump(self.sources, src_json, indent=4)
			return 0
		print('failed to write to file')
		return -1
	
	def pull_sources(self):
		sources = requests.get('https://newsapi.org/v1/sources')
		if sources:
			return sources.json()
		return -1

	def add_source(self, source_name):
		if source_name in self.sources:
			print('{} is already a source'.format(source_name))
			return -1
		all = self.pull_sources()
		for src in all['sources']:
			if src['name'] == source_name:
				self.sources[source_name] = src
				break
		else:
			print('No source by the name of{}'.format(source_name))
			return -1
		print('{} added as source'.format(source_name))
		return 0
	
	def remove_source(self, source_name):
		if source_name in self.sources:
			self.sources.pop(source_name)
			print('{} removed as source'.format(source_name))
			return 0
		print('failed to remove {} as source'.format(source_name))
		return -1

	def get_articles(self, source):
		if source not in self.sources:
			self.add_source(source)
		payload = {'source': self.sources[source]['id'], 'apiKey': self.key}
		articles = requests.get('https://newsapi.org/v1/articles', params=payload)
		return articles.json()

def main():
	print('---- Source Controller ----')
	if len(sys.argv) > 3:
		if sys.argv[1]:
			sc = SourceController(sys.argv[1])
		
		if sys.argv[2] == 'add':
			if sys.argv[3]:
				sc.load_sources()
				sc.add_source(sys.argv[3].replace("_", " "))
				sc.dump_sources()
		elif sys.argv[2] == 'remove':
			if sys.argv[3]:
				sc.load_sources()
				sc.remove_source(sys.argv[3].replace("_", " "))
				sc.dump_sources()
		else:
			print('enter valid command')
	else:
		print('format of commands:')
		print('python3 news_controller.py [source_file] [add / remove] [source]')
	

if __name__ == '__main__':
	main()




