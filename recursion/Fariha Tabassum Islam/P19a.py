#Find the sum of the following series up to nth position / Print the following series up to nth position.
# 1 + 2 + 3 + ⋯

def sum_of_digits(n):
    if n == 0:
        return 0  
    elif n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

def main():
    num= int(input('Number of nth positions :'))
    print('Sum of Series :',sum_of_digits(num))
                  
main()