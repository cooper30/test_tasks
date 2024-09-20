def get_longest_word(line: str) -> str:
    dictionary = line.split()

    max_word = ''
    max_word_len = 0

    for item in dictionary:
        i = len(item)
        if max_word_len < i:
            max_word = item
            max_word_len = i

    return max_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
