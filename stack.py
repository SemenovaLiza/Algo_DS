# push -> add to the stack
# pop -> take element from stack
# size -> stack size
# peek -> show last element
# isEmpty -> check if stack is empty 
from linked_list import Node


class Stack:
    """"Stack using Linked List for massive dataset."""
    def __init__(self):
        self.head = None


    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        element = self.head
        self.head = self.head.next
        return element.value


    def peek(self):
        return self.head.value


    def size(self):
        count = 0
        current_element = self.head
        while current_element:
            count += 1
            current_element = current_element.next
        return count


    def isEmpty(self):
        return self.head is None
    
    def __repr__(self):
        stack = []
        current_element = self.head
        while current_element:
            stack.append(repr(current_element.value))
            current_element = current_element.next
        return "<-".join(stack[::-1])


if __name__=="__main__":
    a = Stack()
    for i in range(5):
        a.push(i+1)
    print(a)
    print(a.pop())
    print(a)
    print(a.peek())
    print(a)
    a.push(7)
    print(a)
    print(a.size())