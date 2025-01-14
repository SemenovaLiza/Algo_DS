class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def print_linked_list(vertex):
        while vertex:
                print(vertex.value, end=" -> ")
                vertex = vertex.next
        print("None") 


def get_element(head, index):
	while index:
		head = head.next
		index -= 1
	return head


def solution(head, index):
	pass

a1 = Node('1')
a2 = Node('2', a1)
a3 = Node('3', a2)
a4 = Node('4', a3)
a5 = Node('5', a4)
a6 = Node('6', a5)

print(solution(a6, 2))
