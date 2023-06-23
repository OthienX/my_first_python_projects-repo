import re
phoneNumregex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo =phoneNumregex.search('is 232-232-4556 my phone number')
#print('phonenumber found:' +mo.group())
print(mo.group(1))
print(mo.groups())
areacode, mainnumber = mo.groups()
print(areacode)
print(mainnumber)