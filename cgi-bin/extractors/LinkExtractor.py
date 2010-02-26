from Extractor import Extractor
import re

class LinkExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['link.rss'] = 0		
		results['link.atom'] = 0		
		results['link.style'] = 0		
		
		atoms = re.findall(r'\s+type=[\'"]application/atom+xml[\'"]', text, re.M|re.I)
		for atom in atoms:
			results['link.atom'] += 1
		
		rsses = re.findall(r'\s+type=[\'"]application/rss+xml[\'"]', text, re.M|re.I)
		for rss in rsses:
			results['link.rss'] += 1

		styles = re.findall(r'rel=[\'"]stylesheet[\'"]', text, re.I|re.M)
		for style in styles:
			results['link.style'] += 1
		
		return results 
