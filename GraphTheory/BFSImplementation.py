"""Graph theory p1 m2"""
from collections import deque

EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])};
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])};
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,4,5,6,7,3])};

def bfs_visited(ugraph, start_node):
    """bfs_visited(num_nodes) -> dictionary"""
    q = deque();
    visited = [];
    visited.append(start_node);
    q.append(start_node);

    while len(q) != 0:
        j = q.pop();
        for h in ugraph[j]:
            if h not in visited:
                visited.append(h);
                q.append(h);
                print h;

print bfs_visited(EX_GRAPH1, 0);