#Write a python program to reverse a string using recursion.

def reverse(s, n):
    if n == 0:
        return ''
    else:
        return s[n-1] + reverse(s, n-1)

def main():
    str = input('Enter a string: ')
    reversed_string = reverse(str, len(str))
    print('Reversed string:', reversed_string)

main()
