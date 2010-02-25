from Extractor import Extractor
import re

class TagExtractor(Extractor):

	def run(self, text):
		results = dict()
		group = re.findall(r"<([a-zA-Z0-9]+)\b", text, re.I|re.M)
		for tag in group:
			if results.has_key(tag):
				results[tag] += 1
			else:
				results[tag] = 1
		return results 
