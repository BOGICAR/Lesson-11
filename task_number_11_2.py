# Задание №2 - сделано
def u_input() -> str:
    user_input = str(input())
    return user_input


def check_palindrome():
    us_input = u_input()
    palindrome = us_input[::-1]
    if palindrome == us_input:
        return True
    else:
        return False


print(check_palindrome())
