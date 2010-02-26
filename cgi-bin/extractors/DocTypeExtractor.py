from Extractor import Extractor
import re

class DocTypeExtractor(Extractor):

	def run(self, text):
		results = dict()
		p2 = re.search(r'<!DOCTYPE\s+(\S+)\s+PUBLIC\s+"([^"]+?)"\s+"([^"]+?)">', text, re.M|re.I)
		if p2:
			results['root'] = p2.group(1)
			results['fpi'] = p2.group(2)
			results['uri'] = p2.group(3)
			results['kind'] = 'public'
		
		p1 = re.search(r'<!DOCTYPE\s+(\S+)\s+PUBLIC\s+"([^"]+)">', text, re.M|re.I)
		if p1:
			results['root'] = p1.group(1)
			results['fpi'] = p1.group(2)
	
		s1 = re.search(r'<!DOCTYPE\s+(\S+)\s+SYSTEM\s+"(.+)">', text, re.M|re.I)
		if s1:
			results['root'] = s1.group(1)
			results['uri'] = s1.group(2)

		d1 = re.search(r'<!DOCTYPE\s+(\S+)>', text, re.M|re.I)
		if d1:
			results['root'] = d1.group(1)
		return results 
