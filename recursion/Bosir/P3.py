#Write a python program to implement a recursive function to get the nth Fibonacci number.

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo(n-1)+ fibo(n-2)

def main():
    num=int(input('Enter a intager non-negative value: '))
    print(f'{num}th Fibonacci of number:',fibo(num))
    
main()      