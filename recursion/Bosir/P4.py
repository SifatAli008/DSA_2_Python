# Write a python program to implement a recursive function to calculate the sum of digits of a given number.

def calculate_sum(n):
    if n == 0 or n<10:
        return n
    
    else:
        return n%10+calculate_sum(n//10)

def main():
    num=int(input('Number of digits : '))
    print('Sum of Digits : ',calculate_sum(num))
        
        
main()        