#!/usr/bin/python

import cherrypy
from simplejson import dumps 
import os.path
from ComparisonChart import ComparisonChart
from Chart import Chart as GoogleChart
from Extract import Extract
#cherrypy.config['log.error_file'] = '/home/www/sites/techtales/logs/py_error.log'

datapath = '/home/www/sites/techtales/cgi-bin/data'
cachepath = '/home/www/sites/techtales/cache'
extractorpath = '/home/www/sites/techtales/cgi-bin/extractors'

class CompareChart:
	def default(self, url1=None, url2=None, field=None):
		if not url1 or not url2 or not field:
			return dumps({'status':'error', 'message':'Need URIs and field'})
		extract1 = Extract(url1, datapath, cachepath, extractorpath) 
		extract2 = Extract(url2, datapath, cachepath, extractorpath)
		data1 = extract1.run()
		data2 = extract2.run()
		chart = ComparisonChart(url1, url2, data1, data2)
		url = chart.get_graph_url_for_field(field)
		return dumps({'status':'ok', 'url':url})		
	
	default.exposed = True


class Chart:
	def default(self, url=None, fields=None):
		if not url or not fields:
			return dumps({'status':'error', 'message':'Need URI and fields'})
		extract = Extract(url, datapath, cachepath, extractorpath)
		data = extract.run()
		chart = GoogleChart(data)
		field_arr = fields.split(",")
		nfield_arr = []
		for field in field_arr:
			field = field.strip()
			if field != '':
				nfield_arr.append(field)

		if len(nfield_arr) == 1:
			url = chart.get_graph_url_for_field(nfield_arr[0])
		else:
			url = chart.get_graph_url_for_fields(nfield_arr)
		return dumps({'status':'ok', 'url':url})		
	
	default.exposed = True

class Stats:
	def default(self, url=None):
		if not url:
		    return dumps({'status':'error', 'message':'Need URL'})
		extract = Extract(url, datapath, cachepath, extractorpath)
		data = extract.run()
		return dumps({'status':'ok', 'data':data})

	default.exposed = True

class Main:
	stats = Stats()
	chart = Chart()
	comparechart = CompareChart()
#
# These methods take care of running the application via either mod_python or
# stand-alone using the built-in CherryPy server.
#
def start_modpython():
    cherrypy.engine.SIGHUP = None
    cherrypy.engine.SIGTERM = None
    cherrypy.tree.mount(Main(), '/service')
    cherrypy.engine.start(blocking=False)

def start_standalone():
    cherrypy.quickstart(Main(), '/service')

#
# If we're not being imported, it means we should be running stand-alone.
#
if __name__ == '__main__':
	cherrypy.config['log.error_file'] = 'logs/py_error.log'
	start_standalone()

