import os
import os.path
import sys
import re

class Extract(object):
    def __init__(self, site):
        self.site = site
        self.results = {}
        self.html = ''

    def run(self):
        for file in os.listdir('data'):
            if file.startswith(self.site):
                f = open('data/' + file, 'r')
                self.html = f.read()
                f.close()

                date = file.split('.').pop()
                self.results[date] = self.run_extractors()
        return self.results


    def run_extractors(self):
        skip = ('Extractor.py', '__init__.py')

        data = {}

        for file in os.listdir('extractors'):
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
