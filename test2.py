import collections
class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(0,4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    print(nei)
                    queue.append((nei, depth+1))
        return -1

if __name__ == '__main__':
   print( Solution().openLock({},'2003'))