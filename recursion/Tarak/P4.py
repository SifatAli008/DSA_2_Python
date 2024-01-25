#Print Revers Order
def printRevers(n):
    if n==0:
        return 0
    else:
      print(n,end=' ')
      printRevers(n-1)
      
 
def main():
    num=int(input('Enter value : '))
    printRevers(num)
    
main()          
