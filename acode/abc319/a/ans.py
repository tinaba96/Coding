table = '''
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
'''

s = input()
for line in table.strip().split('\n'):
  user,rating = line.split()
  if user == s:
    print(rating)


# or use the eidtor function -> video editorial

