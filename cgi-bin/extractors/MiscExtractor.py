from Extractor import Extractor
import re

class MiscExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['secret.ness'] = 0		
		
		comments = re.findall(r'<!--(.+)-->', text, re.M|re.I)
		for comment in comments:
			results['secret.ness'] += round(len(comment)/10)
		
		return results 
