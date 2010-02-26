import sys
import urllib
import re
from Extract import Extract

class ComparisonChart(object):
    def __init__(self, site1, site2, data1, data2):
        self.site1 = site1
        self.site2 = site2
        self.data1 = data1
        self.data2 = data2

    def get_graph_url_for_field(self, field):
        site_data = {self.site1: None, self.site2: None}
        sites = (self.site1, self.site2)

        max = 0
        total_years = []
        for data in (self.data1, self.data2):
            dates = data.keys()
            for date in dates:
                year = int(date[0:4])
                total_years.append(year)

        total_years = list(set(total_years))

        for (site, data) in ((self.site1,self.data1), (self.site2,self.data2)):
            chart_data = {}

            # fill in empty data for all years
            for year in total_years:
                chart_data[year] = {}
                for month in range(1,13):
                    chart_data[year][month] = []

            dates = data.keys()

            for date in dates:
                year = int(date[0:4])
                month = int(date[4:6])

                if data[date].has_key(field):
                    number = int(data[date][field])
                    chart_data[year][month].append(number)
                    if number > max:
                        max = number
                else:
                    chart_data[year][month].append(0)

            norm_data = {}
            years = chart_data.keys()
            years.sort()

            for y in range(int(years[0]), int(years[-1])+1):
                norm_data[y] = {}
                for m in range(1,13):
                    norm_data[y][m] = 0

            first_year = True
            for year in years:
                mdata = chart_data[year]
                for month in range(1,13):
                    norm_data[year][month] = 0

                    if len(mdata[month]) == 0:
                        if not first_year:
                            if month == 1:
                                prev_year = year - 1
                                norm_data[year][month] = norm_data[year-1][12]
                            else:
                                norm_data[year][month] = norm_data[year][month-1]
                    else:
                        total = 0
                        for num in mdata[month]:
                            total += num
                        avg = float(total) / len(mdata[month])
                        norm_data[year][month] = int(avg)
                first_year = False
            site_data[site] = norm_data

        chtt = "Comparison of %s usage between %s and %s" \
           % (field, self.site1, self.site2)
        chd = 't:'
        first_field = True
        for site in (self.site1, self.site2):
            chart_data = []
            if first_field:
                first_field = False
            else:
                chd += '|'
            
            for year in years:
                for month in range(1,13):
                    chart_data.append(str(site_data[site][year][month]))
            chd += ','.join(chart_data)

        avail_colours = ['FF0000','00FF00','0000FF','FF4500','66CD00','28AE78','00E5EE']
        chco = (avail_colours[0], avail_colours[1])

        chart_query_data = {
            'cht': 'lc',
            'chd': chd,
            'chs': '600x400',
            'chtt': chtt,
            'chco': ','.join(chco),
            'chxt': 'x,y',
            'chdl': '|'.join((self.site1, self.site2)),
            'chxl': '0:|' + '|'.join([str(year) for year in years]) + '|'+str(year+1),
            'chxr': '1,0,' + str(max+5),
            'chds': '0,' + str(max+5)
        }
        url = 'http://chart.apis.google.com/chart?' + urllib.urlencode(chart_query_data)
        url = url.replace('%2C', ',')
        return url
