import re
#regrex = re.compile('^.{10}$')
#othieno = regrex.search('535353')
#print(othieno)
#pattern = re.compile('^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-z]{0,2}$')
#print(pattern.search('ahdhdkldld2314'))
#print(pattern.search('cid.eis242'))
#print(pattern.search('45252.543.'))
#print(pattern.search('33152363#'))
#pattern = re.compile(r'^A-Z+$')
#print(pattern.search('hello world '))
#print(pattern.search('HELLOWORLD'))
#print(pattern.search('HELLOWORLD'))
pattern = re.compile('^[a-zA-z0-9\._]1}[a-zA-z0-9]+\.{1}[a-zA-Z]{2-3}$')
print(pattern.search('thienoronnie7@gmail.com))