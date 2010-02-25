#!/usr/bin/python

import sys
import urllib
import urllib2
import xml.dom.minidom as minidom

base_url = 'http://ia360911.us.archive.org:9090/wayback'

domain = 'www.jisc.ac.uk'
query_url = "http://%s/" % domain
data = {
    'type': 'urlquery',
    'url': query_url
}

qs = base_url + '/xmlquery?' + urllib.urlencode(data)

request = urllib2.Request(qs)
try:
    response = urllib2.urlopen(request)
    xml = response.read()
except Exception, e:
    print e
    sys.exit(1)

capture_dates = []
dom = minidom.parseString(xml)
#dom = minidom.parse('cache')
for result_elem in dom.getElementsByTagName('result'):
    for capture_date in result_elem.getElementsByTagName('capturedate'):
        capture_dates.append(capture_date.firstChild.nodeValue)

for date in capture_dates:
    data = {
        'date': date,
        'url': query_url
    }
    qs = base_url + '/replay?' + urllib.urlencode(data)

    try:
        request = urllib2.Request(qs)
        response = urllib2.urlopen(request)
        html = response.read()
        fname = domain + '.' + date
        f = open(fname, 'w')
        f.write(html)
        f.close()
    except Exception, e:
        print e

