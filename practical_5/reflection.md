# Reflection on Practical 5

This file contains my reflections on the topics covered in the Practical 5 folder. For each topic, I wrote what I learned, the challenges I faced, and how I overcame them.

---

## 1. Binary Search Tree
#### What I Learned
Understood the core idea of how binary search trees (BSTs) store data in sorted order.

Learned that insertion always goes left if the new value is smaller, and right if it is larger.

Practiced writing traversal methods (inorder, preorder, postorder) and saw how they produce different outputs.
#### Challenges Faced
Initially struggled with handling cases where the tree was empty.

Got confused when writing recursive traversal functions, especially with the base case.

Sometimes the output order wasn’t what I expected, so I had to trace the logic carefully.
#### How I Overcame Them
Drew tree diagrams on paper to clearly see where nodes should go.

Walked through my recursive functions step by step to understand how values were returned.

Simplified my code by writing smaller helper functions that focused only on one task.
---

## 2. Graph Data Structure and Traversal Algorithms
#### What I Learned
Learned that graphs can be represented in multiple ways, such as adjacency lists and adjacency matrices.

Practiced implementing BFS (level-order traversal) and DFS (depth-first traversal).

Saw how traversal strategies affect the order in which nodes are visited.
#### Challenges Faced
Had difficulty preventing infinite loops when the graph contained cycles.

Initially forgot to reset my visited list between different traversal runs.

Writing BFS with a queue was tricky at first since I wasn’t fully comfortable with queue operations in Python.
#### How I Overcame Them
Used a set to store visited nodes so that repeated visits were avoided.

Printed the traversal step by step to check if nodes were being visited in the correct order.

Reviewed how queues and stacks work in Python to strengthen my understanding of BFS and DFS.

---

##  Overall Reflection
Practical 5 gave me hands-on practice with two important data structures: binary search trees and graphs. Implementing them from scratch made me appreciate how recursion and data organization make searching and traversal efficient.

### Future Improvements
I want to try implementing self-balancing trees like AVL or Red-Black trees to handle uneven growth.

I plan to explore more advanced graph algorithms such as Dijkstra’s algorithm and Prim’s algorithm to build a stronger foundation in graph theory.

---