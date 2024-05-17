
def isPrime(n):
  if n < 2:
    # 2未満は素数でない
    return False
  if n == 2:
    # 2は素数
    return True
  for p in range(2, n):
      if n % p == 0:
        # nまでの数で割り切れたら素数ではない
        return False
  # nまでの数で割り切れなかったら素数
  return True

if __name__ == "__main__":
    n = int(input())
    print(isPrime(n))






