# Practical Report 2 – CSF101

## Objective

This practical focuses on implementing the Fibonacci sequence using two different approaches: **iterative** and **recursive**. The aim is to understand how both methods work, compare their logic, and observe how the same problem can be solved in multiple ways.

---

## Tasks and Solutions

### 1. Iterative Fibonacci

**Task:** Write a function that returns the *n*-th Fibonacci number using an iterative loop.

**Solution:**

```python
# Iterative Fibonacci function
# fibonacci sequence: 0 1 1 2 3 5 8 13 21

def fibonacci_iterative(n):
    """Return the nth Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example
num = 6
print(f"Iterative: Fibonacci({num}) =", fibonacci_iterative(num))
```

---

### 2. Recursive Fibonacci

**Task:** Create a recursive function that computes the *n*-th Fibonacci value.

**Solution:**

```python
# Recursive Fibonacci function
# fibonacci sequence: 0 1 1 2 3 5 8 13 21

def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example
num = 6
print(f"Recursive: Fibonacci({num}) =", fibonacci_recursive(num))
```

---

If you have more parts for Practical 2, paste them and I’ll add them below.
