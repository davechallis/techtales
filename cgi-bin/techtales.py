#!/usr/bin/python

import cherrypy
from simplejson import dumps 
import os.path
from Chart import Chart as GoogleChart
from Extract import Extract
#cherrypy.config['log.error_file'] = '/home/www/sites/techtales/logs/py_error.log'

class Chart:
	def default(self, url=None, fields=None):
		if not url or not fields:
			return dumps({'status':'error', 'message':'Need URI and fields'})
		extract = Extract(url)
		data = extract.run()
		chart = GoogleChart(data)
		url = chart.get_graph_url_for_fields(fields)
		return dumps({'status':'ok', 'url':url})		
	
	default.exposed = True

class Stats:
	def default(self, url=None):
		if not url:
		    return dumps({'status':'error', 'message':'Need URL'})
		extract = Extract(url)
		data = extract.run()
		return dumps({'status':'ok', 'data':data})

	default.exposed = True

class Main:
	stats = Stats()
	chart = Chart()
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

