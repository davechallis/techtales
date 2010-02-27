import os
import os.path
import sys
import re

class Extract(object):
    def __init__(self, site, datapath='data', cachepath='cache', extractorpath='extractors'):
        self.datapath = datapath
        self.cachepath = cachepath
        self.extractorpath = extractorpath
        self.site = site
        self.results = {}
        self.html = ''

    def run(self):
        cachefile = self.cachepath+'/'+self.site
        # If we have a cache, unpickle and return.
        if os.path.exists(cachefile):
            f = open(cachefile, 'r')
            self.results = pickle.load(file) 
            f.close()
            return self.results

        # Otherwise do the processing.
        for file in os.listdir(self.datapath):
            if file.startswith(self.site):
                f = open(self.datapath+'/'+file, 'r')
                self.html = f.read()
                f.close()

                date = file.split('.').pop()
                self.results[date] = self.run_extractors()

        # Dump out the cache file        
        cache = open(cachefile, 'w')
        pickle.dump(self.results, cache)
        cache.close()

        return self.results

    def run_extractors(self):
        skip = ('Extractor.py', '__init__.py')

        data = {}

        for file in os.listdir(self.extractorpath):
            if file.endswith('.pyc'):
                continue

            if file in skip:
                continue

            (classname, ext) = os.path.splitext(file)
            mod = __import__('extractors.'+classname)

            line = 'mod.%s.%s()' % (classname,classname)
            obj = eval(line)
            results = obj.run(self.html)
            data.update(results)

        return data
