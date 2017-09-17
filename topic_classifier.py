from source_controller import SourceController
from textblob import TextBlob
import json
from textblob.classifiers import NaiveBayesClassifier
from textblob.np_extractors import ConllExtractor

#####################
#####################
STOPWORDS3 = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', \
			'for', 'from', 'he', 'has', 'in', 'is', 'it', 'itds', \
			'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', \
			'with', 'a', 'about', 'above', 'after', 'again', 'against', \
			'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', \
			'be', 'because', 'been', 'before', 'being', 'below', 'between', \
			'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", \
			'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', \
			'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", \
			'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", \
			"he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', \
			'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', \
			'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', \
			'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', \
			'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', \
			'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", \
			"she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', \
			'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', \
			'there', "there's", 'these', 'they', "they'd", "they'll", "they're", \
			"they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', \
			'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", \
			'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", \
			'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", \
			'would', "wouldn't" ]

######################
######################

def format_training_data(filename):
	arr = []
	with open(filename, 'r') as jso:
		read = json.load(jso)
		for key in read:
			dat = (key, read[key])
			arr.append(dat)
	return arr

def extractor(title):
	feats = {}
	words = title.lower().split()
	for w in words:
		if w not in STOPWORDS3:
			feats[w] = True
	print(feats)
	return feats

#sc = SourceController('Sources/NewSources.json')
#sc.load_sources()

train = format_training_data('TrainingSets/training_set.json')

cl = NaiveBayesClassifier(train, feature_extractor=extractor)
cl.show_informative_features(20)
inp = ''
while(inp != 'quit'):
	inp = input('Enter a News Title: ')
	prob_out = cl.prob_classify(inp)
	print('The genre is {}'.format(prob_out.max()))
	print('prob pol: {}'.format(prob_out.prob('Politics')))
	print('prob tech: {}'.format(prob_out.prob('Technology')))	
	print('prob ent: {}'.format(prob_out.prob('Entertainment')))
