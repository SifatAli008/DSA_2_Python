#Write a recursive program to print an array of size n in reverse order.



def print_array_reverse(arr,n):
    if n==0:
        print(arr[0],end=' ')
    else:
        print(arr[n],end=' ')
        print_array_reverse(arr,n-1)
         
 
def main():
    arr=[1,2,3,4,5,6,7,8,9]  
    print('Printing array Element : ')  
    print_array_reverse(arr,len(arr)-1)
    
main()    