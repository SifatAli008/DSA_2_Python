#Write a recursive program to check if a given positive integer is a palindrome or not. An integer is a palindrome when it reads the same backward as forward.

def is_palindrome(n):
   
    num_str = str(n)
    
    if len(num_str) <= 1:
        return True
    elif num_str[0] == num_str[-1]: 
        return is_palindrome(num_str[1:-1])
    else:
        return False

def main():
    num = int(input('Enter a positive integer: '))
    
    if num < 0:
        print("Please enter a positive integer.")
    elif is_palindrome(num):
        print(f'{num} is a palindrome.')
    else:
        print(f'{num} is not a palindrome.')

main()
