#ID 79813786

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

class Stack:
    def __init__(self):
        """Инициализация класса"""
        self.__queue = []

    def push(self, item):
        """Добавление в очередь"""
        self.__queue.append(item)

    def pop(self):
        """Получение значения из очереди с последующим удалением"""
        try:
            return self.__queue.pop()
        except IndexError:
            raise IndexError('Нет данных для расчета.')


def calculator(values):
    """Рассчитать"""
    stack = Stack()

    for item in values:
        try:
            if item not in OPERATORS:
                stack.push(int(item))
            else:
                operand1, operand2 = stack.pop(), stack.pop()
                stack.push(int(OPERATORS[item](operand2, operand1)))
        except ZeroDivisionError:
            raise ZeroDivisionError('Ошибка деления на ноль.')
        except TypeError:
            raise TypeError(f'Невозможно преобразовать {item}')

    return stack.pop()


if __name__ == '__main__':
    input_values = input().split()
    print(calculator(input_values))