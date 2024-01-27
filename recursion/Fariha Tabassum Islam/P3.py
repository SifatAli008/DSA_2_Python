#Write a recursive program to print the nth Fibonacci number.

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

def main():
    num=int(input("Enter a  Non-negative number : "))
    print(f'{num}Number of Fibonacci numbers : {fibo(num)}')

main()    