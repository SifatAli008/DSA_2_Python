#Write a recursive program to find the average of the elements of an array of size n

def calculate_sum_of_array(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + calculate_sum_of_array(arr, n - 1)

def calculate_average_of_array(arr, n):
    array_sum = calculate_sum_of_array(arr, n)
    return array_sum / n if n != 0 else 0

def main():
    arr = [1, 2, 3, 4]
    print('Printing array elements:')
    result = calculate_average_of_array(arr, len(arr))
    print('Average of elements:', result)


main()
