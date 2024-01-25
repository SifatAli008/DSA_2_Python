#Print nth 
def printRevers(n):
    if n==0:
        return 
    else:
      printRevers(n-1)
      print(n,end=' ')
      
 
def main():
    num=int(input('Enter value : '))
    printRevers(num)
    
main()          
