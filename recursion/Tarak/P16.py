#Check whether a given string is palindrome or not.

def check_Palindrome(str,start,end):
    if start >= end:
        return True
    else:
        if str[start] == str[end]:
            return check_Palindrome(str, start + 1, end - 1)
        else:
            return False
def main():
     str="mad AM"
     s=str.replace(" ", "").lower()
     result = check_Palindrome(s, 0, len(s) - 1)
     
     if result:
        print("Palindrome")
     else:
        print("Not a Palindrome")
        
main()        