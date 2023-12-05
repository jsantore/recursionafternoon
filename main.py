
def is_palindrome(string_to_check):
    if string_to_check =='':
        return True
    if len(string_to_check) ==1:
        return True
    if string_to_check[0] != string_to_check[-1]:
        return False
    return is_palindrome(string_to_check[1:-1])


def main():
    to_check = input("What string should I check:")
    print(is_palindrome(to_check))

main()