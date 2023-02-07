# Given a linked list and numbers m and n, return it back with only positions m to n in reverse
# Implementing a doubly linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def print(self):
        '''Prints the linked list'''
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert_back(self, data):
        '''Inserts elements at the end of the linked list'''
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode
        self.count += 1

    def insert_front(self, data):
        '''Inserts elements into the linked list from the front'''
        newNode = Node(data)
        if self.head:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            temp.prev = newNode
        else:
            self.head = newNode
        self.count += 1

    def insert_at(self, data, index):
        '''Inserts elements into the linked list at a specific index'''
        newNode = Node(data)
        current = self.head
        if self.count >= index:
            if index == 0:
                self.insert_front(data)
            elif index == self.count:
                self.insert_back(data)
            else:
                for i in range(0, index - 1):
                    current = current.next

                temp = current.next
                current.next = newNode
                newNode.prev = current
                newNode.next = temp
                temp.prev = newNode
                self.count += 1

        else:
            print(f'Index provided ({index}) is out of bounds ({self.count}). No values were added')

    def delete_value(self, data):
        '''Deletes a specific value in the linked list'''
        if self.count >= 1:
            current = self.head
            # If the list has one element and it matches.
            if self.count == 1 and current.value == data:
                self.head = None
                self.count -= 1
            # If the value is the first item in the list
            elif current.value == data:
                self.head = current.next
                current.next.prev = None
                self.count -= 1
            else:
                next = current.next
                while next:
                    if next.value == data:
                        if next.next:
                            current.next = next.next
                            next.next.prev = current
                        else:
                            current.next = None  # If deleting the last element in the list
                        self.count -= 1
                    current = next
                    next = next.next
        else:
            print('The list is empty. No values were deleted')

    def delete_index(self, index):
        '''Deletes the item at the given index'''
        if self.count >= 1:
            if index <= self.count:
                current = self.head
                if index == 0:
                    self.head = current.next
                    current.next.prev = None
                    self.count -= 1
                elif index == 1:
                    current.next = current.next.next
                    current.next.next.prev = current
                    self.count -= 1
                else:
                    for i in range(0, index - 2):
                        current = current.next

                    tgt = current.next
                    if tgt.next:
                        current.next = tgt.next
                        tgt.next.prev = current
                        self.count -= 1
                    else:
                        current.next = None
                        self.count -= 1
            else:
                print(f'Index provided is outside of the boundary of the list. It contains {self.count} elements')
        else:
            print('The list is empty. No values were deleted')

    def pop(self):
        if self.count >= 1:
            current = self.head
            while current.next:
                current = current.next

            val = current.value
            prev = current.prev
            prev.next = None
            self.count -= 1
            return val
        else:
            return 'The list is empty. There are no values to pop'

    def dequeue(self):
        if self.count >= 1:
            current = self.head
            val = current.value
            current = current.next
            self.head = current
            current.prev = None
            self.count -= 1
            return val
        else:
            return 'The list is empty. There are no values to dequeue'

    def find_index(self, value):
        if self.count >= 1:
            index = 0
            found = False
            current = self.head
            while current:
                if current.value == value:
                    found = True
                    break
                current = current.next
                index += 1
            if found:
                return index
            else:
                return -1
        else:
            return 'The list is empty'

    def m_n(self, m, n):
        if m == n:
            return
        elif self.count >= 1:
            m_index = n_index = 0
            m_found = n_found = False
            count = 0
            current = self.head
            while current:
                if current.value == m:
                    m_index = count
                    m_found = True
                if current.value == n:
                    n_index = count
                    n_found = True
                    break
                count += 1
                current = current.next
            if m_found and n_found:
                diff = n_index - m_index
                current.value = m

                for x in range(0, diff):
                    current = current.prev
                current.value = n
            else:
                print('m or n not found')

        else:
            print('The list is empty')


__name__ = "__main__"

# Testing values
list = LinkedList()
list.insert_back(3)
list.insert_back(5)
list.insert_front(8)
list.insert_back(7)
list.insert_at(9, 1)
list.insert_at(6, 2)
list.insert_at(10, 0)
list.print()
print()
list.m_n(6, 3)
list.print()
