def isphone_number(TEXT):
    if len(TEXT) != 12:
        return False
    for i in range(0, 3):
        if not TEXT[i].isdecimal():
            return False
    if TEXT[3] !='-':
        return False
    for i in range(4,7):
        if not TEXT[i].isdecimal():
            return False
    if TEXT[7] != '-':
        return False
    for i in range(8,12):
        if not TEXT[i].isdecimal():
            return False
    return True

message = 'call me at 433-322-4221 tomorrow! 232-243-3242 is my personal number'
for i in range(len(message)):
    chuck = message[i:i+12]
if isphone_number(chuck):
       print('my number is found '+ chuck)
print("ITS DONE")

