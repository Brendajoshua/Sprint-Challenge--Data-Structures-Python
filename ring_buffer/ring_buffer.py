from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if list is at capacity
        # if so
        if self.capacity == len(self.storage):
            # replace the current item with the new item
            self.current.value = item
            # move current to next item in list
            # if current ite is the tail
            if self.current == self.storage.tail:
                # next value is the head
                self.current = self.storage.head
            else:
                self.current = self.current.next
        # if not at capacity
        else:
            # add to end of storage
            self.storage.add_to_tail(item)
            # if the storage had no items
            if len(self.storage) == 1:
                # set current to new item
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            # add node value to list contents
            list_buffer_contents.append(node.value)
            # move pointer
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0
        self.storage = [None] * 5

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage[self.oldest] = item
            self.oldest = 0 if self.oldest == self.capacity - 1 else self.oldest + 1

    def get(self):
        return list(filter(None, self.storage))

# The advantages of using a Python list instead of a linked list are:
# - in instance, the code is much cleaner
# - accessing elements via indices is faster--const O(1) versus linear O(n) access time for linked lists

# The typical disadvantages of using a Python list instead of a linked list are:
# - fixed sizes rather than dynamic sizes
# - insertion and deletion are expensive

# The disadvantages normally found in arrays that are overcome with this arrangement are with runtime and space complexities. 
# Typically, the runtime complexity of inserting or deleting a value at the front or in the middle of a Python list is linear O(n), since following values need to be shifted back. 
# In this instance, however, since the inserted value replaces an existing value, no shifting of values due to insertion or deletion is needed. 
# Additionally, since we know the length of the list from the outset, no additional space needs to be created for new elements. Since we know from the outset the capacity of the Ring Buffer, we don't have to worry about dynamic sizing.