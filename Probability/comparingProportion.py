from scipy import stats
import math
def comparingProportion(px,m,py,n,alpha=.05):
  if(px * m < 5 or (1-px)*m <5 or py * n < 5 or (1-py)*n <5):
    print("ERROR: Central Limit Theorem does not apply")
    return None
  
  p = (px*m + py*n)/(m+n)

  Z = (px - py) / math.sqrt(p*(1-p) * (1/m + 1/n))
  print(Z)
  pval = 2*stats.norm.sf(abs(Z))

  if pval < alpha: print("Reject the null hypothesis that px = py")
  else: print("FAIL to reject the null hypothesis that px = py")
  
  return pval

def main():
    print(comparingProportion(.0607, 100000, .0588, 100000))
if __name__ == "__main__": main()
