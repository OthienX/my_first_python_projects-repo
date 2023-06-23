#conways gameof life
import random, time, copy
WIDTH = 60
HEIGHT =20
#create a list of list of the cells
nextcells =[]
for x in range(WIDTH):
    column = [] #creating of a new column
    for y in range[HEIGHT]:
        if random.randint(0 ,1) ==0:
            column.append('#') # add a living cell
        else:
            column.append('')# add a living cell
nextcells.append(column) #nexcell is alisty of  column lists.
while True: # main program loop
    print('\n\n\n\n\n\n\n\n\n') #seperating each step with a newline
    currentcells =copy.deepcopy(nextcells)
#print the cuurent cell on the screen
for y in range(WIDTH):
    for y in range(HEIGHT):
#getting the neighboring coordinates
    #% WIDTH ensure leftcord is always between 0 and WIDTH -1
    leftcord = (x-1) %WIDTH
    rightcord =(x+1) %WIDTH
    abovecord  = (y-1)% HEIGHT
    belowcord = (y+1)% HEIGHT
    #count number of living neighboring
    numNeighbour =0
    if currentcells[leftcord][abovecord]=='#':
      numNeighbour +=1 #top_left neighbour is alive.
    if currentcells[x][abovecord]=='#':
       numNeighbour +=1 #top_neighbor is alive.
    if currentcells[rightcord][abovecord]=='#':
        numNeighbour +=1 #top_right neighbor is alive.
    if currentcells[leftcord][y] =='#':
        numNeighbour +=1 #left neighbour is alive.
    if currentcell[rightcord][y] =='#':
         numNeighbour +=1 # right neighbour is alive.
    if currentcells [leftcord][belowcord]=='#':
        numNeighbour +=1 #bottom-left neighbor is alive.
    if currentcells[x][bottomcord]=='#':
         numNeighbour +=1 #bottom neighbour is alive.
    if currentcells[rightcord][belowcord]=='#':
        numNeighbour +=1 #bottom-right neighbour is alive.
#set cells based on conways game of life rules:
    if currentcells[x][y] == '#' and (numNeighbour ==2 or numNeighbour==3):
# livingcells with 2 or 3 neighbors stay alive:
    nextcell[x][y] =='#'
      elif currentcells[x][y] =='' and numNeighbour ==3:
#dead cells with 3 neighbors become alive.
nextcell[x][y] = '#'
     else:
#every thing else dies or stays dead :
nextcells[x][y] =''
time.sleep(1) #add a second pause to reduce flicking
#




