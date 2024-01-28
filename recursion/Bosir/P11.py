#Counting occurrences of an element in an array with recursive function
def count_occurrences(arr, size, value):
    
    if size == 0:
        return 0
    
    count = 1 if arr[size - 1] == value else 0
    return count + count_occurrences(arr, size - 1, value)

def main():
    arr = [1, 2, 3, 4, 5, 6, 4, 4]
    value = int(input("Enter a number : "))
    print("Number of occurrences of", value, "in the array:", count_occurrences(arr, len(arr), value))

main()
