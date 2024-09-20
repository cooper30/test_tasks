class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.qsize = 0

    def is_empty(self):
        return self.qsize == 0

    def push(self, x):
        if self.qsize != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.qsize += 1
            return 'OK'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.qsize -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.qsize


if __name__ == '__main__':
    number = int(input())
    queue_length = int(input())
    stack = MyQueueSized(queue_length)
    result_list = []
    for index in range(number):
        command = input().split()
        if command[0] == 'push':
            result = stack.push(int(command[1]))
            if result == 'error':
                result_list.append(result)
        if command[0] == 'pop':
            result_list.append(stack.pop())
        if command[0] == 'peek':
            result_list.append(stack.peek())
        if command[0] == 'size':
            result_list.append(stack.size())

    for index in result_list:
        print(index)