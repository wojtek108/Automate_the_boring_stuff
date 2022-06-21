def dateDetection(userDate):
    import re

    DateReg = re.compile(r'''
            (0[1-9]|[12][0-9]|3[01])
            [./-]
            (0[1-9]|1[012])
            [./-]
            ([1\d\d\d|20\d\d]+)
            \b''', re.VERBOSE)

    mo = DateReg.findall(userDate)

    if not mo:
        print('no date in the string')

    for t in mo:
        day, month, year = t
        if month in ['04', '06', '09', '11'] and int(day) > 30:
            print('Wrong date')
        elif int(year) % 4 != 0 and month == '02' and int(day) > 28:
            print('Wrong number of days in Feb')
        elif (int(year) % 4 == 0 and int(year) % 100 != 0 
                and month == '02' and int(day) > 29):
            print('Wrong number of days in Feb in a leap year')
        elif int(year) % 400 == 0 and month == '02' and int(day) > 29:
            print('Wrong number of days in Feb in a leap year')
        else:
            print('date ok')

        

text = input('Give me a date in format DD/MM/YYYY:\n')
dateDetection(text)
