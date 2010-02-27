from Extractor import Extractor
import re
from webcolors import hex_to_rgb

class ColourExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['red.ness'] = 0		
		results['green.ness'] = 0		
		results['blue.ness'] = 0		
		count = 0
		
		colours = re.findall(r'[\'"](#[a-zA-Z0-9]+)[\'"]', text, re.M|re.I)
		for colour in colours:
			rgb = hex_to_rgb(colour)
			results['red.ness'] += rgb[0]
			results['green.ness'] += rgb[1]
			results['blue.ness'] += rgb[2]
			count += 1

		results['red.ness'] /= count	
		results['green.ness'] /= count	
		results['blue.ness'] /= count	
		return results 
