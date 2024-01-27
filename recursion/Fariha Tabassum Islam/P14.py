#Write a recursive program to print the prime numbers of an array of n integers

def is_palindrome(num_str):
    if len(num_str) <= 1:
        return True
    elif num_str[0] != num_str[-1]:
        return False
    else:
        return is_palindrome(num_str[1:-1])

def palindrome_in_array(arr, n):
    if n == 0:
        return is_palindrome(str(arr[0]))
    else:
        return is_palindrome(str(arr[n])) or palindrome_in_array(arr, n - 1)

def main():
    arr = [121, 1331, 555, 1221, 78987]
    result = palindrome_in_array(arr, len(arr) - 1)

    if result:
        print('There is a palindrome in the array.')
    else:
        print('There is no palindrome in the array.')


main()
