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
        pass

    def append(self, item):
        pass

    def get(self):
        pass
