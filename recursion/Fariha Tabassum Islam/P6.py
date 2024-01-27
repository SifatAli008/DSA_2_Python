#Write a recursive program to print an array of size n in given order.

def print_array(arr,n):
    if n==0:
        print(arr[0],end=' ')
    else:
        print_array(arr,n-1)
        print(arr[n],end=' ') 
 
def main():
    arr=[1,2,3,4,5,6,7,8,9]  
    print('Printing array Element : ')  
    print_array(arr,len(arr)-1)
    
main()    