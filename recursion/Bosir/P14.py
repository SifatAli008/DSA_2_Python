#Recursion: Calculating the sum of even and odd numbers in a range

def count_even_odd(start,end,total_even=0,total_odd=0):
    if start > end:
        return total_even, total_odd
    
    if start % 2 == 0:
        total_even += start
    else:
        total_odd += start
    
    return count_even_odd(start + 1, end, total_even, total_odd)

def main():
    start=int(input("Starting value: "))
    end=int(input("End value: "))
    
    even_sum, odd_sum = count_even_odd(start, end)
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
    
main()    
