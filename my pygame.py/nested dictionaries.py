all_guests ={'bob':{'apples':2,'sanddwiches':5}, 'ronnie':{'apple piles':5, 'mangoes ':5},'joan':{'oranges':3,'avoado':6}}
def total_items(guests, items):
    numBought= 0
    for k, v in guests.items():
      numBought = numBought + v.get(items, 0)
    return numBought
print('number of items being bought')
print('cakes '+ str(total_items(all_guests, 'cakes')))
print('apples'+str(total_items(all_guests, 'apples')))
print('mangoes'+str(total_items(all_guests, 'mangoes')))