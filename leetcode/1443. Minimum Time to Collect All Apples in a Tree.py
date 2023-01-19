from typing import List

class ISolution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        pass

class Solution_old(ISolution):
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {x[0]: [] for x in edges}
        for x in edges:
            tree[x[0]].append(x[1])
        unreach = set(i for i, x in tree.items()) - set(item for i, sublist in tree.items() for item in sublist)
        print(unreach)
        print(tree)
        print({i: k for i, k in enumerate(hasApple)})
        return sum(self._pass_tree(tree, i, hasApple, unreach) for i in unreach)

    def _pass_tree(self, tree: dict, n: int, has_apple: List[bool], unreach: set) -> int:
        add = 0 if n in unreach else 2
        if n not in tree:
            return add if has_apple[n] else 0
        summ = sum(self._pass_tree(tree, i, has_apple, unreach) for i in tree[n])
        if summ == 0:
            return add if has_apple[n] else 0
        else:
            return summ + add


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        pass

    def _pass_tree(self, tree: dict, node_from: int, node_current: int, has_apple: List[bool]) -> int:
        p_tree = tree[node_current]
        if node_current not in tree:
            return 1 if has_apple[node_current] else 0
        summ = sum(self._pass_tree(tree, i, has_apple) for i in tree[n] if i == node_from)
        summ += 1 if has_apple[node_current] else 0

if __name__ == '__main__':
    n = 7

    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, True, False, True, True, False]
    r = Solution().minTime(n, edges, hasApple)
    print(r)

    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, True, False, False, True, False]
    r = Solution().minTime(n, edges, hasApple)
    print(r)

    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, False, False, False, False, False]
    r = Solution().minTime(n, edges, hasApple)
    print(r)

    edges = [[0,2],[0,3],[1,2]]
    hasApple = [False, True, False, False]
    r = Solution().minTime(n, edges, hasApple)
    print(r)

    edges = [[0,3],[1,2]]
    hasApple = [False, False, True, False]
    r = Solution().minTime(n, edges, hasApple)
    print(r)
