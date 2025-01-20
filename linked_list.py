#append -> +
#insert by index -> +
#replace by index -> +
#get element by index -> +
#length -> +
#remove -> +
#reversed_list -> 
# 3 task with linked lists

class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head


    def get_element(self, index):
        last_node = self.head
        while index:
            last_node = last_node.next
            index -= 1
        return last_node


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node # -> keeps the last element for efficiency


    def insert_by_index(self, index, value):
        if index == 0:
            new_node = Node(value, self.head)
            self.head = new_node
            return
        last_node = self.get_element(index-1)
        new_node = Node(value, last_node.next)
        last_node.next = new_node


    def replace_by_index(self, index, value):
        if index == 0:
            new_node = Node(value, self.head.next)
            self.head = new_node
            return
        last_node = self.get_element(index-1)
        new_node = Node(value, last_node.next.next)
        last_node.next = new_node


    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        last_node = self.get_element(index-1)
        last_node.next = last_node.next.next


    def length(self):
        current_node = self.head
        length = 1
        while current_node.next:
            length += 1
            current_node = current_node.next
        return length
    

    def reverse(self):
        nodes = []
        current_node = self.tail
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.previous
        return "->".join(nodes)

    
    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return "->".join(nodes)



a = LinkedList()
a.append('5')
a.append('1')
a.append('2')
a.append('3')
a.insert_by_index(2,'6')
a.insert_by_index(1,'6')
a.replace_by_index(0,'6')

#a.replace_by_index(2, '1.5')
#a.remove(2)
print(a.get_element(0)) #5
print(a.length()) #4

print(a.reverse()) #5->1->2->3
