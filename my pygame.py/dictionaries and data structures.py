#spam = {'name':'ronnie', 'age':'20'}
#spam.setdefault('color', 'black')
#print(spam)
#print('how many metres are   there'+ str(spam.get('age', 0))+'are there you now make ur order')
# alternatively
#spam = {'name':'ronnie', 'age':'20'}
#if 'colour ' not in spam:
 #   spam['color'] ='black'
  #  print(spam)
import pprint
message = 'hey, There how  are you doing'
count={}
for charcter in message:
    count.setdefault(charcter, 0)
    count[charcter] =count[charcter]+1
    #pprint.pprint(count)
    print(pprint.pformat(count))

