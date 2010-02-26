from Extractor import Extractor
import re

class AccessExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['access.ness'] = 0		
		
		alts = re.findall(r'\s+alt=[\'"][^\'"]+[\'"]', text, re.M|re.I)
		for alt in alts:
			results['access.ness'] += 1
		
		titles = re.findall(r'\s+title=[\'"][^\'"]+[\'"]', text, re.M|re.I)
		for title in titles:
			results['access.ness'] += 1
		

		accesskeys = re.findall(r'\s+accesskey=[\'"][^\'"]+[\'"]', text, re.M|re.I)
		for accesskey in accesskeys:
			results['access.ness'] += 1
		
		longdescs = re.findall(r'\s+longdesc=[\'"][^\'"]+[\'"]', text, re.M|re.I)
		for longdesc in longdescs:
			results['access.ness'] += 1
		
		return results 
