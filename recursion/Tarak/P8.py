#max Elemeent in array

def Max_Elemeent(arr,n):
    if n == 1:
        return arr[0]
    else:
        i = arr[n-1]
        result = Max_Elemeent(arr,n-1)
        return i if i>result else result
    
def main():
    arr =[1,2,3,4,5,6,7,8,9]
    print(Max_Elemeent(arr,len(arr))) 
    
main()         