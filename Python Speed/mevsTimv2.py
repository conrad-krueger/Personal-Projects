import random as r
from time import perf_counter


#modified counting sort that does not accumulate values of counting list (store)
def sort(lst):
  store = [0] * (max(lst)+1) #keeps track of repeated values
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



def sort2(lst):
  minVal = min(lst)
  store = [0] * (max(lst)-minVal+1) #keeps track of repeated values
  newLst = [None] * len(lst) #returned sorted list

  #increment indexes
  for val in lst:
    store[val-minVal] += 1

  i = 0
  for index,occurs in enumerate(store):

    while(occurs != 0):
      newLst[i] = index+minVal
      occurs -= 1
      i+= 1
  
  return newLst



def test(totalIter, minN, maxN, minVal, maxVal, verbose = True):
  tim = None
  me = None
  iter = 0
  timW = 0
  meW = 0


  for _ in range(totalIter):
      n = r.randint(minN ,maxN)

      lst = [r.randint(minVal,maxVal) for _ in range(n)]
      r.shuffle(lst)
      mx = max(lst)
      mn = min(lst)

      start = perf_counter()
      sort(lst)
      end = perf_counter()
      me = (end - start)

      #timsort
      start = perf_counter()
      lst.sort()
      end = perf_counter()
      tim = (end - start)

      winner = "Modified Counting Sort"
      loser = "Tim Sort"
      ratio = (tim/me)
       
      if(tim < me):
          winner, loser = loser, winner
          ratio = 1/ratio
          timW += 1
      else: meW += 1
      
      iter += 1
      if verbose:
         print(f"[{iter}] {winner} was {ratio}x faster than {loser}")
         print(f"INFO: n = {n}, range = [{mn},{mx}], Tim Time: {round(tim,6)} sec, Counting Sort v2 Time: {round(me,6)} sec")


  print()
  print()
  print("SUMMARY")
  print(f"Tim Sort was fastest algorithm {timW} times ({round(timW/totalIter *100,2)}%)")
  print(f"Modified Counting Sort was fastest algorithm {meW} times ({round(meW/totalIter *100,2)}%)")  
  print()


def main(): 
    iterations = 25 #how many tests
    minListSize, maxListSize = 1000000, 3000000 #will generate list of random sizes of minListSize to and including maxListSize
    maxValue = 1000000 #lists will contain integer values randomly from minValue to maxValue
    minValue = 0
    verbose = True #should it print info on every iteration or not

    test(iterations, minListSize, maxListSize, minValue, maxValue, verbose)


if __name__ == "__main__":
  main()




