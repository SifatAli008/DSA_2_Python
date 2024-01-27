# Write a recursive program to print all subsets of a set of n elements.

def print_all_subsets(arr, n, subset=[]):
    if n == 0:
        print(subset)
        return

    print_all_subsets(arr, n - 1, subset)
    print_all_subsets(arr, n - 1, subset + [arr[n - 1]])

def main():
    elements = [1, 2, 3]
    print_all_subsets(elements, len(elements))

main()
