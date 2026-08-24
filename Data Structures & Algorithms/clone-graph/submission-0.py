"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        clones = {}

        if node is None:
            return None
        
        def clone(origin):
            if origin in clones:
                return clones[origin]
            copy = Node(origin.val)
            clones[origin] = copy
            for n in origin.neighbors:
                copy.neighbors.append(clone(n))
            return copy

        return clone(node)
