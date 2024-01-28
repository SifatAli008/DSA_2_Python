#Write a C++ program to calculate the factorial of a given number using recursion.

def factorial(n):
     if n==1:
         return 1;   
     else:
         return n*factorial(n-1)
     
def main():
     num=int(input('Enter a intager non-negative value: '))
     print(f'factorial of {num} number:',factorial(num))
    
main()     