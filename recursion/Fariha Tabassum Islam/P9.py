#Write a recursive program to find the products of the elements of an array of size n.

def print_product_of_array(arr,n):
    if n==1:
       return 1
    else:
        return n*print_product_of_array(arr,n-1)    
 
def main():
    arr=[1,2,3,4]  
    print('Printing array Element : ')  
    result=print_product_of_array(arr,len(arr))
    print('Product of elements: ',result)
main()    