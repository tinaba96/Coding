def janken(a,b):
  if a==b:
    return -1
  elif a=="G" and b=="P":
    return 1
  elif a=="P" and b=="C":
    return 1
  elif a=="C" and b=="G":
    return 1
  return 0
N,M=map(int,input().split())
S=[input() for _ in range(2*N)]
#print(S)
rank=[[0,i] for i in range(2*N)]
for i in range(M):
  for j in range(N):
    player_1=rank[2*j][1]
    player_2=rank[2*j+1][1]
    #print(player_1,player_2)
    #print(S[player_1][i],S[player_2][i])
    result=janken(S[player_1][i],S[player_2][i])
    if result!=-1:
      rank[2*j+result][0]-=1
  rank.sort()
  #print(rank)
for i in range(2*N):
  print(rank[i][1]+1)

# this is same approach as the video editorial from Atcoder
# 参考
# https://note.nkmk.me/python-list-2d-sort/
# デフォルトでは各リストの最初の等しくない要素が比較されソートされるので、1列目が等しい場合は2列目の値でソートされる。


