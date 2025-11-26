# Reflection on Practical 6

This file contains my reflections on the topics covered in Practical 6. I wrote what I learned, the challenges I faced, and how I overcame them.

## 1. Linear Search
### What I Learned

Linear search checks each element one by one until the target is found.

It works on unsorted lists.

Simple and intuitive, but less efficient for large datasets.

### Challenges Faced

Initially, I forgot to return -1 if the target wasn’t found.

Understanding when linear search is appropriate versus binary search.

### How I Overcame Them

Tested with multiple lists including edge cases.

Compared linear vs binary search to understand performance differences.

## 2. Binary Search (Iterative and Recursive)
### What I Learned

Binary search divides the search range in half each time → O(log n) complexity.

Works only on sorted lists.

Recursive implementation is elegant but requires careful handling of base cases.

### Challenges Faced

Getting the mid-index calculations correct.

Avoiding infinite loops or stack overflow in recursion.

Remembering that the list must be sorted first.

### How I Overcame Them

Practiced tracing through examples on paper.

Used sorted test lists to verify correctness.

Wrote both iterative and recursive versions to compare approaches.

## Overall Reflection

Practical 6 reinforced the importance of choosing the right search algorithm based on the data.
I now understand the efficiency differences between linear and binary search and gained confidence writing both iterative and recursive solutions.

## Future Improvements

Explore searching in more complex data structures, like trees or graphs.

Learn to combine search algorithms with Python built-in methods for optimization.