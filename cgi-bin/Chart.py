import sys
import urllib
import re
import copy
from Extract import Extract
class Chart(object):
    def __init__(self, extracted_data):
        self.data = extracted_data

    def get_graph_url_for_fields(self, fields):
        nfields = []
        for field in fields:
            if field.strip() != '':
                nfields.append(field)

        fields = nfields
        if len(fields) == 1:
            return self.get_graph_url_for_field(fields[0])

        data = self.data
        dates = data.keys()
        dates.sort()

        total_years = []
        empty_chart_data = {}
        for date in dates:
            year = date[0:4]
            total_years.append(year)
        total_years = list(set(total_years))
        total_years.sort()

        for year in range(int(total_years[0]), int(total_years[-1])+1):
            empty_chart_data[year] = {}
            for month in range(1,13):
                empty_chart_data[year][month] = []

        field_data = {}

        max = 0
        for field in fields:
            #chart_data = empty_chart_data.copy()
            chart_data = copy.deepcopy(empty_chart_data)
            for date in dates:
                year = int(date[0:4])
                month = int(date[4:6])

                if data[date].has_key(field):
                    number = int(data[date][field])
                    chart_data[year][month].append(number)
                else:
                    chart_data[year][month].append(0)

            norm_data = {}
            years = chart_data.keys()
            years.sort()

            first_year = True
            for year in years:
                norm_data[year] = {}

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
                        avg = int(avg)
                        if avg > max: max = avg

                first_year = False
            field_data[field] = norm_data

        chtt = "Comparison of %s usage" % ', '.join(fields)
        chd = 't:'
        first_field = True
        for field in fields:
            chart_data = []
            if first_field:
                first_field = False
            else:
                chd += '|'
            
            for year in years:
                for month in range(1,13):
                    chart_data.append(str(field_data[field][year][month]))
            chd += ','.join(chart_data)

        chco = []
        avail_colours = ['FF0000','00FF00','0000FF','FF4500','66CD00','28AE78','00E5EE']
        for field in fields:
            chco.append(avail_colours.pop(0))

        chart_query_data = {
            'cht': 'lc',
            'chd': chd,
            'chs': '600x400',
            'chtt': chtt,
            'chco': ','.join(chco),
            'chxt': 'x,y',
            'chdl': '|'.join(fields),
            'chxl': '0:|' + '|'.join([str(year) for year in years]) + '|'+str(year+1),
            'chxr': '1,0,' + str(max+5),
            'chds': '0,' + str(max+5)
        }
        url = 'http://chart.apis.google.com/chart?' + urllib.urlencode(chart_query_data)
        url = url.replace('%2C', ',')
        return url
        

    def get_graph_url_for_field(self, field):
        data = self.data
        dates = data.keys()
        dates.sort()

        chart_data = {}

        total_years = []
        for date in dates:
            year = date[0:4]
            total_years.append(year)
        total_years = list(set(total_years))
        total_years.sort()


        for year in range(int(total_years[0]), int(total_years[-1])+1):
            chart_data[year] = {}
            for month in range(1,13):
                chart_data[year][month] = []

        max = 0
        for date in dates:
            year = int(date[0:4])
            month = int(date[4:6])

            if data[date].has_key(field):
                number = int(data[date][field])
                chart_data[year][month].append(number)
            else:
                chart_data[year][month].append(0)

        norm_data = {}
        years = chart_data.keys()
        years.sort()

        first_year = True
        for year in years:
            norm_data[year] = {}

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
                    avg = int(avg)
                    if avg > max: max = avg

            first_year = False


        chtt = "%s usage" % field
        chd = []
        for year in years:
            for month in range(1,13):
                chd.append(str(norm_data[year][month]))

        chart_query_data = {
            'cht': 'lc',
            'chd': 't:' + ','.join(chd),
            'chs': '600x400',
            'chtt': chtt,
            'chxt': 'x,y',
            'chxl': '0:|' + '|'.join([str(year) for year in years]) + '|'+str(year+1),
            'chxr': '1,0,' + str(max+5),
            'chds': '0,' + str(max+5)
        }
        url = 'http://chart.apis.google.com/chart?' + urllib.urlencode(chart_query_data)
        return url

