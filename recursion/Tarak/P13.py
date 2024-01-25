# Print the array elements.

def print_array(arr, n):
    if n == 1:
        print(arr[0], end=' ')
    else:
        print_array(arr, n - 1)
        print(arr[n - 1], end=' ')

def main():
    arr = [int(x) for x in input('Enter space-separated elements of Array: ').split()]
    print('Array elements:')
    print_array(arr, len(arr))


main()
