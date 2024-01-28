# Write a C++ program to implement a recursive function to find the sum of all prime numbers in a given range.

def prime(num, divisor=2):
    if num <= 2:
        return num == 2
    
    if num % divisor == 0:
        return False
    
    return True if divisor * divisor > num else prime(num, divisor+1)
    
def sum_of_primes(start, end):
    if start == end:
        return 0
    
    return start + sum_of_primes(start+1, end) if prime(start) else sum_of_primes(start + 1, end)

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    print("Sum of prime numbers in the range:", sum_of_primes(start, end))

main()
