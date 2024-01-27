#Implement in-order, preorder and postorder traversal of a graph using recursion.

def preorder(bin_tree, size, myind):
    if myind >= size or bin_tree[myind] == -1  :
        return
    else:
        print(bin_tree[myind], end=" ")
        
        left_child = 2 * myind
        right_child = 2 * myind + 1
        
        preorder(bin_tree, size, left_child)
        preorder(bin_tree, size, right_child)

def inorder(bin_tree, size, myind):
    if myind >= size or bin_tree[myind] == -1 :
        return
    else:
        left_child = 2 * myind
        right_child = 2 * myind + 1
        
        inorder(bin_tree, size, left_child)
        print(bin_tree[myind], end=" ")
        inorder(bin_tree, size, right_child)

def postorder(bin_tree, size, myind):
    if myind >= size or bin_tree[myind] == -1 :
        return
    else:
        left_child = 2 * myind
        right_child = 2 * myind + 1
        
        postorder(bin_tree, size, left_child)
        postorder(bin_tree, size, right_child)
        print(bin_tree[myind], end=" ")

def main():
     bin_tree = [-1, 100, 300, 50, 120, 200, 30, -1, -1, 20, 80, 150, -1, 90]
     n = len(bin_tree)

     print("In Order:", end=" ")
     inorder(bin_tree, n, 1)
     print('\n')

     print("Pre Order:", end=" ")
     preorder(bin_tree, n, 1)
     print('\n')

     print("Post Order:", end=" ")
     postorder(bin_tree, n, 1)
     print('\n')
      
main() 