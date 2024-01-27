#Write a recursive program to find the maximum of a 2d array.

def max_element_in_2d_array(arr, m, n):
    if m == 1 and n == 1:
        return arr[0][0]
    elif m == 1:
        return max(arr[0][:n])
    elif n == 1:
        return max(arr[i][0] for i in range(m))
    else:
        max_of_row = max_element_in_2d_array(arr, m - 1, n)
        max_of_column = max_element_in_2d_array(arr, m, n - 1)
        return max(max_of_row, max_of_column, arr[m - 1][n - 1])

def main():
    arr = [[1, 2, 3,
            4, 5, 6,
            7, 8, 9]]

    m = len(arr)
    n = len(arr[0])
    result = max_element_in_2d_array(arr, m, n)
    print(f'Max element in 2D array: {result}')


main()
