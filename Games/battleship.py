import random 
import time


#This program simulates the battleship game against a bot


#initalize random guessing strategy
#will guess in a checker pattern (unless it hits somthing)
spaces = []
spaces2 = []
q = 0

swap = True
for x in range(10): 
  for y in range(10): 
    if (swap): 
      if (y%2==0): spaces.append((x,y))
      else: spaces2.append((x,y))
    else:
      if (y%2==1): spaces.append((x,y))
      else: spaces2.append((x,y))
  swap = not swap
random.shuffle(spaces)
random.shuffle(spaces2)
spaces += spaces2

#spaces is list containing the order the computer will guess assuming it does not hit anything


#initalize grid and ship list for player and computer
ships = []
shipsPlay = []
numAsStr = [str(x) for x in range(1,11)]
alpha = ["A","B","C","D","E","F","G","H","I","J"]
grid = [[0 for x in range(10)] for x in range(10)]

#clear grid
def clear(grid):
  """
  Clears grid
  
  :param list grid: grid to be set to all zeros
  :return: None
  """
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      grid[i][j]= 0


gridPlay = [[0 for x in range(10)] for x in range(10)]
#0 = empty
#1 = ship
#-1 = hit
# 5 = miss

#for computer
def canAtk(x,y):
  """
  Lets computer know if it can attack a position on the grid
  
  :param int x: x coordinate position on the grid
  :param int y: y coordinate position on the grid
  :return: if computer can attack a square (which is in bounds, and not already attacked previously)
  :rtype: bool
  """
  return ((x,y) in spaces)


def compAlg(point):
  """
  Part of computer strategy to attack player's grid. 

  :param tuple or None point: specific position to attack on player's grid or if None, attack randomly
  :return: coded result of compAtk() function and the x and y coordinate points of the space hit
  :rtype: tuple
  """
  if point: 
    return compAtk(point[0],point[1]), point[0],point[1]
  else:
    return compAtk(spaces[0][0],spaces[0][1]), spaces[0][0],spaces[0][1]
    



def compAtk(x,y):
  """
  Computer Attacks specific coordinate point of player's grid 

  :param int x: x coordinate position on the grid
  :param int y: y coordinate position on the grid
  :return: coded result of strike (5 = miss, 10 = ship sunk, 1 = hit)
  :rtype: int
  """

  print("Computer Attacks: "+alpha[x]+numAsStr[y])
  time.sleep(2)
  if gridPlay[x][y] == 0:
    print("Computer MISS")
    gridPlay[x][y] = 5
    return 5

  if gridPlay[x][y] == 1:
    print("Computer HIT")
    gridPlay[x][y] = -1
    
  
    for indx in range(len(shipsPlay)):

      if ((x,y) in shipsPlay[indx]):
        shipsPlay[indx].remove((x,y))

        if (len(shipsPlay[indx]) == 0):
          time.sleep(2)
          print("SHIP DESTROYED!!!")
          shipsPlay.pop(indx)
          
          
          return 10
    
        return 1


def isEmpty(x,y,grid):
  """
  Checks if grid spot is empty

  :param int x: x coordinate position on the grid
  :param int y: y coordinate position on the grid
  :param list grid: the grid itself 
  :return: if grid[x][y] is empty
  :rtype: bool
  """
  if x > 9 or x < 0 or y > 9 or y < 0: return False
  return (grid[x][y] == 0)
  


def place(lst,grid,ships):
  """
  Places list of coordinate positions on a grid as ships

  :param list lst: contains coordinate positions tuples of ship locations
  :param list grid: grid for ships to be placed on
  :param list ships: list of a list of coordinate point tuples that have the location of the ships
  :return: None
  """
  for x,y in lst:
    grid[x][y] = 1
  ships.append(lst)

