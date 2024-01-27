#Write a recursive program to find the LCM of x and y where x, y are positive integers.

def gcd(x, y):
    if y==0:
        return x 
    else:
        return gcd(x, x%y)

def lcm(x, y):
    return (x * y) // gcd(x, y)    
 
def main():
    num1 = 48
    num2 = 18
    result_gcd = gcd(num1, num2)
    result_lcm = lcm(num1, num2)

    print(f"The GCD of {num1} and {num2} is: {result_gcd}")
    print(f"The LCM of {num1} and {num2} is: {result_lcm}")
    
main() 