def regex_strip(string, key):
    import re

    if key == '':
        # how to read this regex?
        regex7 = re.compile(r'(?s:.*)\S')
        mo1 = regex7.search(string)
        start, end = mo1.span()
        regex5 = re.compile(r'\S')
        mo = regex5.search(string)
        s = string.index(mo.group())
        print('\n1st way:')
        print(string[s:end])
        
        xl = []
        for i, k in enumerate(string):
            if not re.search('\s', k):
                xl.append(i)
        print('\n2nd way')
        print(string[xl[0]:int(xl[-1])+1])

        regex6 = re.compile(r'(^\s+)?(.*)(\s+$)?')
        pr = re.search(regex6, string)
        print('\n3ed way')
        print(pr.group(2))

    elif key != '':
        print(f'\nString stripped of the {key} character:')
        regex4 = re.compile(key)
        list2 = [n for n in string if not re.search(regex4, n)]
        list3 = [n for n in string if n != key]
        print('\n1st way:')
        print(''.join(list2))
        print('\n2nd way')
        print(''.join(list3))



userString = input('Give me a string:\n')
char = input('Give me a character: ')

regex_strip(userString, char)
