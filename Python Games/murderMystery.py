# Starting round
from random import *
import time

class character:
  def __init__(self, name):
    self.good = True
    self.alive = True
    self.name = name
    self.spec = "Citizen"
    self.vinno = 0
    self.reverse = True
    self.investigated = False
  
  def evil(self):
    self.good = False
  
  def killed(self):
    self.alive = False

  def morals(self):
    return self.good

  def isAlive(self):
    return self.alive

  def id(self):
    return self.name
  
  def ability(self, insert):
    self.spec = insert
  
  def role(self):
    return self.spec

  # if this number is 0, then the role of this person is unknown, if it is 1 they are a confirmed inno, if it is 2 they are confirmed evil
  def exposed(self, num):
    self.vinno = num
  
  def target(self):
    return self.vinno
  
  def perm(self):
    self.reverse = False

  def cantheybesaved(self):
    return self.reverse
  
  def revive(self):
    self.alive = True
  
  def invest(self):
    self.investigated = True
    
  def checked(self):
    return self.investigated



#spawn 10 random characters



special = input("Do you want to 100% have a special role? 1] yes 2] no ")
while True:
    full_cast = []

    me = character("You")
    full_cast.append(me)
    red = character("RED")
    full_cast.append(red)
    green = character("GREEN")
    full_cast.append(green)
    blue = character("BLUE")
    full_cast.append(blue)
    purple = character("PURPLE")
    full_cast.append(purple)
    black = character("BLACK")
    full_cast.append(black)
    white = character("WHITE")
    full_cast.append(white)
    yellow = character("YELLOW")
    full_cast.append(yellow)
    brown = character("BROWN")
    full_cast.append(brown)
    cyan = character("CYAN")
    full_cast.append(cyan)


    # select two murderers at random
    lst = list(range(0,10))
    shuffle(lst)
    x = lst[0]
    y = lst[1]

    full_cast[x].evil()
    full_cast[x].ability("Murderer")
    full_cast[y].evil()
    full_cast[y].ability("Murderer")
    murder1 = x
    murder2 = y




    #assign detective
    a = lst[2]

    full_cast[a].ability("Detective")

    #assign doc
    b = lst[3]

    full_cast[b].ability("Doctor")

    #assign ninja
    c = lst[4]

    full_cast[c].ability("Detective")

    if (special != "1" or (x == 0 or y == 0 or c == 0 or b == 0 or a == 0) ): break


active = ["1] red", "2] green" , "3] blue", "4] purple" , "5] black" , "6] white" , "7] yellow" , "8] brown" , "9] cyan",  "0] Noone"]
activev2 = ["You", "red", "green" , "blue", "purple" , "black" , "white" , "yellow" , "brown" , "cyan"]
for x in full_cast:
  print(x.role())
        


# murderer?
def murder():
  #while ur evil and alive, select to kill someone
  while True:
    if (me.morals() == False and me.cantheybesaved()):
      print(active)
      ded = input("Choose to kill someone: ")
      time.sleep(2)
      print("Assasinating...")
      time.sleep(2)
      ded = int(ded)
      if (full_cast[ded].morals() == True and full_cast[ded].isAlive() == True):
        full_cast[ded].killed()
        break
      else:
        print("You have attempted to kill someone who is either already dead or is a fellow murderer. Please Choose another victim")
        time.sleep(2)
    elif (full_cast[murder1].cantheybesaved() == True or full_cast[murder2].cantheybesaved() == True):
      continuing = True
      for x in full_cast:
        if (x.target() == 1 and x.isAlive() == True):
          x.killed()
          continuing = False
          break
      while continuing:
        vict = randint(0,9)
        if (full_cast[vict].morals() == True and full_cast[vict].isAlive() == True):
          full_cast[vict].killed()
          break
        vict = randint(0,9)
      break
    else:
      break





