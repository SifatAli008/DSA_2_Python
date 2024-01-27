#Write a recursive program to solve the Tower of Hanoi problem for n disks.


def hanoi(n, i, j, k):
    if n == 1:
        print(f"{i}->{j}")
    else:
        hanoi(n-1, i, k, j)
        print(f"{i}->{j}")
        hanoi(n-1, j, i, k)

def main():
 n=int(input('Enter the number of Disk to solve the Tower of Hanoi : '))
 hanoi(n, 1, 2, 3)

main() 
