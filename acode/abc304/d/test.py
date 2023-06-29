

import bisect
list1 = [1, 4, 6, 8, 9, 12, 15, 20, 25, 47]
value1 = 460
print(bisect.bisect(list1, value1))
# 8
list2 = [1, 1, 4, 5, 6, 8, 8, 8, 8, 9, 9, 9]
value2 = 8
#print(bisect.bisect(list2, value2))
# 9
list3 = [2, 4, 6, 8, 10, 12, 14]
value3 = 7
#print(bisect.bisect(list3, value3))
# 3
