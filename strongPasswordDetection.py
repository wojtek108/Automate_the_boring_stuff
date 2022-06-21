def strong_password(string):
    import re

    regex01 = re.compile(r'[a-z]')
    mo1 = regex01.search(string)

    regex02 = re.compile(r'[A-Z]')
    mo2 = regex02.search(string)

    regex03 = re.compile(r'\d')
    mo3 = regex03.search(string)

    if mo1 and mo2 and mo3 and len(string) > 7:
        print('strong password')
    else:
        print('weak password')

testPassword = input('Give me a password to test: ')
strong_password(testPassword)
