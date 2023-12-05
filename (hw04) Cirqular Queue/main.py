
class CircularQueue:

    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.tail = -1
        self.head = -1
        self.real_size = 0
        self.queue_sum = 0

    def enqueue(self, data):

        if self.tail == self.size:
            self.tail = 0
        if (self.is_full()) == False:
            # print(self.tail)
            # print(self.size)
            # print(self.real_size)
            # print()
            self.queue[self.tail] = data
            self.queue_sum += self.queue[self.tail]
            self.tail += 1
            self.real_size += 1

        if self.is_full() == True:
            temp_tail = [self.tail][0]
            if self.head >= self.tail:
                self.head += self.size

            self.queue[self.tail:self.tail] = [None] * self.size

            self.tail += self.size
            self.size *= 2

            print(f"Resized to {self.size} elements")
            self.tail = temp_tail

    def dequeue(self):
        if self.head == self.size:
            self.head = 0
        # print(self.head)
        # print(self.size)
        # print(self.real_size)
        # print()
        # input()
        self.queue_sum -= self.queue[self.head]
        temp = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        self.real_size -= 1

        return temp


        #print("H:", self.head)
        #print("T:", self.tail)
    def display_queue(self):
        print(self.queue)


    def is_empty(self):
        if self.real_size == 0:
            return True
        else:
            return False
    def is_full(self):
        if self.real_size == self.size:
            return True
        else:
            return False

    def count(self):
        return self.real_size
    def avg(self):
        return self.queue_sum / self.real_size



# def sample1():
#     q = CircularQueue(3)
#     q.enqueue(5)
#     q.enqueue(10)
#     q.enqueue(15)
#     # Resized to 6 elements
#     print(q.count())
#     print(3)
#     print(q.avg())
#     print(10.0)
#     print(q.dequeue())
#     print(5)
#     print(q.dequeue())
#     print(10)
#     print(q.count())
#     print(1)
#
# sample1()

# def sample2():
#     q = CircularQueue(20)
#     for x in range(10):
#         q.enqueue(x)
#     for x in range(5):
#         q.dequeue()
#     for x in range(100):
#         q.enqueue(x)
#     print('count =', q.count())
#     print('average =', q.avg())
#     print(q.dequeue())
#
# sample2()

# def sample3():
#     q = CircularQueue(3)
#     q.enqueue(1)
#     for x in range(3):
#         q.enqueue(x)
#         q.dequeue()
#     print('avg is', q.avg())
#     print(q.dequeue())
#
# sample3()

# def sample4():
#     q = CircularQueue(1)
#     q.enqueue(1)
#     q.enqueue(2)
#     print(q.dequeue())
#     print(q.dequeue())
#
# sample4()

# def sample5():
#     q = CircularQueue(3)
#     for x in range(3):
#         q.enqueue(x)
#     print('count is', q.count())
#     sum = 0
#     while q.count() > 0:
#         sum += q.dequeue()
#     print('sum is', sum)
#
# sample5()

def sample6():
    q = CircularQueue(1)
    for x in range(5):
        q.enqueue(x)
        q.enqueue(2 * x)
        q.dequeue()

    print('count is', q.count())
    print('avg is', q.avg())
sample6()