# ID 80468440


def broken_search(arr: list, search_value: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == search_value:
            return middle
        elif arr[start] <= arr[middle]:
            if arr[start] <= search_value < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if arr[middle] < search_value <= arr[end]:
                start = middle + 1
            else:
                end = middle - 1

    return -1


if __name__ == '__main__':
    number = int(input())
    search_value = int(input())
    arr = [int(num) for num in input().split()]

    print(broken_search(arr, search_value))
