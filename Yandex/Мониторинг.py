from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []

    for i in range(col):
        for j in range(row):
            result.append(matrix[j][i])

    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    row = int(input())
    col = int(input())
    matrix = []
    for i in range(row):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))