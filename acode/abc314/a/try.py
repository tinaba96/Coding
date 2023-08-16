N = int(input())

number = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

print(number)

#number = round(number, N)
formatted_number = "{:.{}f}".format(number, N)
print(formatted_number)

number = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
formatted_number = format(number, ".100f")
print(formatted_number)

# 倍精度浮動小数点数だから？１５桁くらいしか精度が保証されていないため。
# 基本的に（約）15桁以上の精度は保証されていない。

