#Write a recursive program to find the minimum of the elements of an array of size n

def min_element_of_array(arr,n):
    if n==0:
       return arr[0]
    else:
     i=arr[n-1]
     return i if i<min_element_of_array(arr,n-1) else min_element_of_array(arr,n-1)
 
def main():
    arr =[10,22,3,14,50,6,47,19,9]
    print(min_element_of_array(arr,len(arr))) 
    
main()          