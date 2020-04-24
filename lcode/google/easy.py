#299
class Solution:
    def getHint(self, secret: str, guess:str) -> str:
        bulls = 0
        cows = 0
        li = []
        same = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                cows += 1
                same.append(i)
                li.append(i)
        for i in range(len(guess)):
                for j in range(len(secret)):
                    if guess[i] == secret[j]:
                        if i not in same:
                            if j not in li:
                                bulls += 1
                                li.append(j)
                                break
        return str(cows) + 'A' + str(bulls) + 'B'

    #O(n)
    def getHint(self, secret: str, guess: str) -> str:
        if secret == guess:
            return f"{len(secret)}A0B"
        
        potential_cows_in_secret = {}
        potential_cows_in_guess = {}
        bulls = 0 
        cows = 0 
        
        i = 0 
        while i < len(guess):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in potential_cows_in_secret:
                    potential_cows_in_secret[secret[i]] += 1
                else:
                    potential_cows_in_secret[secret[i]] = 1
                    
                if guess[i] in potential_cows_in_guess:
                    potential_cows_in_guess[guess[i]] += 1
                else:
                    potential_cows_in_guess[guess[i]] = 1
            
            i += 1
        
        for digit in potential_cows_in_guess:
            if digit in potential_cows_in_secret:
                cows += min([potential_cows_in_secret[digit], potential_cows_in_guess[digit] ])
        
        return f"{bulls}A{cows}B"

#359
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.message = 0

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        list = {}
        if message in list:
            return False
        else:
            list.append((timestamp, message))
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