def randPos(grid,length,ships):
  """
  Randomly place ships on a grid

  :param list grid: grid for ships to be placed on
  :param int length: length of the ship
  :param list ships: list of a list of coordinate point tuples that have the location of the ships
  :return: None
  """

  origin = length
  while(True):
    #continue to randomly generate until a good mid point has been found
    length = origin
    used = []
    a = random.randint(0,9)
    b = random.randint(0,9)
    mid = grid[a][b]

    while (mid != 0):
      a = random.randint(0,9)
      b = random.randint(0,9)
      mid = grid[a][b]
    upOrSide = random.randint(0,1)
    used.append((a,b))

    length -= 1

    #if cannot traverse the total length from the mid point, choose another mid point
    #each if-statement does this

    if (upOrSide == 0):
      while(length != 0):
        if(isEmpty(a-1,b,grid)):
          a = a-1
          used.append((a,b))
          length -= 1
        else: 
          break

    #break if all spots were filled
    if(length == 0):
      place(used,grid,ships)
      return

    if (upOrSide == 1):
      while(length != 0):
        if(isEmpty(a,b-1,grid)):
          b = b-1
          used.append((a,b))
          length -= 1
        else: 
          break
    
    #break if all spots were filled
    if(length == 0):
      place(used,grid,ships)
      return
    
        

def depict(grid,cheater = False):
  """
  Prints grid in to output

  :param list grid: grid to be depicted
  :param bool cheater: if user should see opponents ship placement
  :return: None
  """

  print("  ",end="")
  [print("  "+str(x)+" ",end="") for x in range(1,11)]
  print()
  a = 0

  border = "  "+"---"*13 + "--"
  for row in grid:
    print(border)
    print(alpha[a],end=" ")
    a+=1
    for space in row:
      indicate = " "
      if (cheater and space == 1):
        indicate = "&" #shows positio of a ship part
      if (space == -1):
        indicate = "X" #shows hit marker
      if (space == 5):
        indicate = "0" #show miss marker
      
    
      print("| "+indicate,end=" ")
    print("|")
  print(border)
  
    
def checkValid(coord):
  """
  Determines if a coordinate point entered as a letter and a number is a valid 

  :param str coord: coordinate position
  :return: if there is an invalid input it will return -1. Else, it will return the coordinate position as a tuple on the actual grid
  :rtype: int or tuple
  """

  if (len(coord) == 0): 
    print("Error: Invalid Input")
    return -1
  if (coord[0] not in alpha): 
    print("Error: Invalid Input")
    return -1
  
  if (coord[1:] not in numAsStr): 
    print("Error: Invalid Input")
    return -1
  
  x = alpha.index(coord[0])
  y = int(coord[1:]) - 1


  if(grid[x][y] == -1 or grid[x][y] == 5):
    print("Error: Position has already been attacked")
    return -1


  return (x,y)

        
def atk(x,y):
  """
  Attacks the computer's grid at a specific coordinate position

  :param int x: x coordinate position on the grid to attack
  :param int y: y coordinate position on the grid to attack
  :return: None
  """
  if grid[x][y] == 0:
    print("MISS")
    grid[x][y] = 5
  
  if grid[x][y] == 1:
    print("HIT")

    #check which ship index was destroyed
    for indx in range(len(ships)):
      
      if ((x,y) in ships[indx]):
        ships[indx].remove((x,y))

        if (len(ships[indx]) == 0):
          time.sleep(2)
          print("SHIP DESTROYED!!!")
          ships.pop(indx)
          grid[x][y] = -1
          return
        
    grid[x][y] = -1
  print()




