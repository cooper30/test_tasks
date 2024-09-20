# ID 78257975
from typing import List, Tuple


def get_score(desired_number: int, matrix: List[str]) -> int:
    score = 0
    numbers = {k: 0 for k in range(1, 10)}

    for i in range(len(matrix)):
        for j in matrix[i]:
            if j == '.':
                continue

            numbers[int(j)] += 1

    for i in numbers.values():
        if 0 < i <= 2 * desired_number:
            score += 1

    return score


def read_input() -> Tuple[int, List[str]]:
    desired_number = int(input())
    matrix = [str(input()) for i in range(4)]
    return desired_number, matrix


if __name__ == '__main__':
    desired_number, matrix = read_input()
    print(get_score(desired_number, matrix))
