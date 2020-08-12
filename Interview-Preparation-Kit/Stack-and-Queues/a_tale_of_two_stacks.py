class MyQueue(object):
    def __init__(self):
        self.head = []
        self.tail = []

    def peek(self):
        if not self.tail:
            self.tail = list(reversed(self.head))
            self.head = []
        return self.tail[-1]

    def pop(self):
        head = self.peek()
        del self.tail[-1]
        return head

    def put(self, value):
        self.head.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())