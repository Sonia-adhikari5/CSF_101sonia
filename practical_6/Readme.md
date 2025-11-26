### Practical 6 — Searching Algorithms
1. Linear Search
Problem

Search for a target value in an unsorted list by checking each element one by one.

Most Optimal Solution (for UNSORTED lists)

Linear search is the best approach because you cannot use binary search unless the list is sorted.

Short Code
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

2. Binary Search (Iterative)
Problem

Search for a target value in a sorted list using the divide-and-conquer method.

Most Optimal Solution

Binary search → O(log n)
Works only when the list is already sorted.

Short Code
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

3. Recursive Binary Search
Problem

Same as binary search, but using recursion instead of a loop.

Most Optimal Solution

Uses the same O(log n) complexity but with recursive calls.

Short Code
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)