class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = []
        for i in range(0, len(compressedString), 2):
            for j in range(compressedString[i+1]):
                self.compressed.append(compressedString[i])

        

    def next(self) -> str:
        if self.compressed:
            return self.compressed.pop(0)
        else:
            return ""

    def hasNext(self) -> bool:
        if self.compressed:
            return true
        else:
            return false
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()




