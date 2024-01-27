#Write a recursive program to count the odd/even numbers of an array of n integers
def count_odd_even(arr, n, odd_count=0, even_count=0, index=0):
  
    
    if index == n:
        return odd_count, even_count

    if arr[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    return count_odd_even(arr, n, odd_count, even_count, index + 1)

def main():
      array = [1, 2, 2 , 4 , 2, 6, 7, 8, 9, 10]
      array_size = len(array)

      odd_count, even_count = count_odd_even(array, array_size)

      print("Number of odd numbers:", odd_count)
      print("Number of even numbers:", even_count)
  
main()      
