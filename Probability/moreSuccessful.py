
import scipy.stats as stat
from math import sqrt, ceil
import sys
# This program develops confidence intervals on a list of player's population proportions of a Bernoulli event (ideally skill-based), 
# compares player's point estimates and indicates if there is statistically significant evidence to suggest that not all proportions are the same using Chi-squared Hypothesis Testing,
# and if there is evidence, isolate which differences in the player's point estimates are statistically significant using the Marascuilo Procedure

suc = "E"

def proportion_ci(p_hat:float, n:int, alpha:float = .05):
  """
  Prints a confidence interval for population proportion only if the Central Limit Theorem applies
  
  :param float p_hat: sample proportion
  :param int n: sample size
  :param float alpha: level of significance
  :return: 1/2 width of the confidence interval
  :rtype: float
  """


  if (round(p_hat*n >= 5) and round((1-p_hat)*n) >= 5): #CLT applies
    
    edges = stat.norm.ppf(1-alpha/2)*sqrt(p_hat*(1-p_hat)/n)
    print(f"P({suc}) = {p_hat} ± {round(edges,9)} ({(1-alpha) *100}% CI)")
    return edges
  
  else:
    print("ERR: CLT does not apply")
    return 0
  


#https://www.itl.nist.gov/div898/handbook/prc/section4/prc474.htm
def marascuilo(lst, alpha): #lst =[[name ,p_hat, n]]
  """
  Performs a Marascuilo Procedure which prints out a comparison of all pairs of proportions and depicts if 
  a particular pair's difference is statistically significant
  
  :param [[str, float, int]] lst: list of a list of information containing a string that has the players name, a float that has the players sample proportion of throwing unhindered strikes, and an int containing the number of trials 
  :return: None
  :raises ValueError: if the lst has less than 3 arguments
  """

  if(len(lst) < 3):
    raise ValueError("Can only perform Marascuilo Procedure with atleast 3 proportions")

  sig = []
  for i in range(len(lst)):
    idi,pi,ni = lst[i][0], lst[i][1], lst[i][2]

    for j in range(i+1,len(lst)):
      idj,pj,nj = lst[j][0], lst[j][1], lst[j][2]
      rij = sqrt(stat.chi2.ppf(1-alpha,len(lst)-1)) * sqrt(pi*(1-pi)/ni + pj*(1-pj)/nj)

      detail = f"|{idi[:4] if pi > pj else idj[:4]}✓ - {idj[:4] if pi > pj else idi[:4]}|\t Diff: {round(abs(pi-pj),4)}\t Crit: {round(rij,4)} Sig: {rij < abs(pi-pj)}"
      if (rij < abs(pi-pj)): sig.append(detail)
      print(detail)

  print()
  print(f"Statistically Significant differences in \"{suc}\" proportions:")
  if(len(sig) == 0): print("None")
  for detail in sig:
    print(detail[:-10])




#https://www.itl.nist.gov/div898/handbook/prc/section4/prc46.htm
#https://www.openanesthesia.org/statistics_test_of_proportions/ (this is why chisquared test and not Z test is being used, comparing 2+ groups)
def comparing_proportions(lst, alpha): #lst of [name, p_hats, n]
  """
  Performs a Hypothesis Test where H0: No difference in proportions & Ha: Not all proportions are equal
  Hypothesis Testing method is "Testing for homogeneity of proportions using the Chi-squared distribution via contingency tables" (see link above)
  
  :param [[str, float, int]] lst: list of a list of information containing a string that has the players name, a float that has the players sample proportion of throwing unhindered strikes, and an int containing the number of trials 
  :param float alpha: level of significance
  :return: True if the null hypothesis was rejected, otherwise False is returned
  :type: bool
  :raises ValueError: if the lst has less than 2 arguments
  """
  p_overall = 0
  n_total = 0

  if(len(lst) < 2):
    raise ValueError("Can only compare atleast 2 proportions")


  for _, p, n in lst:
    p_overall += p*n 
    n_total += n
  p_overall /= n_total #pooling average

  test_stat = 0

  for _, p, n in lst: #compare and accumulate expected successes AND failures with actual successes AND failures
    test_stat += ((p*n-p_overall*n)**2)/(p_overall*n) #multiply with sample size to get expected frequency
    test_stat += (( ((1-p)*n) - ((1-p_overall)*n) )**2)/ ((1-p_overall)*n)

  crit_val = stat.chi2.ppf(1-alpha,len(lst)-1)
  
  print(f"Test Statistic: {test_stat} Critical Value: {crit_val} p-value: {1 - stat.chi2.cdf(test_stat, len(lst)-1)}")
  

  if (test_stat > crit_val): 
    print("CONCLUSION: Reject H0")
    return True
  else: 
    print("CONCLUSION: Fail to Reject H0")
    return False


