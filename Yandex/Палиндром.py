def is_palindrome(line: str) -> bool:
    current_line = (''.join(c for c in line if c.isalnum())).lower()
    reverse_line = current_line[::-1]
    if current_line == reverse_line:
        return True
    return False


print(is_palindrome(input().strip()))