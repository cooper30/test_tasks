#ID 79813506

ERROR_MESSAGE = 'error'

class Deque:
    """Cтруктура данных Дек"""

    def __init__(self, max_size):
        """Инициализация класса"""
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        """Метод по проверки на пустой дек"""
        return self.__size == 0

    def is_full_queue(self):
        """Метод по проверки на заполненность дека"""
        return self.__size == self.__max_size

    def __get_index(self, method):
        if method in ('push_back', 'push_front'):
            if self.is_empty():
                self.__head = 0
                self.__tail = 0
                return 0
            if method == 'push_back':
                return (self.__tail + 1) % self.__max_size
            else:
                return (self.__head - 1) % self.__max_size
        if method == 'pop_back':
            return (self.__tail - 1) % self.__max_size
        if method == 'pop_front':
            return (self.__head + 1) % self.__max_size

    def __push(self, method, value):
        """
        Общий метод по добавлению элемента
        """
        if self.is_full_queue():
            raise RuntimeError(ERROR_MESSAGE)

        if method == 'push_back':
            self.__tail = self.__get_index(method=method)
            self.__queue[self.__tail] = value
        if method == 'push_front':
            self.__head = self.__get_index(method=method)
            self.__queue[self.__head] = value

        self.__size += 1

    def __pop(self, method):
        """
        Общий метод по получению элемента дека с последующим удалением его
        """
        if self.is_empty():
            raise RuntimeError(ERROR_MESSAGE)

        if method == 'pop_front':
            value = self.__queue[self.__head]
            self.__head = self.__get_index(method='pop_front')
        if method == 'pop_back':
            value = self.__queue[self.__tail]
            self.__tail = self.__get_index(method='pop_back')
        self.__size -= 1

        return value

    def push_back(self, value):
        """Метод по добавлению элемента в конец дека"""
        self.__push(method='push_back', value=value)

    def push_front(self, value):
        """Метод по добавлению элемента в начало дека"""
        self.__push(method='push_front', value=value)

    def pop_back(self):
        """
        Метод по получению последний элемент дека с последующим удалением его
        """
        return self.__pop('pop_back')

    def pop_front(self):
        """
        Метод по получению первого элемент дека с последующим удалением его
        """
        return self.__pop('pop_front')


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().strip().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except RuntimeError:
            print(ERROR_MESSAGE)