#Doctor?
def doctor():
  while True:
    if (me.role() == "Doctor" and me.cantheybesaved()):
      print(active)
      ded = input("Choose to heal someone: ")
      time.sleep(2)
      print("Healing...")
      time.sleep(2)
      ded = int(ded)
      if (full_cast[ded].cantheybesaved() == True):
        full_cast[ded].revive()
        break
      else:
        print("You have attempted to heal someone who is already dead. Please Choose another player")
        time.sleep(2)
    elif (full_cast[b].cantheybesaved() == True):
      for x in full_cast:
        if (x.target() == 1 and x.cantheybesaved() == True):
          prob = randint(1,3)
          if (prob == 1):
            x.revive()
          break
      while True:
        vict = randint(0,9)
        if (full_cast[vict].cantheybesaved() == True):
          full_cast[vict].revive()
          break
        vict = randint(0,9)
      break
    else:
      break



#Detective?
def detective():
  while True:
    if (me.role() == "Detective" and me.isAlive()):
      print(active)
      ded = input("Choose to investigate someone: ")
      time.sleep(2)
      print("Investigating...")
      time.sleep(2)
      ded = int(ded)


      if (full_cast[ded].cantheybesaved() == True):
        if (full_cast[ded].morals() == False):
          print("The person you have investigated is evil")
          time.sleep(2)
          risk = input("Would you like to reveal this information to the public? WARNING THE MURDERERS WILL TARGET YOU. 1] Yes 2] No ")
          risk = int(risk)
          biscuit = 0
          for x in full_cast:
            if (x.role() == "Murderer" and x.cantheybesaved() == False):
              biscuit += 1 
          if (risk == 1 or biscuit == 1):
            full_cast[ded].exposed(2)
            me.exposed(1)
        else:
          print("The person you have investigated is innocent.")
        break
      else:
        print("You have attempted to investigate someone who is already dead. Please Choose another player")
        time.sleep(2)
    else:
      break

  if (full_cast[a].isAlive() and a != 0 and a != c):
    pick = [0,1,2,3,4,5,6,7,8,9]
    shuffle(pick)
    for x in pick:
      if (detective_tracker[x] == 0):
        break
    if (full_cast[x].morals() == False):
      risk = randint(1,2)
      biscuit = 0
      for y in full_cast:
        if (y.role() == "Murderer" and y.cantheybesaved() == False):
          biscuit += 1
      if (risk == 1 or biscuit == 1):
        full_cast[x].exposed(2)
        full_cast[a].exposed(1)
      else:
        full_cast[x].invest()
        detective_tracker[x] += 1

  if (full_cast[c].isAlive() and c != 0 and c != a):
    pick = [0,1,2,3,4,5,6,7,8,9]
    shuffle(pick)
    for x in pick:
      if (detective_tracker[x] == 0):
        break
    if (full_cast[x].morals() == False):
      risk = randint(1,2)
      biscuit = 0
      for y in full_cast:
        if (y.role() == "Murderer" and y.cantheybesaved() == False):
          biscuit += 1
      if (risk == 1 or biscuit == 1):
        full_cast[x].exposed(2)
        full_cast[c].exposed(1)
 
      else:
        full_cast[x].invest()
        detective_tracker[x] += 1



# Game Center
#ANNOUNCE ROLES

