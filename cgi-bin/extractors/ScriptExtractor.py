from Extractor import Extractor
import re

class ScriptExtractor(Extractor):

	def run(self, text):
		results = dict()
		results['js.ness'] = 0

		if re.search(r'[\'"][^\'"]+prototype.js[\'"]', text, re.M|re.I):
			results['js.ness'] += 1
			results['js.prototype'] = 1
		
		if re.search(r'[\'"][^\'"]+scriptaculous.js[\'"]', text, re.M|re.I):
			results['js.ness'] += 1
			results['js.scriptaculous'] = 1
		
		if re.search(r'[\'"][^\'"]+mootools.js[\'"]', text, re.M|re.I):
			results['js.ness'] += 1
			results['js.mootools'] = 1
		
		if re.search(r'[\'"][^\'"]+jquery.js[\'"]', text, re.M|re.I):
			results['js.ness'] += 1
			results['js.jquery'] = 1
		
		jss = re.findall(r'type=[\'"]text/javascript[\'"]', text, re.I|re.M)
		for js in jss:
			results['js.ness'] += 1
		
		return results 

