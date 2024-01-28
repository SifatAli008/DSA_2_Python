#Write a python program to find the sum of all elements in an array using recursion.

def sum_of_elements(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + sum_of_elements(arr, n-1)

def main():
    arr = [int(x) for x in input('Enter space-separated values for the array: ').split()]
    
    print('Sum of elements:', sum_of_elements(arr,len(arr)))

main()
