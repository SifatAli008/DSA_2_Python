#Write a recursive program to find the GCD of x and y where x, y are positive integers.

def gcd(x, y):
    if y==0:
        return x 
    else:
        return gcd(x, x%y)
 
def main():
     num1 = 48
     num2 = 18
     result = gcd(num1, num2)
     print(f"The GCD of {num1} and {num2} is: {result}")
    
main()    