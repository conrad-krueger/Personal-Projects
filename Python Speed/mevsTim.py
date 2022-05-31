import random as r
from time import perf_counter
import statistics as s

def quickSort(lst):
  if(len(lst) <= 1): return lst 
  
  pivot = r.randint(0,len(lst)-1)

  left, right, eq = [], [], []

  for num in lst:
    if (num > lst[pivot]):
      right.append(num)
    elif (num < lst[pivot]):
      left.append(num)
    else:
      eq.append(num)
  
  left = quickSort(left)
  right = quickSort(right)

  return left + eq + right


def countingSort(lst, maxVal):
  store = [0] * (maxVal+1)
  newLst = [None] * len(lst)

  for val in lst:
    store[val] += 1

  for i in range(len(store)-1):
    store[i+1] += store[i]
  
  for i in range(len(lst)-1,-1,-1):
    store[lst[i]] -= 1
    newLst[store[lst[i]]] = lst[i]
    
  return newLst

def countingSort2(lst, maxVal):
  store = [0] * (maxVal+1) #keeps track of repeated values

  newLst = [None] * len(lst) #returned sorted list

  #increment indexes
  for val in lst:
    store[val] += 1

  i = 0
  for index,occurs in enumerate(store):

    while(occurs != 0):
      newLst[i] = index
      occurs -= 1
      i+= 1
  
  return newLst



def bucket(lst, maxVal):
  store = [[] for _ in range(maxVal+1)]
  newLst = [None] * len(lst)
  
  for val in lst:
    (store[val]).append(val)
  
  i = 0
  for lst1 in store:
    for num in lst1:
      newLst[i] = num
      i+=1
  return newLst


globalWins = {"Counting Sort":0,"Counting Sort v2":0,"Bucket Sort":0,"Quick Sort":0,"Tim Sort":0}

iter = 0

def winner(n, timTime, countingTime, counting2Time, bucketTime, quickTime,verbose):
  lst = [ counting2Time, countingTime, bucketTime, quickTime ,timTime]
  strLst = ["Counting Sort v2","Counting Sort","Bucket Sort","Quick Sort","Tim Sort"]


  mx = min(lst)
  
  winner = strLst[lst.index(mx)]
  globalWins[winner] += 1

  global iter

  if (verbose): 
    print(f"{iter}] Fastest (n = {n}): {winner}")
    for i, v in enumerate(lst):
      print(f"{strLst[i]} = {round(v/mx,6)}x slower, ", end="")
    
    print()

  iter += 1


def main(totalIter, n, maxVal, verbose = True):
  quickTime = None
  timTime = None
  countingTime = None
  counting2Time = None
  bucketTime = None


  for _ in range(totalIter):
      lst = [r.randint(0,maxVal) for _ in range(n)]
      lst2 = lst
      r.shuffle(lst)
      mx = max(lst)

      #counting sort test
      start = perf_counter()
      countingSort(lst, mx)
      end = perf_counter()
      countingTime = end - start

      #counting sort v2 test
      start = perf_counter()
      countingSort2(lst, mx)
      end = perf_counter()
      counting2Time = end - start

      #bucket sort test
      start = perf_counter()
      bucket(lst, mx)
      end = perf_counter()
      bucketTime = end - start

      #Quick Sort
      start = perf_counter()
      quickSort(lst)
      end = perf_counter()
      quickTime = end - start

      #TimSort
      start = perf_counter()
      lst2.sort()
      end = perf_counter()
      timTime = end - start

       
      winner(n, timTime, countingTime, counting2Time, bucketTime, quickTime, verbose)

  print("SUMMARY")
  for key in globalWins:
    print(f"{key} was fastest algorithm {globalWins[key]} times ({round(globalWins[key]/totalIter *100,2)}%)")
      
  print()
  

if __name__ == "__main__":
  main(100, 100000, 100000)




