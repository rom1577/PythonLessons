def is_recursive_palindrome(string: str, i:int):
    if i > len(string) // 2:
        return True
    if string[i-1] == string[-i]:
        i += 1
        return is_recursive_palindrome(string, i)
    return False

# основная функция для вызова
def is_palindrome(string: str):
    string = ''.join(string.split())
    string = string.lower()
    i = 1
    if is_recursive_palindrome(string, i):
        return True
    return False

