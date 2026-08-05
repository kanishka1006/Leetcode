from collections import defaultdict
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
        suspicious = set()
        def dfs(node):
            suspicious.add(node)

            for nei in graph[node]:
                if nei not in suspicious:
                    dfs(nei)
        dfs(k)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]