import sys
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # MAking sure the size of the storage is less than the capacity
        if len(self.storage) < self.capacity:
            # Add to the tail in order to prevent checking for head == None
            # then set the current_node variable to the head
            self.storage.add_to_tail(item)
            self.current_node = self.storage.head
        else:  # capacity is full, need to make room
            if not self.current_node.next:
                self.current_node.value = item
                self.current_node = self.storage.head
            else:
                self.current_node.value = item
                self.current_node = self.current_node.next

    def get(self):
        buffer = []
        current = self.storage.head
        while current:  # while there is still a current value
            # we append the value to the array
            buffer.append(current.value)
            current = current.next

        return buffer
