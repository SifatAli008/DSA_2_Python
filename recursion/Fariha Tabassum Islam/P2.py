#Write a recursive program to calculate the power of x (x^y), where y is a non-negative integer.

def Power_Of_Element(base, n):
    if n == 0:
        return 1

    half = Power_Of_Element(base, n // 2)
    return half * half if n % 2 == 0 else base * half * half

def main():
    base = int(input('Enter a Non-Negative value: '))
    n = int(input('Enter a non-negative exponent value: '))
    print(f'The result of {base}^{n} is: {Power_Of_Element(base, n)}')


main()
