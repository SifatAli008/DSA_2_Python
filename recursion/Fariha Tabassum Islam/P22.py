#Write a recursive program to count the number of digits of an integer.

def count_digits(n):
     n = abs(n)  # Handle negative numbers
     if n < 10:
        return 1
     else:
        return 1 + count_digits(n // 10)

def main():
    num = int(input('Enter a value: '))
    print(f'The number of digits in {num} is:', count_digits(num))

main()
