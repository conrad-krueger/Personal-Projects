from time import perf_counter




def traverseTest(n):
  lst = [x for x in range(n)]

  print("Quickest Loops")

  #enumerate
  start = perf_counter()
  for i,v in enumerate(lst):
    pass
  end = perf_counter()
  print(f"enumerate:  {end - start}")

  #range len
  start = perf_counter()
  for i in range(len(lst)):
    pass
  end = perf_counter()
  print(f"range(len()):  {end - start}")

  #x in lst
  start = perf_counter()
  for x in lst:
    pass
  end = perf_counter()
  print(f"in lst:  {end - start}")

  #while loop
  start = perf_counter()
  i = 0
  while i != len(lst):
    pass
    i += 1
  end = perf_counter()
  print(f"while loop:  {end - start}")

  #list comp
  '''
  start = perf_counter()
  [for x in lst]
  end = perf_counter()
  print(f"list comp:  {end - start}")
  '''

  


def createListTest(n):

  print("Fastest way to intialize empty list with size n")
  start = perf_counter()
  [None] * n
  end = perf_counter()
  print(f"None * n:  {end - start}")

  start = perf_counter()
  [None for x in range(n)]
  end = perf_counter()
  print(f"[None for]:  {end - start}")

  start = perf_counter()
  lst = []
  for x in range(n):
    lst.append(None)
  end = perf_counter()
  print(f".append(None):  {end - start}")

  start = perf_counter()
  lst = []
  for x in range(n):
    lst += [None]
  end = perf_counter()
  print(f"+= [None]:  {end - start}")

  print()
  print("Don't know elements but know size of final array?")
  print("Should you do .append() to an empty list or [None]*n and then change each element")
  start = perf_counter()
  lst = []
  for x in range(n):
    lst.append(x)
  end = perf_counter()
  print(f".append():  {end - start}")
  start = perf_counter()
  lst = [None] * n
  for x in range(n):
    lst[x] = x
  end = perf_counter()
  print(f"None and change:  {end - start}")


def main():
  createListTest(100000000)
  traverseTest(100000000)

if __name__ == "__main__":
  main()
