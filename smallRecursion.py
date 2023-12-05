
def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n-1)

def loop_factorial(n):
    answer = 1
    while n>=1:
        answer = answer*n
        n = n-1
    return answer

def main():
    to_check = int(input("what number shall we check:"))
    print(factorial(to_check))
    print(loop_factorial(to_check))

main()
