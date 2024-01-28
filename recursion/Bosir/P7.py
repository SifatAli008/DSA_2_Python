#Write a python program to implement a recursive function to calculate the power of a number.

def pow(base, n):
    if n == 0:
        return 1
    else:
        half = pow(base, n // 2)
        return half * half if n % 2 == 0 else base * half * half

def main():
    base = int(input('Enter base value: '))
    n = int(input('Enter power of n: '))
    
    print(f'{n} Power of {base}:', pow(base, n)) 

main()
