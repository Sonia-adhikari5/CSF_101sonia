# Practical 4 – Linked List Operations

## Objective

This practical focuses on implementing **singly linked lists**, reversing a linked list, and performing standard linked-list operations such as insertion, deletion, searching, and traversal.

---

## 1. Reversing a Linked List

The following code reverses a singly linked list using an iterative approach.

### **Code Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev becomes the new head

# Helper function to print the linked list

def printList(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements))

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

reversed_head = reverseList(head)
print("Reversed list:")
printList(reversed_head)
```

---

## 2. Singly Linked List Implementation

This linked list supports:

* **append()** – add new nodes at the end
* **display()** – print the list
* **insert()** – insert a node at a given position
* **delete()** – remove a node by value
* **search()** – return the position of a value
* **reverse()** – reverse the entire list

### **Code Solution:**

```python
# Singly Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Testing the LinkedList
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()           # Output: 1 -> 2 -> 3

ll.insert(4, 1)
ll.display()           # Output: 1 -> 4 -> 2 -> 3

ll.delete(2)
ll.display()           # Output: 1 -> 4 -> 3

print(ll.search(4))    # Output: 1
print(ll.search(5))    # Output: -1

ll.reverse()
ll.display()           # Output: 3 -> 4 -> 1
```

---

End of Practical 4.
