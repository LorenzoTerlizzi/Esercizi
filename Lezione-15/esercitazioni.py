def longest_palindrome(s: str) -> int:
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        
    lenght_palindrome = 0
    odd_count = False

    for count in dict.values():
        if count % 2 == 0:
            lenght_palindrome += count
        else:
            lenght_palindrome += count - 1
            odd_count = True
        
    if odd_count:
        lenght_palindrome += 1
        
    return lenght_palindrome

#########
# 2
#########
class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def append(self, val: int):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)
    def get_node(self, val):
        if val == 0:
            return self.head
        else:
            current = self.head
            while current.next:
                current = current.next
        
def is_palindrome(head: Node) -> list[int]:
    
    slow = head
    stack = []
    ispalind = True

    while slow != None:
        stack.append(slow.val)
        slow = slow.next
 
    while head != None:
 
        i = stack.pop()
        if head.val == i:
            ispalind = True
        else:
            ispalind = False
            break
        head = head.next
    return ispalind