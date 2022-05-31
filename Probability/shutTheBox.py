import random as r
import statistics as s
import matplotlib.pyplot as plt
import math
all = []
freq = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} #will contain how valuable each number is in creating a summation of 2 dice role.

#generating function for rolling 2 dice
def weight(num):
  if num <= 7: return (num-1)/36
  else: return (num-(2*(num-7)-1))/36

#generates all possible combinations in which 1 to 3 numbers can add up to each possible 2 dice roll [2,12]
for rolled in range(2,13):
  combos = []


  for num1 in range(1,10):
    if (num1 == rolled): 
      combos.append((num1,))
      freq[num1] += weight(num1) #assign freq with the weight of the number. if a number is used for getting the number 7, that is more important than generating the number 12.
    if (num1 > rolled): break #efficent break. if num1 is greater than the number rolled no point in checking if num1 + other numbers = rolled

    for num2 in range(1, 10):
      if (num1 + num2 == rolled and num1 != num2):  #make sure numbers are not the same (cannot repeat numbers)
        combos.append(tuple(sorted([num1, num2])))
        freq[num1] += weight(num1 + num2)
        freq[num2] += weight(num1 + num2)
      if (num1 + num2 > rolled): break

      for num3 in range(1, 10): 
        if (num1 + num2 + num3 == rolled and num1 != num2 and num2 != num3 and num1 != num3): 
          combos.append(tuple(sorted([num1, num2, num3])))
          freq[num1] += weight(num1 + num2 + num3)
          freq[num2] += weight(num1 + num2 + num3)
          freq[num3] += weight(num1 + num2 + num3)
        if (num1 + num2 + num3 > rolled): break
  noDup = []
  [noDup.append(x) for x in combos if x not in noDup] #yes i could have just casted to a set but i prefer to have it in this order
  all.append(noDup)
  print(f"All possible combinations of {rolled} are: {noDup}")

print("Frequency:", freq)

lostremain = []
allremain = []




#function play simulates [iter] iterations of Shut the Box game. verbose and small info indicate what, if any, information is printed out to the user.
#[method] determines the method of selecting the numbers that will sum to the 2 dice roll.
def play(iter, verbose = False, smallinfo = False, method=1):
  i = 0
  win = 0 
  loss = 0
  global freq
  while i < iter:

    if verbose or smallinfo:
      print()
      print(f"New Round (# {i+1})")
    options = [1,2,3,4,5,6,7,8,9]
    while True:
      if verbose: print(options)


      if sum(options) == 0:
        if verbose or smallinfo: print("WIN!")
        win += 1
        allremain.append(0)
        break

      
      dice = r.randint(1,6) + r.randint(1,6) #roll dice
      if verbose: print("Rolled a", dice)
      freqMin = 100
      elimHold = None

      canKnockDown = False

      #Preserve Highest frequency method
      if (method == 1):
        for elim in all[dice-2]: #iterate through all combinations to get dice.
          currFreq = 0
          for num in elim: #ensure that combination is still available
            if num not in options:
              canKnockDown = False
              break
            
            currFreq += freq[num] #if it is avaiable, get the frequency value of that combination
            canKnockDown = True

            
            
          if canKnockDown:
            if currFreq < freqMin: #get the samllest frequency val
              freqMin = currFreq
              elimHold = elim
      
      ######################

      #Random / least numbers
      if method >= 2:
        if method == 4: r.shuffle(all[dice-2]) #Random selection
        if method == 3: 
          for elim in all[dice-2][::-1]:
            for num in elim:
              if num not in options:
                  canKnockDown = False
                  break
              canKnockDown = True

            if canKnockDown: 
              elimHold = elim
              break
        else: #most numbers method
          for elim in all[dice-2]:
            for num in elim:
              if num not in options:
                  canKnockDown = False
                  break
              canKnockDown = True

            if canKnockDown: 
              elimHold = elim
              break
  
      #checks if a combination was found, if so, remove that combination from the avaiable options
      if elimHold != None:
        if verbose: print("Knocking down:", elimHold)
        for x in elimHold:
          options[x-1] = 0
      else: #else, this round was a loss
        if verbose or smallinfo: print("Loss")
        loss += 1
        count = 0
        for x in options: 
          if x != 0: count += 1
        lostremain.append(count)
        allremain.append(count)
        break
    i += 1
    


  print()
  print("FINAL STATISTICAL ANALYSIS")
  print()
  print()

  print("Total wins:", win)
  print("Win rate: ", win/iter * 100 ,"%",sep="")
  print()
  print("Total Losses:", loss)
  print("Lose rate: ", loss/iter * 100 ,"%",sep="")
  print()
  print("Statistics of remaining squares on all Losses:")
  print("Mean:", s.mean(lostremain))
  print("Median:", s.median(lostremain))
  print("Mode:", s.mode(lostremain))
  print("Min:", min(lostremain))
  print("Max:", max(lostremain))
  print("Standard Deviation:",s.stdev(lostremain))
  if(loss >= 5 and win >= 5): #CLT
    p_hat = win/iter
    Z = 2.58
    stderr = math.sqrt(p_hat* (1-p_hat)/ iter)
    lb = round((p_hat-Z*stderr)*100,6)
    if lb < 0: lb = 0

    print(f">99% Confidence Interval: {p_hat} ± {Z*stderr} = ({lb}%, {round((p_hat+Z*stderr)*100,6)}%)" )
  else: print("No Confidence Interval can be made. Central Limit Theorem does not apply.")
  print()
  print()


  freq = [0] * 9

  for x in lostremain:
    try:
      freq[x-1] += 1
    except Exception:
      print(x)


  plt.bar(list(range(1,10)), freq)
  plt.xlabel("Remaining Squares")
  plt.ylabel("Frequency")
  plt.title("Distribution of Remaining Squares on a Losing Game of Shut the Box (n ="+str(len(lostremain))+")")
  plt.show(block=True)



def main():
    try:
      iter = int(input("Number of iterations: "))
      verbose = True if input("Show each game? 1] Yes 2] No ") == "1" else False
      smallinfo = True if input("Show win or loss on each iteration 1] Yes 2] No ") == "1" else False
      method = int(input("What Method should be used? 1] Preserve Highest Frequent Numbers 2] Highest amount of numbers 3] Lowest amount of Numbers 4] Random "))
      
      play(iter, verbose, smallinfo,method)
    except Exception:
        print("Error: Invalid Input")

if __name__ == "__main__":
    main()



