#Write a recursive program to count the prime numbers of an array of n integers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_array(arr, n):
    if n == 0:
        return 1 if is_prime(arr[0]) else 0
    else:
        return (1 if is_prime(arr[n]) else 0) + count_primes_in_array(arr, n - 1)

def main():
    arr = [2, 3, 5, 6, 9, 11, 13, 17]
    count = count_primes_in_array(arr, len(arr) - 1)
    print(f'The number of prime numbers in the array is: {count}')

main()
