import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumberRegex.search('My number is 415-555-4242 and 321-234-4363.')
print('Phone number found: ' + mo.group())