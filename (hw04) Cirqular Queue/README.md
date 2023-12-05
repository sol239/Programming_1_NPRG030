Write a class CircularQueue that implements a queue of numbers using an array.

Your class should support the following operations:

CircularQueue(size) - create an empty CircularQueue that initially has room for 'size' elements
q.enqueue(n) - add a number at the tail of the queue
q.dequeue() - remove a number from the head of the queue, and return it
q.count() - return the number of values in the queue
q.avg() - return the average of all values in the queue
You may assume that q.dequeue() and q.avg() will never be called when the queue is empty.

The enqueue() method should run in O(1) on average. All other methods should always run in O(1).

The array holding the queue elements should always have at least one free slot. If an enqueue() operation would fill 
the last slot, then it should expand the structure to make more room. To do this, replace the array with a newly 
allocated array that is twice as big, and print a message such as

Resized to 200 elements
Important: You may not use any classes from Python's collections module (e.g. deque).

Important: Your class must be in a source file called circular_queue.py.

Do not read any input. ReCodEx will call your class's methods to test them directly.

Sample usage 1:

>>> q = CircularQueue(3)
>>> q.enqueue(5)
>>> q.enqueue(10)
>>> q.enqueue(15)
Resized to 6 elements
>>> q.count()
3
>>> q.avg()
10.0
>>> q.dequeue()
5
>>> q.dequeue()
10
>>> q.count()
1

Sample usage 2:

def sample2():
    q = CircularQueue(20)
    for x in range(10):
        q.enqueue(x)
    for x in range(5):
        q.dequeue()
    for x in range(100):
        q.enqueue(x)
    print('count =', q.count())
    print('average =', q.avg())
    print(q.dequeue())

>>> sample2()
Resized to 40 elements
Resized to 80 elements
Resized to 160 elements
count = 105
average = 47.476190476190474
5

Sample usage 3:

def sample3():
    q = CircularQueue(3)
    q.enqueue(1)
    for x in range(3):
        q.enqueue(x)
        q.dequeue()
    print('avg is', q.avg())
    print(q.dequeue())
    
>>> sample3()
avg is 2.0
2

Sample usage 4:

def sample4():
    q = CircularQueue(1)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())

>>> sample4()
Resized to 2 elements
Resized to 4 elements
1
2

Sample usage 5:

def sample5():
    q = CircularQueue(3)
    for x in range(3):
        q.enqueue(x)
    print('count is', q.count())
    sum = 0
    while q.count() > 0:
        sum += q.dequeue()
    print('sum is', sum)
    
>>> sample5()
Resized to 6 elements
count is 3
sum is 3

Sample usage 6:

def sample6():
    q = CircularQueue(1)
    for x in range(5):
        q.enqueue(x)
        q.enqueue(2 * x)
        q.dequeue()
    print('count is', q.count())
    print('avg is', q.avg())
    
>>> sample6()
Resized to 2 elements
Resized to 4 elements
Resized to 8 elements
count is 5
avg is 5.0
Hints:

In your initializer, allocate an array of the given size, initially filled with None values. For example:

self.a = size * [None]
Any approach where you sometimes need to delete an array element at the beginning (e.g. using 'a.pop(0)' or 'del a[0]') 
will be too slow, since these operations will take O(N) time.

Instead, use attributes 'self.head' and 'self.tail' to store the starting and ending indices of a range of 
array elements that hold the current queue values. For example, at some moment you might have

self.a = [ None, None, None, None, 10, 7, 5, 6, None, None ]
self.head = 4
self.tail = 8
The values in the queue at this moment are 10, 7, 5, and 6. With this approach, you can enqueue in O(1): store a value at 
the end of the active range, and increment self.tail. You can also dequeue in O(1): retrieve a value from the beginning of 
the active range, and increment self.head.

There's only one catch: what happens if the range reaches the end of the array, and you need to enqueue? For example, consider this situation:

self.a = [ None, None, None, None, 10, 7, 5, 6, 11, 2 ]
If we need to enqueue another value at this moment, we don't want to shift all the values back to the 
beginning of the array - that could take O(N) time. Instead, we will allow the range to wrap around to the 
beginning. If we enqueue the value 18, we will now have

self.a = [ 18, None, None, None, 10, 7, 5, 6, 11, 2 ]
self.head = 4
self.tail = 1
If we then enqueue 19, we will now have

self.a = [ 18, 19, None, None, 10, 7, 5, 6, 11, 2 ]
self.head = 4
self.tail = 2
An array used in this way is sometimes called a 'circular array' (hence the name of this exercise). With this 
approach, both dequeue() and enqueue() will always run in O(1), except in the case when enqueue() needs to expand the array because it is full.

To expand the array, allocate a new array and copy all elements from the old array to the new. 
(However, look out: if the active range in the old array currently wraps past the end of that array, you cannot simply copy 
them to the same positions in the new array, since they would not wrap around in the same way with the larger array size.)