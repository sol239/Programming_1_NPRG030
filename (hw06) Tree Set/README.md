 # TreeSet Implementation in Python

## Description

Write a Python class `TreeSet` that stores a set of values in a binary search tree.

### Operations Supported

- `TreeSet()`: Create a TreeSet.
- `ts.contains(x)`: True if x is in the set.
- `ts.add(x)`: Add x to the set if not already present.
- `ts.remove(x)`: Remove x from the set if present.
- `ts.min()`: Return the smallest value in the set, or None if the set is empty.
- `ts.max()`: Return the largest value in the set, or None if the set if empty.
- `ts.size()`: Return the total number of values in the set.
- `ts.count(lo, hi)`: Return the number of values x in the set such that lo <= x <= hi.

### Additional Requirements

- `count()` should only explore parts of the tree that might contain values between lo and hi.
- `size()` should run in O(1).
- All other operations should run in O(h), where h is the height of the binary tree.
- If a node has two children, `remove()` should replace its value with the smallest value in the node's right subtree.

## Implementation Details

- Your class must be in a source file named `tree_set.py`.

## Sample Usage

### Sample #1

```python
def sample1():
    t = TreeSet()
    print(t.min())
    print(t.max())
    for x in [4, 2, 8, 6, 10]:
        t.add(x)
    t.add(4)
    print('size =', t.size())
    print('min =', t.min())
    print('max =', t.max())
    print('t.contains(8) =', t.contains(8))
    t.remove(8)
    print('t.contains(8) =', t.contains(8))
    print('size =', t.size())
    print('t.count(3, 7) =', t.count(3, 7))

# sample1()
# Output:
# None
# None
# size = 5
# min = 2
# max = 10
# t.contains(8) = True
# t.contains(8) = False
# size = 4
# t.count(3, 7) = 2
