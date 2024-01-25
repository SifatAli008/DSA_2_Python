# Print the array elements in revers.

def reverse_print(arr, n):
    if n == 1:
        print(arr[0], end=' ')
    else:
        print(arr[n-1], end=' ')
        reverse_print(arr, n-1)

def main():
    arr = [int(x) for x in input('Enter space-separated elements of Array: ').split()]
    print('Array elements in reverse:')
    reverse_print(arr, len(arr))


main()
