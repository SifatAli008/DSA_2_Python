#Binary Search

def binary_search(arr, start, end, value):
    if start <= end:
        mid = (start + end) // 2

        if arr[mid] == value:
            return mid  
        elif value < arr[mid]:
            return binary_search(arr, start, mid - 1, value) 
        else:
            return binary_search(arr, mid + 1, end, value)  
    else:
     return -1 

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = int(input("Enter the value to search: "))

    result = binary_search(arr, 0, len(arr) - 1, value)

    if result:
        print(f"Element {value} found at index {result}.")
    else:
        print(f"Element {value} not found in the array.")


main()
