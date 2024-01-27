#Write a recursive implementation of the factorial function. Recall that n! =
#1 × 2 × ... × n, with the special case that 0! = 1.

def fact(n):
    if n==1:
        return 1
    else:
     return n*fact(n-1)
 
def main():
    num=int(input('Enter a Intager Number : '))   
    print('factorial of ',num,':',fact(num))
    
main()    