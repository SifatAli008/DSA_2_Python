#NTH sum

def sum_of_values(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_values(n - 1)

def main():
    num = int(input('Number of values to sum: '))
    result = sum_of_values(num)
    print('Sum of values:', result)

main()
