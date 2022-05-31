import random 
import time

spaces = []
q = 0
for x in range(10): 
  for y in range(10): 
    spaces.append((x,y))
random.shuffle(spaces)

ships = []
shipsPlay = []
numAsStr = [str(x) for x in range(1,11)]
alpha = ["A","B","C","D","E","F","G","H","I","J"]
grid = [[0 for x in range(10)] for x in range(10)]

gridPlay = [[0 for x in range(10)] for x in range(10)]

#0 = empty
#1 = ship
#-1 = hit
# 5 = miss

def compAlg():
  compAtk(spaces[0][0],spaces[0][1])

def compAtk(x,y):
  print("Computer Attacks: "+alpha[x]+numAsStr[y])
  time.sleep(2)
  if gridPlay[x][y] == 0:
    print("Computer MISS")
    gridPlay[x][y] = 5

  if gridPlay[x][y] == 1:
    print("HIT")
    for indx in range(len(shipsPlay)):
      if ((x,y) in shipsPlay[indx]):
        shipsPlay[indx].remove((x,y))
        if (len(shipsPlay[indx]) == 0):
          time.sleep(2)
          print("SHIP DESTROYED!!!")
          shipsPlay.pop(indx)
  
    gridPlay[x][y] = -1
  print()

def isEmpty(x,y,grid):
  if x > 9 or x < 0 or y > 9 or y < 0:
    return False
  if(grid[x][y] != 0):
    return False
  
  return True


def place(lst,grid,ships):
  for x,y in lst:
    grid[x][y] = 1
  ships.append(lst)

def randPos(grid,length,ships):
  origin = length
  while(True):
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

    if (upOrSide == 0):
      while(length != 0):
        if(isEmpty(a-1,b,grid)):
          a = a-1
          used.append((a,b))
          length -= 1
        else: 
          break

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

    if(length == 0):
      place(used,grid,ships)
      return
    
        






  

def depict(grid,cheater = False):
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
        indicate = "&"
      if (space == -1):
        indicate = "X"
      if (space == 5):
        indicate = "0"
      
    
      print("| "+indicate,end=" ")
    print("|")
  print(border)
  
    
def checkValid(coord):
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
  if grid[x][y] == 0:
    print("MISS")
    grid[x][y] = 5
  
  if grid[x][y] == 1:
    print("HIT")
    for indx in range(len(ships)):
      if ((x,y) in ships[indx]):
        ships[indx].remove((x,y))
        if (len(ships[indx]) == 0):
          time.sleep(2)
          print("SHIP DESTROYED!!!")
          ships.pop(indx)
        
    grid[x][y] = -1
  print()




def playerPlace(num):
  allowed = [5,4,3,3,2]
  while(num != 0):
    pos = input("Enter the start and end position of your ship (EX: A1 A4 or random): ")
    if (pos == "random"):
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
        start,end = pos.split(" ")
        x0, y0 = checkValid(start)
        x1, y1 = checkValid(end)
        if (abs(y0 - y1)+1 not in allowed and abs(x1-x0)+1 not in allowed):
            raise Exception
        else:
            try:
                allowed.remove(abs(y0 - y1)+1)
            except Exception:
                allowed.remove(abs(x0 - x1)+1)


        if(x0-x1 == 0):

          if(y0-y1 < 0):
            for step in range(y0,y1+1):
              if(not isEmpty(x0,step,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((x0,step))

          else:
            for step in range(y0,y1-1,-1):
              if(not isEmpty(x0,step,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((x0,step))
          

        if(y0-y1 == 0):
          
          if(x0-x1 < 0):
            for step in range(x0,x1+1):
              if(not isEmpty(step,y0,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((step,y0))

          else:
            for step in range(x0,x1-1,-1):
              if(not isEmpty(step,y0,gridPlay)):
                print("Error: Space Occupied")
                num+=1
                break
              ship.append((step,y0))


        place(ship,gridPlay,shipsPlay)
        num -= 1
        depict(gridPlay,True)
        shipsPlay.append(ship)


      except Exception: 
        print("Error: Invalid Input")

def depictPlayShip():
  a = 1
  for ship in shipsPlay:
    print("Ship " + str(a) + ":",len(ship),end = " | ")
    a+=1

  print()
  


def main():
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
    compAlg()
    spaces.pop(0)
    print()
    depictPlayShip()

    if (len(shipsPlay) == 0):
      print("YOU LOSE!!!!")
      time.sleep(2)
      print("HAHA")
      break




if __name__ == "__main__":
    main()

