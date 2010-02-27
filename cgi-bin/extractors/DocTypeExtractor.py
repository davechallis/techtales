from Extractor import Extractor
import re

class DocTypeExtractor(Extractor):

	def run(self, text):
		results = dict()

		root = None
		fpi = None
		uri = None

		p2 = re.search(r'<!DOCTYPE\s+(\S+)\s+PUBLIC\s+"([^"]+?)"\s+"([^"]+?)">', text, re.M|re.I)
		if p2:
			fpi = p2.group(2)
			uri = p2.group(3)

		p1 = re.search(r'<!DOCTYPE\s+(\S+)\s+PUBLIC\s+"([^"]+)">', text, re.M|re.I)
		if p1:
			root = p1.group(1)
			fpi = p1.group(2)

		if fpi:
			if fpi == "-//W3C//DTD HTML 4.01//EN":
				results['doctype.html401_strict'] = 1
				results['doctype.html401'] = 1
				results['doctype.html'] = 1
			elif fpi == "-//W3C//DTD HTML 4.01 Transitional//EN":
				results['doctype.html401_transitional'] = 1
				results['doctype.html401'] = 1
				results['doctype.html'] = 1
			elif fpi == "-//W3C//DTD HTML 4.01 Frameset//EN":
				results['doctype.html401_frames'] = 1
				results['doctype.html401'] = 1
				results['doctype.html'] = 1
			elif fpi == "-//W3C//DTD XHTML 1.0 Strict//EN":
				results['doctype.xhtml1_strict'] = 1
				results['doctype.xhtml1'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//W3C//DTD XHTML 1.0 Transitional//EN":
				results['doctype.xhtml1_transitional'] = 1
				results['doctype.xhtml1'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//W3C//DTD XHTML 1.0 Frameset//EN":
				results['doctype.xhtml1_frames'] = 1
				results['doctype.xhtml1'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//W3C//DTD XHTML 1.1//EN":
				results['doctype.xhtml11'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//W3C//DTD XHTML Basic 1.0//EN":
				results['doctype.xhtml10_basic'] = 1
				results['doctype.xhtml10'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//W3C//DTD XHTML Basic 1.1//EN":
				results['doctype.xhtml11_basic'] = 1
				results['doctype.xhtml11'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//WAPFORUM/DTD XHTML Mobile 1.0//EN":
				results['doctype.mobile10'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//WAPFORUM/DTD XHTML Mobile 1.1//EN":
				results['doctype.mobile11'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1
			elif fpi == "-//WAPFORUM/DTD XHTML Mobile 1.2//EN":
				results['doctype.mobile12'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1
				results['doctype.ness'] = 0

		
		s1 = re.search(r'<!DOCTYPE\s+(\S+)\s+SYSTEM\s+"(.+)">', text, re.M|re.I)
		if s1:
			root = s1.group(1)
			uri = s1.group(2)
		
		if uri:
			if uri == "http://www.w3.org/TR/html4/strict.dtd":
				results['doctype.html401_strict'] = 1
				results['doctype.html'] = 1
				results['doctype.ness'] = 3
			elif uri == "http://www.w3.org/TR/html4/loose.dtd":
				results['doctype.html401_transitional'] = 1
				results['doctype.html'] = 1
				results['doctype.ness'] = 2
			elif uri == "http://www.w3.org/TR/html4/frameset.dtd":
				results['doctype.html401_frames'] = 1
				results['doctype.html'] = 1
				results['doctype.ness'] = 1
			elif uri == "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd":
				results['doctype.xhtml1_strict'] = 1
				results['doctype.xhtml'] = 1
				results['doctype.ness'] = 6
			elif uri == "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd":
				results['doctype.xhtml1_transitional'] = 1
				results['doctype.xhtml'] = 1
				results['doctype.ness'] = 5
			elif uri == "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd":
				results['doctype.xhtml1_frames'] = 1
				results['doctype.xhtml'] = 1
				results['doctype.ness'] = 4
			elif uri == "http://www.w3.org/TR/xhtml1/DTD/xhtml11.dtd":
				results['doctype.xhtml11'] = 1
				results['doctype.xhtml'] = 1
				results['doctype.ness'] = 7
			elif uri == "http://www.w3.org/TR/xhtml-basic/xhtml-basic10.dtd":
				results['doctype.xhtml10_basic'] = 1
				results['doctype.xhtml10'] = 1
				results['doctype.xhtml'] = 1
			elif uri == "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd":
				results['doctype.xhtml10'] = 1
				results['doctype.xhtml'] = 1
			elif uri == "http://www.wapforum.org/DTD/xhtml-mobile10.dtd":
				results['doctype.mobile10'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1
			elif uri == "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile11.dtd":
				results['doctype.mobile11'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1
			elif uri == "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd":
				results['doctype.mobile12'] = 1
				results['doctype.mobile'] = 1
				results['doctype.xhtml'] = 1


		d1 = re.search(r'<!DOCTYPE\s+(\S+)>', text, re.M|re.I)
		if d1:
			root = d1.group(1)
			results['doctype.html5'] = 1
			results['doctype.ness'] = 8

		return results 
