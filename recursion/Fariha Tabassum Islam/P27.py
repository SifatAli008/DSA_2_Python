#Write a recursive implementation of binary search in a sorted array.

def Bin_Search(arr, start, end, value):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return Bin_Search(arr, mid + 1, end, value)
        else:
            return Bin_Search(arr, start, mid - 1, value)
    else:
        return -1 

def main():
    arr = [2, 10, 25, 29, 32, 48]
    value_to_search = 29
    result = Bin_Search(arr, 0, len(arr) - 1, value_to_search)

    if result:
        print(f"Element {value_to_search} found at index {result}")
    else:
        print(f"Element {value_to_search} not found in the array.")

main()
