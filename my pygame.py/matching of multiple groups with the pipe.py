import re

#rocks = re.compile(r'batman| tinafey')
#mo1 =rocks.search('batman and tinefey')
#print(mo1.group())
#mo2 = rocks.search('tinefey and batman' )
#print(mo2.group())
#regex = re.compile(r'bat(wo)*man')
#mo1 = regex.search('the  batman')
#print(mo1)
#mo2  = regex.search('the adventure batwoman')
#print(mo2)
rockstar = re.compile(r'(ha){3,5}')
mo3 = rockstar.search('hahahaha')
print(mo3 )

