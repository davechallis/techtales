from Extractor import Extractor
import re

class ImageExtractor(Extractor):

	def run(self, text):
		results = dict()

		results['image.gif'] = 0		
		results['image.jpg'] = 0		
		results['image.png'] = 0		
		
		images = re.findall(r'<img.+src=[\'"]([^\'"]+)[\'"]', text, re.M|re.I)
		
		for image in images:
			if image.endswith(".gif"):
				results['image.gif'] += 1
			if image.endswith(".jpeg") or image.endswith(".jpg"):
				results['image.jpg'] += 1
			if image.endswith(".png"):
				results['image.png'] += 1
		
		return results 
