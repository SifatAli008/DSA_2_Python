# Write a python program to implement a recursive function to check if a given string is a palindrome.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    
def check_palindrome(strings, index=0):
    if index == len(strings):
        return
    
    print(f"{strings[index]}: ",is_palindrome(strings[index]))
    
    check_palindrome(strings, index + 1)

def main():
    strings = ["radar", "hello", "level", "racecar"]
    check_palindrome(strings)

main()
