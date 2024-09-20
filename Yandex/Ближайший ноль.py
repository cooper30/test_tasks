# ID 78339489
from typing import List, Tuple


def nearest_zero_calculation(street: List[int],
                             street_length: int) -> List[int]:
    result = []
    zero_position = None

    for i, value in enumerate(street):
        if value == 0:
            zero_position = i
            result.append(0)
            continue

        result.append(
            (i - zero_position) if zero_position is not None else street_length
        )

    return result


def get_distance_to_nearest_zero(street: List[int],
                                 street_length: int) -> List[int]:
    result = []

    distance = nearest_zero_calculation(street, street_length)
    reversed_distance = (nearest_zero_calculation(street[::-1],
                                                  street_length))[::-1]

    for item in range(street_length):
        result.append(min(distance[item], reversed_distance[item]))

    return result


def read_input() -> Tuple[int, List[int]]:
    street_length = int(input())
    street = [int(num) for num in input().split(' ')]
    return street_length, street


if __name__ == '__main__':
    street_length, street = read_input()
    print(*get_distance_to_nearest_zero(street,
                                        street_length))