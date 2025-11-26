
## Practical 5 – Binary Search Trees & Graph Traversal

### 📝 Problem Summary

* **BST:** Insert nodes, perform inorder/preorder/postorder traversal.
* **Graphs:** Build a graph and perform **BFS** and **DFS**.

### ✅ Optimal Approaches

#### **Binary Search Tree (BST)**

* Use **recursion** for insertion and traversal.
* Inorder traversal naturally outputs sorted values.

##### **Shortest Clean BST Code**

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
```

---

### **Graph Traversal (BFS & DFS)**

#### Optimal methods:

* Use **adjacency list** for efficient traversal.
* Use **queue** for BFS and **stack/recursion** for DFS.

##### **Shortest Clean Graph Code**

```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def bfs(start):
    visited, q = set(), deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

def dfs(start, visited=set()):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for n in graph[start]:
            dfs(n, visited)
```

---

### ⭐ Summary

* BST uses recursion for insertion + traversal.
* BFS uses a **queue**, DFS uses **recursion/stack**.
* These are the most optimal and clean solutions for this practical.