def playerPlace(num):
  """
  Prompts user to input coordinate positions of their ships.

  :param int num: how many ships the player can have
  :return: None
  """
  allowed = [5,4,3,3,2]
  while(num != 0):
    pos = input("Enter the start and end position of your ship (EX: A1 A4 or random): ")
    
    if (pos == "random"): #if they choose random place ships randomly
      clear(gridPlay)
      shipsPlay.clear()
      randPos(gridPlay,5,shipsPlay)
      randPos(gridPlay,4,shipsPlay)
      randPos(gridPlay,3,shipsPlay)
      randPos(gridPlay,3,shipsPlay)
      randPos(gridPlay,2,shipsPlay)
      depict(gridPlay,True)
      num = 0
    else:
      try:
        ship = []
        #ensure coordinate points are valid and are of allowed length
        start,end = pos.split(" ")
        x0, y0 = checkValid(start)
        x1, y1 = checkValid(end)
        if (abs(y0 - y1)+1 not in allowed and abs(x1-x0)+1 not in allowed):
            raise Exception
        else:
            #if they are allowed length removed that length from allowed
            try:
                allowed.remove(abs(y0 - y1)+1)
            except Exception:
                allowed.remove(abs(x0 - x1)+1)


        #ensure those spaces between coordinate 1 and 2 are unoccupied
        if(x0-x1 == 0):
        
          if(y0-y1 < 0):
            #check each coordinate point
            for step in range(y0,y1+1):

              if(not isEmpty(x0,step,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break

              ship.append((x0,step))

          else:
            #check each coordinate point
            for step in range(y0,y1-1,-1):
              
              if(not isEmpty(x0,step,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((x0,step))
          

        if(y0-y1 == 0):
          
          if(x0-x1 < 0):
            #check each coordinate point
            for step in range(x0,x1+1):

              if(not isEmpty(step,y0,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((step,y0))

          else:
            #check each coordinate point
            for step in range(x0,x1-1,-1):
              
              if(not isEmpty(step,y0,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((step,y0))


        #if no issues, place the ships
        place(ship,gridPlay,shipsPlay)
        num -= 1
        depict(gridPlay,True)
        shipsPlay.append(ship)


      except Exception: #if something was wrong above, probably bad input from user
        print("Error: Invalid Input")


#Prints lives of each of the player's ships to output
def depictPlayShip():
  a = 1
  for ship in shipsPlay:
    print("Ship " + str(a) + ":",len(ship),end = " | ")
    a+=1

  print()
  


def main():

  #generate random position for computer
  randPos(grid,5,ships)
  randPos(grid,4,ships)
  randPos(grid,3,ships)
  randPos(grid,3,ships)
  randPos(grid,2,ships)
  cheater = False
  print("WELCOME TO BATTLE SHIP")
  time.sleep(2)

  print("YOUR BOARD")
  depict(gridPlay,True)
  playerPlace(5)
  time.sleep(2)

  toAtk = []
  indx = 0


  while(len(ships) != 0):

    print()
    print()
    depict(grid,cheater)
    guess = input("Enter a coordinate postion to attack: ")

    if (guess == "cheat"): cheater = True
    pos = checkValid(guess)
    while(pos == -1):
      guess = input("Enter a coordinate postion to attack: ")
      if (guess == "cheat"): cheater = True
      pos = checkValid(guess)
    
    x, y = pos 
    print()
    time.sleep(1)
    atk(x,y)
    time.sleep(2)
    depict(grid,cheater)
    print()
    print()

    if (len(ships) == 0):
      print("YOU WIN!!!!")
      time.sleep(2)
      break
    time.sleep(2)


    #computer strat

    point = None
    #toAtk will have list of nearby points to attack next turn
    if toAtk != []:
      point = toAtk[0][indx]
      spaces.remove(point)
      result,x,y = compAlg(point)
    else:
      result,x,y = compAlg(point)
      spaces.pop(0)
    
    #if ship has sunk, return back to random guessing
    if result == 10:
      toAtk = []
      indx = 0

    #if hit and toAtk is empty, populate toAtk with legal coordinate positions to the left, right, above and below
    elif result == 1 and toAtk == []:
      right, left, top, bottom = [], [], [], []
      for i in range(x+1,10):
        if canAtk(i,y): right.append((i,y))
        else: break
      
      if len(right) != 0: toAtk.append(right)
      for i in range(x-1,-1,-1):
        if canAtk(i,y): left.append((i,y))
        else: break
      if len(left) != 0: 
        toAtk.append(left)
      
      for i in range(y+1,10):
        if canAtk(x,i): bottom.append((x,i))
        else: break
      if len(bottom) != 0: toAtk.append(bottom)
      for i in range(y-1,-1,-1):
        if canAtk(x,i): top.append((x,i))
        else: break
      if len(top) != 0: 
        toAtk.append(top)
      
      #print(toAtk)
 

    
    #if it hits keep attacking in that direction
    elif result == 1 and toAtk != []:
      indx+= 1
      if indx >= len(toAtk[0]):
        toAtk.pop(0)
        indx = 0

    #if misses stop attacking in that direction and go a different way
    elif result == 5 and toAtk != []:
      toAtk.pop(0)
      indx = 0
    


    
    print()
    depictPlayShip()

    if (len(shipsPlay) == 0):
      print("YOU LOSE!!!!")
      time.sleep(2)
      print("HAHA")
      break
  




if __name__ == "__main__":
    main()

