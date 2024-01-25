#Min Elemeent
def Min_Element(arr,n):
    if n==0:return arr[0]
    else:
        i = arr[n-1]
        result = Min_Element(arr,n-1)
        return i if i<result else result

def main():
    arr = [int(x) for x in input('Enter space-separated values for the array: ').split()]
    print("Minimume Element:",  Min_Element(arr, len(arr)))

main()
    