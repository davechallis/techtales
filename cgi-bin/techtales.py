#!/usr/bin/python

import cherrypy
from simplejson import dumps 
import os.path

#cherrypy.config['log.error_file'] = '/home/www/sites/techtales/logs/py_error.log'

class Stats:
	def default(self, uri=None):
		if not uri:
		    return dumps({'status':'error', 'message':'Need URI'})
		return dumps({})

	default.exposed = True

class Main:
	stats = Stats()
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
