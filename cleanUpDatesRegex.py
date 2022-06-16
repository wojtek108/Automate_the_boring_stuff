# Clean up dates in different date formats (such as 3/14/2019, 03-14-2019,
# and 2015/3/19) by replacing them with dates in a single, standard format.

import re

string = ''' The date is 12/31/2020 11/18.1985 and the next is 3/30/1902,
2015-02-20, 1988.12.31'''


def dateCleanUp(text):
    # regex for date format MM/DD/YYYY and another separators
    aDateReg = re.compile(r'''
            (0?[1-9]|1[012])
            [-/.]
            (0[1-9]|[12][0-9]|3[01])
            [-/.]
            (19\d{2}|20[01][0-9]|2020)
            \b''', re.VERBOSE)
    
    mo = aDateReg.findall(text)
    
    m = []
    d = []
    y = []
    
    for n in mo:
        month, day, year = n
        m.append(month)
        d.append(day)
        y.append(year)
    
    # regex for date in format YYYY/MM/DD
    bDateReg = re.compile(r'''
            (19\d{2}|20[01][0-9]|2020)
            [-/.]
            (0?[1-9]|1[012])
            [-/.]
            (0[1-9]|[12][0-9]|3[01])
            \b''', re.VERBOSE)
    
    mo1 = bDateReg.findall(text)
    
    for t in mo1:
        year1, month1, day1 = t
        m.append(month1)
        d.append(day1)
        y.append(year1)
    
    m1 = ['0' + i if i in '1 2 3 4 5 6 7 8 9' else i for i in m]
    d1 = ['0' + i if i in '1 2 3 4 5 6 7 8 9' else i for i in d]
    
    for x in range(len(d1)):
        print(f'{d1[x]}.{m1[x]}.{y[x]}')
    
dateCleanUp(string)
