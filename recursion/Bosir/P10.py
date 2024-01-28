#Write a C++ program to implement a recursive function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    num1 = input("Enter the first number : ")
    num2 = input("Enter the Second number : ")
    print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
    
main()    
