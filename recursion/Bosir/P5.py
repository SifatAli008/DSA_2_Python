#Write a python program to implement a recursive function to find the maximum and minimum elements in an array.

def max(arr,n):
    if n==0:
        return arr[0]
    else:
        return arr[n-1]  if arr[n-1] > max(arr,n-1) else max(arr,n-1)
    
def min(arr,n):
    if n==0:
        return arr[0]
    else:
        return arr[n-1]  if arr[n-1] < min(arr,n-1) else min(arr,n-1)
    
def main():
    arr = [int(x) for x in input('Enter space-separated values for the array: ').split()]
    print('Max value of arr: ',max(arr,len(arr)))
    print('Max value of arr: ',min(arr,len(arr)))
    
main()    