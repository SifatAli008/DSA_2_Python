 #Find the sum of the following series up to nth position / Print the following series up to nth position.
 #1^2 + 2^2 + 3^2 + ⋯
 
def sum_of_series_elements(n):
    if n==1:
        return 1
    return n*n+sum_of_series_elements(n-1)
 
def main():
    num= int(input('Number of nth positions :'))
    print('Sum of Series :',sum_of_series_elements(num))
                  
main()