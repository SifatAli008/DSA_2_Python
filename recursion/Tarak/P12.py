#Count the number of digits of a given number n.

def count_digits(n):
    if n == 0:
        return 0
    else :
      n=n//10
      return 1+count_digits(n);  


def main():
    n=int(input('Enter the digits :'))
    print('Sum of digits',count_digits(n))
    
main()        