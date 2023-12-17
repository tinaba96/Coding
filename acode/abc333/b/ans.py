S = input()
T = input()

len_1s = ["AB", "AE", "BA", "BC", "CD", "CB", "DE", "DC", "EA", "ED"]
if (S in len_1s and T in len_1s) | (S not in len_1s and T not in len_1s):
    print("Yes")
else:
    print("No")
