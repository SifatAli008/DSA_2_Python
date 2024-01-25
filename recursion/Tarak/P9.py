#max Elemeent in array

def recursion(arr, n):
    if n == 1: return arr[0]
    else:  
        i = arr[n - 1]  
        result = recursion(arr, n - 1)
        return i if i > result else result


def main():
   
    arr = [int(x) for x in input('Enter space-separated values for the array: ').split()]
    length = len(arr)
    print("Maximum Element:", recursion(arr, length))

main()
