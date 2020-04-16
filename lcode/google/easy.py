#299
class Solution:
    def getHint(self, secret: str, guess:str) -> str:
        bulls = 0
        cows = 0
        li = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                cows += 1
                li.append(i)
        flag
        for i in range(len(guess)):
                for j in range(len(secret)):
                    if guess[i] == secret[j]:
                        if j not in li:
                            bulls += 1
                            li.append(j)
        return str(cows) + 'A' + str(bulls) + 'B'



