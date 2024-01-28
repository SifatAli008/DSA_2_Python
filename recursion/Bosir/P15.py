#Write a python program to implement a recursive function to check if a given binary tree is a binary search tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

def main():
    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    linked_list.add(40)
    
    # Printing the list
    linked_list.print_list()

main()
