
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        a = 0
        if digits[n-1] != 9:
            digits[n-1] += 1
            return digits
        while digits[n-1-a] == 9:
            digits[n-1-a] = 0
            a += 1
            if n-1-a < 0:
                digits.insert(0, 1)
                return digits
        digits[n-1-a] += 1  #input [9]のときの挙動チェック
        return digits

    #ans 





	def findReplaceString(self, S, indexs, sources, targets):
		for i in range(len(sources)):
			index = indexes[i]
			if S[index] == sources[index]:
				S.insert(index, targets[index])
				del S[index+len(targets[index]) : index+len(targets[index])+len(sources[index])]



	def merge(self, intervals):
		index = []
		ans = []
            for i in range(len(intervals)-1):
			if intervals[i][1] >= intervals[i+1][0]:
				index.append(str(i))
		extra = 0
        for i in range(len(intervals)):
        	temp = []
		if i in index:
                    temp.append(intervals[i][0])
                    temp.append(intervals[i+1][1])
                    ans.append(temp)
                    extra += 1
                else:
        		ans.append(intervals[i])
		return ans



