#def hey(something):
    #something.append('hello')
#spam =[1,2,3,4,5,6]
#hey(spam)
#print(spam)
#id(spam)
import copy
rock = [1,2,3,4,5,6,7,8,9]
id(rock)
ronnie = copy.copy(rock)
id(ronnie)
ronnie[3] =10
print(rock)
print(ronnie)

