# Write a recursive program to check if a given string is a palindrome or not (not case sensitive, ignore whitespaces)
#Sample input Sample output
#Evil olive        True
#Too bad           False

def check_palindrome(s, start, end):
    if start >= end:
        return True
    else:
        if s[start] == s[end]:
            return check_palindrome(s, start + 1, end - 1)
        else:
            return False

def main():
    user_input = input('Enter a string: ')
    s = user_input.replace(" ", "").lower()
    result = check_palindrome(s, 0, len(s) - 1)

    if result:
        print("Palindrome")
    else:
        print("Not a Palindrome")


main()