def main():

    if (me.role() == "Detective"):
    print("You are the Detective (innocent)")
    if (me.role() == "Doctor"):
    print("You are the Doctor (innocent)")
    if (me.role() == "Citizen"):
    print("You are a citizen (innocent)")
    if (me.role() == "Murderer"):
    print("You are a Murderer (evil)")
    for x in range(1,9):
        if (full_cast[x].morals() == False):
        broski = full_cast[x]
        print("Your fellow Murderer is " + full_cast[x].id())
    time.sleep(3)
    print()
    print("------------------------------------------------------------------------------------------------")
    print()

    tracker = 0
    detective_tracker = [0,0,0,0,0,0,0,0,0,0] # if 1 they dead or have been invested, 0 no one knows
    day = 1

    while True:
    print("-----------------------------------------------NIGHT TIME------------------------------------------------")
    print()
    print()
    time.sleep(3)
    print("The sun sets...")
    time.sleep(2)
    print()
    print("Something doesn't feel right.")
    print()
    time.sleep(2)
    if (me.role() == "Citizen"):
        print("Standby...")
        time.sleep(3.5)

    murder()
    doctor()
    detective()
    
    print("The sun rises...")
    print()
    time.sleep(1.5)
    print("-----------------------------------------------DAY " + str(day) + "------------------------------------------------")
    time.sleep(2.5)
    print()
    print()
    wasthereevenamurder = 0
    print("MAYOR: Good Morning Citizens.")
    print()
    time.sleep(1.5)
    print("MAYOR: We have some information regarding a murder that has taken place.")
    time.sleep(2)
    print()
    for x in full_cast:
        if (x.isAlive() == False and x.cantheybesaved()):
        wasthereevenamurder += 1
        print("MAYOR: " + x.id() + " was murdered last night.")
        print()
        time.sleep(1.75)
        print("MAYOR: Looking through our data base.")
        print()
        time.sleep(1.75)
        print("MAYOR: Their role was: " + x.role())
        print()
        x.perm()

    if (wasthereevenamurder == 0):
        print("MAYOR. Oh... Pardon me the Police have notified me that there wasn't an actual murder that occured last night")
        print()
        time.sleep(2)
        print("MAYOR: It seems that a DOCTOR was able to revive a patient who was the victim of an ATTEMPTED MURDER!")
    print()
    time.sleep(2)
    print("MAYOR: If anyone has any intel regarding this tragedy. Please speak up")
    print()
    print()
    time.sleep(1.75)

    for x in full_cast:
        if (x.cantheybesaved()== True and x.target() == 1):
        print(x.id() + " has revealed themselves to be a confirmed innocent!")
        print( "Their role is: " + x.role())
        print()
        time.sleep(1.75)
        if (x.cantheybesaved()== True and x.target() == 2):
        print(x.id() + " has been outed to be a confirmed evil!")
        print( "Their role is: " + x.role())
        print()
        time.sleep(1.75)
    aliveMurder = 0
    aliveCitizen = 0
    for x in full_cast:
        if (x.role() == "Murderer" and x.isAlive()):
        aliveMurder += 1
        if (x.cantheybesaved()):
        aliveCitizen += 1 

    if (aliveMurder == 0):
        print()
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print()
        print("THE CITIZENS HAVE WON! ALL MURDERERS HAVE BEEN ELMINATED!!!!")
        time.sleep(2)
        break
    if (aliveMurder *2 >= aliveCitizen):
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print()
        print("The Murderers have won...")
        time.sleep(2)
        print("Congratulations...")
        time.sleep(1.4)
        print()
        winners=[]
        for x in full_cast:
        if (x.role() == "Murderer"):
            winners.append(x.id())
        
        print(winners[1])
        print('&')
        print(winners[0])
        break
    time.sleep(2)
    print("MAYOR: Thank you all for those who have spoken up. The town will now vote out suspected killers.")
    time.sleep(2)
    print()
    anyone = 0
    for x in full_cast:
        if (x.isAlive()== True and x.target() == 2):
        print("The Town has came to a decison")
        print()
        time.sleep(2)
        print("The Town has choosen to execute " + x.id())
        print()
        time.sleep(2)
        x.killed()
        print(x.id() + " was killed...")
        time.sleep(1.5)
        print()
        x.perm()
        print( "Their role was: " + x.role())
        print()
        time.sleep(2)
        anyone += 1
        tracker = 0
    if (anyone == 0 and tracker % 2 == 0):
        print("The Town has came to a decison")
        print()
        time.sleep(2)
        while True:
        randolol = randint(0,9)
        if (full_cast[randolol].cantheybesaved() and full_cast[randolol].target != 2):
            break
        randolol = randint(0,9)
        print("The Town has choosen to execute " + full_cast[randolol].id())
        print()
        time.sleep(2) 
        print("MAYOR: I'm so sorry to have to do this to you " + full_cast[randolol].id())
        time.sleep(2) 
        print()     
        print("MAYOR: We just dont have enough info and I really wanna wrap this up.")
        time.sleep(2)
        print()
        if (full_cast[randolol].id() == "ck" and full_cast[randolol].role() != "Murderer" and full_cast[randolol].role() != "Citizen"):
        reveal = input("YOU ARE ABOUT TO BE EXCECUTED! Will you reveal your role to save yourself? 1] Yes 2] No")
        reveal = int(reveal)
        if (reveal == 1):
            print(full_cast[randolol].id() + " has revealed themselves to be a confirmed innocent!")
            time.sleep(2)
            print( "Their role is: " + full_cast[randolol].role())
            print()
            full_cast[randolol].exposed(1)
            print("MAYOR: Oh. My Apologies...")
        else:
            print("MAYOR: bye. bye.")
            print()
            full_cast[randolol].killed()
            full_cast[randolol].perm()
            time.sleep(1.5)
            print(full_cast[randolol].id() + " was killed...")
            time.sleep(2)
            print()
            print( "Their role was: " + full_cast[randolol].role())
        elif (full_cast[randolol].role() != "Murderer" and full_cast[randolol].role() != "Citizen"):
        print(full_cast[randolol].id() + " has revealed themselves to be a confirmed innocent!")
        time.sleep(2)
        print( "Their role is: " + full_cast[randolol].role())
        print()
        full_cast[randolol].exposed(1)
        print("MAYOR: Oh. My Apologies...")
        else: 
        print("MAYOR: bye. bye.")
        print()
        full_cast[randolol].killed()
        full_cast[randolol].perm()
        time.sleep(1.5)
        print(full_cast[randolol].id() + " was killed...")
        time.sleep(2) 
        print( "Their role is: " + full_cast[randolol].role())
    aliveMurder = 0
    aliveCitizen = 0
    for x in full_cast:
        if (x.role() == "Murderer" and x.isAlive()):
        aliveMurder += 1
        if (x.cantheybesaved()):
        aliveCitizen += 1 

    if (aliveMurder == 0):
        print()
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print()
        print("THE CITIZENS HAVE WON! ALL MURDERERS HAVE BEEN ELMINATED!!!!")

        time.sleep(2)
        break
    if (aliveMurder *2 >= aliveCitizen):
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------")
        print()
        print("The Murderers have won...")
        time.sleep(2)
        print("Congratulations...")
        time.sleep(1.4)
        print()
        winners=[]
        for x in full_cast:
        if (x.role() == "Murderer"):
            winners.append(x.id())
        
        print(winners[1])
        print('&')
        print(winners[0])
        break


        print()
        print()
        time.sleep(2.5)
    if (anyone == 0 and tracker % 2 != 0):
        print("The Town has came to a decison")
        print()
        time.sleep(2)
        print("MAYOR: We will wait till tomorrow to make an execution")
        print()
        time.sleep(2)
        print("MAYOR: MURDERERS beware...")
        time.sleep(2.5)

    tracker += 1  
    for x in range(1,10):
        if (full_cast[x].isAlive() == False):
        active[x-1] = "DEAD"
        activev2[x] = "DEAD"
        if (detective_tracker[x] == 0):
            detective_tracker[x]+=1
    print("Here are the remaining...")
    print(activev2)
    print()
    time.sleep(1)
    print("There are still murderers amoung us...")
    print()
    print()
    time.sleep(2)
    day += 1


    print()
    print()
    print("The end.")


if __name__ == "__main__": main()
