#Write a recursive program to print the odd/even numbers of an array of n integers

def even_numbers_to_n(arr, n):
    if n == 0:
        return 
    even_numbers_to_n(arr, n - 1)
    
    if arr[n - 1] % 2 == 0:
        print(arr[n - 1], end=' ')

def odd_numbers_to_n(arr, n):
    if n == 0:
        return
    odd_numbers_to_n(arr, n - 1)
    if arr[n - 1] % 2 != 0:
        print(arr[n - 1], end=' ')
        
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Even numbers in array:')
    even_numbers_to_n(arr, len(arr))
    print('\nOdd numbers in array:')
    odd_numbers_to_n(arr, len(arr))


main()

