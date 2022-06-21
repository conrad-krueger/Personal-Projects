import random as r
from scipy import stats as s
import matplotlib.pyplot as plt
formatting = '''Go
Mediterranean Avenue
Community Chest
Baltic Avenue
Income Tax
Reading Railroad
Oriental Avenue
Chance
Vermont Avenue
Connecticut Avenue
Just Visiting
St. Charles Place
Electric Company
States Avenue
Virginia Avenue
Pennsylvania Railroad
St. James Place
Community Chest
Tennessee Avenue
New York Avenue
Free Parking
Kentucky Avenue
Chance
Indiana Avenue
Illinois Avenue
B. & O. Railroad
Atlantic Avenue
Ventnor Avenue
Water Works
Marvin Gardens
Go To Jail
Pacific Avenue
North Carolina Avenue
Community Chest
Pennsylvania Avenue
Short Line
Chance
Park Place
Luxury Tax
Boardwalk'''
formatting = formatting.split("\n")
names = {}
for x in range(1,41):
    names[x] = formatting[x-1]

names[41] = "Jail"


Aland = [1]
APassGo = 0
chance = [1,25,"U",12,"R","","-3",11,"","",6,40,"","","","R"]
r.shuffle(chance)
CC = [1,"","","","",11,"","","","","","","","","",""]
r.shuffle(CC)
freq = {41:0}

rollInARow = 0
iter = int(input("Enter number of Iterations: "))

for p in range(iter):
    jailed = False
    jmp = False
    #print("Iteration:",p+1)

    #no more chance cards = reshuffle
    if (len(chance) == 0):
        chance = [1,25,"U",12,"R","","-3",11,"","",6,40,"","",""]
        r.shuffle(chance)

    #roll die for player A
    die1 = r.randint(1,6) 
    die2 =  r.randint(1,6)
    A = die1 + die2
    if (die1 == die2):
        rollInARow +=1
    else:
        rollInARow = 0
    
    if rollInARow == 3:
        Aland.append(11)
        freq[41] += 1
        continue


    moveTo = Aland[-1] + A
    if (moveTo > 40): 
        APassGo += 1
        moveTo -= 40

    #locations after rolling 2 dice
    
    Aland.append(moveTo)
    try: freq[moveTo] += 1
    except KeyError: freq[moveTo] = 1

    #Go to Jail
    if (moveTo == 31):
        Aland.append(11)
        jailed = True
        jmp = True

    #land on chance square
    elif (moveTo == 8 or moveTo == 23 or moveTo == 37):
        
        #advance to nearest utility
        if (chance[0] == "U"): 
            jmp = True
            if (moveTo == 23):
                Aland.append(29) #water works
            else:
                Aland.append(13) #electric

        #railroad
        elif (chance[0] == "R"): 
            jmp = True
            if (moveTo == 8): 
                Aland.append(16) #ppenn
            if (moveTo == 23):
                Aland.append(26) #B&O
            if (moveTo == 37):
                Aland.append(6) #read
        
        #move back 3 spaces
        elif (chance[0] == "-3"): 
            jmp = True
            Aland.append(moveTo-3)

        #move to specific places
        elif (type(chance[0]) == int): 
            jmp = True
            Aland.append(chance[0])
            if (chance[0] == 11): jailed = True
        chance.remove(chance[0])

        #reshuffle if no chance cards
        if (len(chance) == 0):
            chance = [1,25,"U",12,"R","","-3",11,"","",6,40,"","",""]
            r.shuffle(chance)

    #community chest
    elif (moveTo == 18 or moveTo == 34):
        #move to specific square
        if (type(CC[0]) == int):
            jmp = True
            Aland.append(CC[0])
            if (CC[0] == 11): jailed = True
        CC.remove(CC[0])
        #reshuffle if empty
        if (len(CC)==0):
            CC = [1,"","","","",11,"","","","","","","","","",""]
            r.shuffle(CC)

        

    if jmp:
        try:
            if jailed: freq[41] += 1
            else: freq[Aland[-1]] += 1
        except KeyError:
            if jailed: freq[41] = 0
            else: freq[Aland[-1]] = 0


try:
  freq[1] += 1
except KeyError:
  freq[1] = 1



plt.bar([key for key in freq],[freq[key] for key in freq])
sortFreq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
print("Percent Chance of landing on each Square ")
for key in sortFreq:
    print(f"{names[key]}: {round(sortFreq[key]/iter*100,6)}%")

#plt.xlim(0,12)
plt.xlabel("Squares landed on")
plt.ylabel("Frequency")
plt.title(f"Distribution of Squares Landed on in a game of Monopoly (n = {len(Aland)})")
plt.show(block=True)
