bds ={'bod': '2rd april', 'anna':'3rd july'}
while True:
    print('ente your name (to quit )')
    name = input()
    if name == '':
        break
    if name in bds:
        print(bds[name] + ' is the bd of ' + name)
    else:
        print('i dont have bd information of ' + name)
        print('wats your bd' +name)
        bd = input()
        bds[name] = bd
        print('bd data base update')


