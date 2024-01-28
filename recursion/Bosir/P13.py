# Calculating product of two numbers without multiplication operator

def product_of_two_numbers(x,y):
    if x==0 or y==0:
        return 0
    return x+product_of_two_numbers(x,y-1) if y>0 else -x+product_of_two_numbers(x,y+1)

def main():
    value1=int(input("Enter first number : "))
    value2=int(input("Enter first number : "))
    print (f'Product of {value1} and {value2} = {product_of_two_numbers(value1,value2)}')

main()