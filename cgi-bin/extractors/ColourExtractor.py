from Extractor import Extractor
from webcolors import hex_to_rgb
import re

class ColourExtractor(Extractor):

	def run(self, text):
		results = dict()

		total_red = 0
		total_green = 0
		total_blue = 0
		count = 0

		colours = re.findall(r'(#[a-fA-F0-9]+)', text, re.M|re.I)
		for colour in colours:
			rgb = hex_to_rgb(colour)
			total_red += rgb[0]
			total_green += rgb[1]
			total_blue += rgb[2]
			count += 1
	
		total_red /= count	
		total_green /= count	
		total_blue /= count	

		results['colour.red'] = total_red
		results['colour.green'] = total_green
		results['colour.blue'] = total_blue
	
		return results 
