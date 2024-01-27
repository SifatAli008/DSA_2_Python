 #Find the sum of the following series up to nth position / Print the following series up to nth position.
 #2 ∗ 3 + 4 ∗ 5 + 8 ∗ 7 + 16 ∗ 9 + ⋯
   
def sum_of_series_elements(n):
    if n==0:
        return 0
    return (2**n)*((2*n)+1)+sum_of_series_elements(n-1)
 
def main():
    num= int(input('Number of nth positions :'))
    print('Sum of Series :',sum_of_series_elements(num))
                  
main()