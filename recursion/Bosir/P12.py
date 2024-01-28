#Write a C++ program to implement a recursive function to generate all permutations of a given string.

def generate_permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):

            fixed_char = s[i] 

            for perm in generate_permutations(s[:i] + s[i+1:]):
                perms.append(fixed_char + perm)
                
        return perms

def main():
    input_string = "abc"
    print("Permutations of", input_string, "are:")
    permutations = generate_permutations(input_string)
    for perm in permutations:
        print(perm)

main()