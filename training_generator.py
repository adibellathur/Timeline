from source_controller import SourceController
import json
import sys

class TrainingGenerator:
	
	def __init__(self, sourcefile, trainingfile):
		self.tset = {}
		self.trainingfile = trainingfile
		self.sc = SourceController(sourcefile)
	
	def load_tset(self):
		with open(self.trainingfile, 'r') as ts:
			self.tset = json.load(ts)
			return 0
		print('failed to read file')
		return -1

	def dump_tset(self):
		with open(self.trainingfile, 'w') as ts:
			json.dump(self.tset, ts, indent=4)
			return 0
		print('training set on {} dump failed'.format(self.trainingfile))
		return -1

	def get_titles(self):
		self.sc.load_sources()
		for src in self.sc.get_sources():
			print('-- SOURCE: {} --'.format(src))
			articles = self.sc.get_articles(src)
			for art in articles['articles']:
				title = art['title']
				if title not in self.tset:
					print(title)
					self.tset[title] = ""
		return 0

	def classify_titles(self):
		for title in self.tset:
			if self.tset[title] == '':
				print(title)
				topic = input('Topic: ')
				#insert topic validator later
				self.tset[title] = topic
		return 0

	
def main():	
	print('---- Topic Generator ----')
	if len(sys.argv) > 2:
		if sys.argv[1] == 'get':
			test = TrainingGenerator(sys.argv[2], sys.argv[3])
			if sys.argv[2]:
				sourcefile = sys.argv[2]
				test.load_tset()
				test.get_titles(sourcefile)
				test.dump_tset()
			return 0
		elif sys.argv[1] == 'classify':
			test = TrainingGenerator(sys.argv[2], sys.argv[3])
			test.load_tset()
			test.classify_titles()
			test.dump_tset()
			return 0
		else:
			print('Incorrect command specified. Arguements are as follows:')
	else:
		print('No command specified. Arguements are as follows:')
	print('--get: get more headlines from sources')
	print('--classify: specify the topic of un-classified titles')
	print('format: python3 training_generator.py [get/classify] [source_file] [training_set_file]')

if __name__ == '__main__':
	main()
