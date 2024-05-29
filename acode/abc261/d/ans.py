#import numpy as np
import itertools

def main():
  n, m=map(int, input().split())
  x=list(map(int, input().split()))
  b=[0]*(n+1)
  for i in range(m):
    c, y=map(int, input().split())
    b[c]=y
    
  dp=[[0]*(n+1) for _ in range(n+1)]
  
  for i in range(1,n+1):
    dp[i][0]=max(dp[i-1])
    for j in range(1,i+1):
      dp[i][j]=dp[i-1][j-1] + x[i-1] + b[j]
      
  #print(max(list(itertools.chain.from_iterable(dp))))
  print(list(itertools.chain.from_iterable(dp)))
  print(max(dp[-1]))
  
if __name__=="__main__":
  main()
  
