
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

# An input string is valid if: 

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.

def is_valid_parenthesis(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    list = []
    for i in s:
        if i in dict.keys():
                list.append(i)
        else:
            if list == []:
                return False
            a = list.pop()
            if i!= dict[a]:
                return False
    return True

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into 
# a single array sorted in non-decreasing order. 
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    for i in nums2:
        nums1.append(i)
        nums1.remove(0)
    a = len(nums1)
    for i in range(len(nums1)):
        for j in range(len(nums1) -1):
            if nums1[j] > nums1[j+1]:
                temp: int = nums1[j]
                nums1[j] = nums1[j+1]
                nums1[j+1] = temp
        return nums1

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the 
# functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:

# - push(x: int) -> None: Pushes element x to the top of the stack.
# - pop() -> None Removes the element on the top of the stack and returns it.
# - top() -> None Returns the element on the top of the stack.
# - empty() -> None Returns true if the stack is empty, false otherwise.

class Queue:
    pass

class MyStack: 
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue2:
           self.queue1.append(self.queue2.pop(0))
           self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self):
        return self.queue1.pop()
    def top(self):
        return self.queue1[1]
        
    def empty(self):
        return len(self.queue1) == 0
    
# Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts 
# using classes. 

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


# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked 
# list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is 
# not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
# Model the Node and Linked List concepts using classes.

class Node:
    pos = 0
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        self.pos = Node.pos
        Node.pos += 1
        
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
                if current.pos == val:
                    return current
def has_cycle(head: Node) -> list[int]:
    prev: Node = head
    current: Node = head.next
    
    if current is None:
        return False
    if current.pos <= prev.pos:
        return True
    
    while current.next is not None:
        prev = current
        current = current.next
        if current.pos <= prev.pos:
            return True
    return False


# Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the 
# longest palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not 
# considered a palindrome here.

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

# The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive integer k 
# given as inputs. A subset of nums is beautiful if it does not contain two integers with an absolute difference equal 
# to k. Return the number of non-empty beautiful subsets of the array nums. A subset of nums is an array that can be 
# obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen 
# indices to delete are different.

#def beautiful_subsets(nums: list[int], k: int):
