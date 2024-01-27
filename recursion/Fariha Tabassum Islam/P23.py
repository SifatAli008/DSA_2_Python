#Write a recursive program to find the sum of digits of an integer.

def sum_of_digits(n):
    if n == 0 or  n<10:
        return n
    else:
        return n%10+sum_of_digits(n//10)

def main():
    num=int(input('Enter a value : '))
    print(f'The Sum of digits in {num} is: ',sum_of_digits(num))

main()    