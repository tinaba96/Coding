
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
        digits[n-1-a] += 1  
        return digits

    #ans 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits





	def findReplaceString(self, S, indexs, sources, targets):
		for i in range(len(sources)):
			index = indexes[i]
			if S[index] == sources[index]:
				S.insert(index, targets[index])
				del S[index+len(targets[index]) : index+len(targets[index])+len(sources[index])]

#ans
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in xrange(len(x))):
                S[i:i+len(x)] = list(y)  #単純にyでも同様。しかし、[y]とすると一つの要素として認識されるが、結果は同じ。

        return "".join(S)

'''
文字列はスライスで指定することはできるが、置き換えることができない。→一回リストに変換する必要あり。
スライスして結合する方法でも可能。
'''

'''
java solution
class Solution {
    public String findReplaceString(String S, int[] indexes, String[] sources, String[] targets) {
        int N = S.length();
        int[] match = new int[N];
        Arrays.fill(match, -1);

        for (int i = 0; i < indexes.length; ++i) {
            int ix = indexes[i];
            if (S.substring(ix, ix + sources[i].length()).equals(sources[i]))
                match[ix] = i;
        }

        StringBuilder ans = new StringBuilder();
        int ix = 0;
        while (ix < N) {
            if (match[ix] >= 0) {
                ans.append(targets[match[ix]]);
                ix += sources[match[ix]].length();
            } else {
                ans.append(S.charAt(ix++));
            }
        }
        return ans.toString();
    }
}

'''


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

#ans
class Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph


    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]


    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])


        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]


#better answer
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


