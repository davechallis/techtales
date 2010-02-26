from Extractor import Extractor
import re

class SocialExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['social.ness'] = 0		
		results['social.twitter'] = 0		
		results['social.facebook'] = 0		
		
		twitters = re.findall(r'[\'"]http://([^\'"]*)twitter\.com', text, re.M|re.I)
		for twitter in twitters:
			results['social.ness'] += 1
			results['social.twitter'] += 1
		
		facebooks = re.findall(r'[\'"]http://([^\'"]*)facebook\.com', text, re.M|re.I)
		for facebook in facebooks:
			results['social.ness'] += 1
			results['social.facebook'] += 1
		
		myspaces = re.findall(r'[\'"]http://([^\'"]*)myspace\.com', text, re.M|re.I)
		for myspace in myspaces:
			results['social.ness'] += 1
			results['social.myspace'] += 1
		
		return results 
