en
Write a Python class TreeSet that stores a set of values in a binary search tree.

Your class should support the following operations:

TreeSet() - create a TreeSet
ts.contains(x) - True if x is in the set
ts.add(x) - add x to the set if not already present
ts.remove(x) - remove x from the set if present
ts.min() - return the smallest value in the set, or None if the set is empty
ts.max() - return the largest value in the set, or None if the set if empty
ts.size() - return the total number of values in the set
ts.count(lo, hi) - return the number of values x in the set such that lo <= x <= hi
count() should only explore parts of the tree that might contain values between lo and hi. If it always explores the entire tree (i.e. always takes O(N)), it will be not be efficient enough to pass the tests.

size() should run in O(1). All other operations should run in O(h), where h is the height of the binary tree.

If a node has two children, remove() should replace its value with the smallest value in the node's right subtree.

Do not read any input or write any output; ReCodEx will call your methods to test them.

Important: Your class must be in a source file named tree_set.py.

Sample usage #1:

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

>>> sample1()
None
None
size = 5
min = 2
max = 10
t.contains(8) = True
t.contains(8) = False
size = 4
t.count(3, 7) = 2
Sample usage #2:

def sample2():
    t = TreeSet()
    a = [5, 2, 3, 4, 1]
    for x in a:
        t.add(x)
    for x in a:
        print(t.contains(x))
        t.remove(x)
        print(t.contains(x))
    t.remove(5)
    print(t.size())

>>> sample2()
True
False
True
False
True
False
True
False
True
False
0
Sample usage #3:

def sample3():
    t = TreeSet()
    a = [10, 5, 3, 8]
    for x in a:
        t.add(x)
    for x in [5, 8, 3, 10]:
        print(t.contains(x))
        t.remove(x)
        print(t.contains(x))
    print(t.size())

>>> sample3()
True
False
True
False
True
False
True
False
0
Sample usage #4:

def sample4():
    t = TreeSet()
    a = [10, 5, 20, 2]
    for x in a:
        t.add(x)
    for x in a:
        print(t.contains(x))
        t.remove(x)
        print(t.contains(x))
    print(t.size())

>>> sample4()
True
False
True
False
True
False
True
False
0
Sample usage #5:

def sample5():
    t = TreeSet()
    a = [3, 9, 5, 4, 8, 2, 10]
    for x in a:
        t.add(x)
    for x in a:
        print(t.contains(x))
        t.remove(x)
        print(t.contains(x))

>>> sample5()
True
False
True
False
True
False
True
False
True
False
True
False
True
False
Sample usage #6:

def sample6():
    t = TreeSet()
    t.add(20)
    t.remove(15)
    print(t.size())
    for x in [10, 30, 25, 40, 28]:
        t.add(x)
    t.remove(20)
    print(t.contains(28))

>>> sample6()
1
True
Sample usage #7:

def sample7():
    t = TreeSet()
    for x in [10, 20, 15]:
        t.add(x)
    t.remove(20)
    print(t.contains(13))
    
>>> sample7()
False
Sample usage #8:

def sample8():
    t = TreeSet()
    for x in [10, 20, 15, 18]:
        t.add(x)
    t.remove(20)
    print(t.contains(18))
    
>>> sample8()
True
Hints:

You may want to review our lecture notes on binary search trees.

I recommend implementing count() using a recursive helper function outside the TreeSet class that takes 3 arguments: a Node, lo, and hi. Your count() method will call the recursive helper and will pass self.root to begin the recursion.

remove() is the most challenging method to implement. First, here's a word of warning. In remove(), suppose that you have a local variable n that points to a node containing the value you want to remove. Sometimes students think that in this situation they can remove the node by assigning "n = None". Actually this statement has no effect on the data structure! It merely assigns None to a local variable. Instead, you need to determine who points to the node n (i.e. either n's parent, or the TreeSet object itself if n is the root) and change their pointer to point to None instead.

There are various possible ways to write this method. As one possible iterative approach, walk down the tree and use an extra variable to remember the current node's parent (if any). Then, when you reach the node to remove you'll know which pointer to update. The following helper method might be useful:

  # Given a node n and its parent (if any), replace n with a node p.
  def replace(self, parent, n, p):
      if parent == None:      # n is the root
          self.root = p
      elif parent.left == n:  # n is the left child
          parent.left = p
      elif parent.right == n: # n is the right child
          parent.right = p
      else:
          assert False, 'not a child'
Your remove() method might look something like this:

  def remove(self, x):
      n = self.root
      parent = None
  
      while n != None:
          if x < n.val:
              parent = n
              n = n.left    # go left
          elif x > n.val:
              ...
          else:   # x == n.val
              if n.left == None and n.right == None:
                  self.replace(parent, n, None)   # replace n with None
              elif ...
As another possible approach, write remove() using a recursive helper function outside the TreeSet class that takes a pointer to a root node plus an element to remove, and returns an updated version of the tree.

Details
Deadline:	12/12/2023 23:59 in 5 days
Points limit:	10
Correctness threshold:	0 %
Allowed environments:	Python
Submission attempts:	0 / 50
Solution file restrictions:	10 files, 256 KiB total

Submitted Solutions
Date of submission	Validity	Points	Target language	
No solutions were submitted yet.