def summary(lst,alphaCI, alphaCompare):
  """
  Runs all of the functions above for each pitcher/whole dataset
  
  :param [[str, float, int]] lst: list of a list of information containing a string that has the players name, a float that has the players sample proportion of success, and an int containing the number of trials 
  :param float alphaCI: level of significance for developing a confidence interval
  :param float alpha: level of significance for comparing proportions
  :return: None
  """

  for name, prob, n in lst:
    print(f"{name}'s Statistics:")
    proportion_ci(prob, n, alphaCI)
    print()
  print("="*20)
  print()
  
  print("Chi-Squared Hypothesis Test.")
  print("H0: No difference in proportions & Ha: Not all proportions are equal")
  if(comparing_proportions(lst,alphaCompare)):
    print()
    print("="*20)
    print()
    print("Because H0 was rejected, a Marasculio Procedure will be ran to see which specific differences in proportions are significant...")
    print("Note: '✓' denotes which of the players being compared has the higher sample proportion.")
    marascuilo(lst, alphaCompare)





def main(argv):
  data = []
  alphaCI = 0.1
  alphaCompare = 0.1
  #modify 'suc' above if hardcoding values

  #user inputs data, else will compute with hard coded values
  if argv == "user":
    
    #get number of players
    while True:
      try:
        playerNum = int(input("Enter number of players: "))
        if (playerNum <= 2): raise ValueError()
        break
      except ValueError: 
        print("ERROR: Incorrect Input. Enter an integer value greater than 2.")
    
    #get Event name
    global suc
    suc = input("Enter what is considered a \"success\" in these Bernoulli Trials: ")
    print()

    #get player info
    for i in range(playerNum):
      player = input(f"Enter name of player {i+1}: ")

      #P(success)
      while True:
        try:
          ps = float(input(f"Enter {player}'s sample probability of \"{suc}\": "))
          if (ps < 0 or ps > 1): raise ValueError()
          break
        except ValueError: 
          print("ERROR: Incorrect Input. Enter a floating-point value greater between 0 and 1 inclusive.")
      
      #How many Bernoulli Trials
      while True:
        try:
          n = int(input(f"Enter {player}'s number of trials: "))
          if (n < 0): raise ValueError()
          break
        except ValueError: 
          print("ERROR: Incorrect Input. Enter an integer value greater than 0.")
      
      data.append([player,ps,n])
      print()
    
    #end for

    #Alpha level for CI
    while True:
      try:
        alphaCI = float(input(f"Enter the level of sigificance (alpha) for developing a confidence interval: "))
        if (alphaCI < 0 or alphaCI > 1): raise ValueError()
        break
      except ValueError: 
        print("ERROR: Incorrect Input. Enter a floating-point value greater between 0 and 1 inclusive.")
    
    #Alpha level for Comparing Proportions
    while True:
      try:
        alphaCompare = float(input(f"Enter the level of sigificance (alpha) for comparing proportions: "))
        if (alphaCompare < 0 or alphaCompare > 1): raise ValueError()
        break
      except ValueError: 
        print("ERROR: Incorrect Input. Enter a floating-point value greater between 0 and 1 inclusive.")
    print()
    print("Data:",data)
    print()

  #end if
        
  print("="*20)
  print()


  try:
    summary(data,alphaCI,alphaCompare)
  except Exception as err:
    print(f"ERROR: {err}")


if __name__ == "__main__": 
  if (len(sys.argv) > 1): main(sys.argv[1])
  else: main("")
