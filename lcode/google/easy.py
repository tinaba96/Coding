#299
class Solution:
    def getHint(self, secret: str, guess:str) -> str:
        bulls = 0
        cows = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                cows += 1
            if guess[i] in secret:
                bulls += 1
        return str(cows) + 'A' + (bulls-cows) + 'B'


