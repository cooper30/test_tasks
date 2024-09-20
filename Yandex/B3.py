# ID 80468544


class Player:
    def __init__(self, name, number_solved_task, fine):
        self.name = name
        self.number_solved_task = number_solved_task
        self.fine = fine

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return (
            (-self.number_solved_task, self.fine, self.name) <
            (-other.number_solved_task, other.fine, other.name)
        )


def quicksort(players: list, start: int=0, end: int=0) -> None:

    def __partition(low, high):
        if low >= high:
            return

        left = low
        right = high
        pivot = players[(right + left) // 2]

        while left <= right:
            while players[left] < pivot:
                left += 1

            while players[right] > pivot:
                right -= 1

            if left <= right:
                players[left], players[right] = players[right], players[left]
                left += 1
                right -= 1

        __partition(low, right)
        __partition(left, high)

    __partition(start, end - 1)


if __name__ == '__main__':
    number = int(input())
    players = []
    for _ in range(number):
        name, number_solved_task, fine = input().split()
        players.append(
            Player(
                name=name,
                number_solved_task=int(number_solved_task),
                fine=int(fine)
            )
        )
    quicksort(players, end=number)
    print(*players, sep='\n')
