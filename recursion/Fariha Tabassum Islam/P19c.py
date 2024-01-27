 #Find the sum of the following series up to nth position / Print the following series up to nth position.
 #1 ∗ 3 + 2 ∗ 5 + 3 ∗ 7 + 4 ∗ 9 + ⋯
   
def sum_of_series_elements(n):
    if n==0:
        return 0
    
    return n*((2*n)+1)+sum_of_series_elements(n-1)
 
def main():
    num= int(input('Number of nth positions :'))
    print('Sum of Series :',sum_of_series_elements(num))
                  
main()