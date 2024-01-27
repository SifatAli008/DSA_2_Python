#Write a recursive program to find the sum of the elements of an array of size n.

def print_sum_of_array(arr,n):
    if n==0:
       return 0
    else:
        return n+print_sum_of_array(arr,n-1)    
 
def main():
    arr=[1,2,3,4]  
    print('Printing array Element : ')  
    result=print_sum_of_array(arr,len(arr))
    print('Sum of elements: ',result)
main()    