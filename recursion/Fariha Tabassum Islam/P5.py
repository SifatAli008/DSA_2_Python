#Write a recursive program to print the even numbers in a given range.
#Sample input    Sample output
#3 10             4 6 8 10

def even_numbers_to_n(m,n):
    if m>n:
        return
    if m%2==0:
        print(m, end=' ')
    even_numbers_to_n(m+1,n)

def main():
    start=int(input('Enter start number : '))
    end=int(input('end end number : '))       
    even_numbers_to_n(start,end)    

main()
