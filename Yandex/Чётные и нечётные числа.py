def check_type(number: int) -> int:
    if number % 2 == 0:
        return 1

    return 0


def check_parity(a: int, b: int, c: int) -> bool:
    if (check_type(a) + check_type(b) + check_type(c)) in (0, 3):
        return True

    return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
