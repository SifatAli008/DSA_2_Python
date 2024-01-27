def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_number(n // 10, rev)

def is_palindrome(n):
    reversed_num = reverse_number(n)
    return n == reversed_num

def main():
  number = int(input("Enter a positive integer: "))
  
  if number < 0:
        print("Please enter a positive integer.")
  elif is_palindrome(number):
     print(f"{number} is a palindrome.")
  else:
     print(f"{number} is not a palindrome.")
    
main()
