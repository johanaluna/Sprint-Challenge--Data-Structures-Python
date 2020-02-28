from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: 
            #add item in the tail we are the newest
            self.storage.add_to_tail(item)
            # if the buffer is not full the pointer is in the tail
            self.current = self.storage.tail
        #If the buffer is full capacity
        else :
            #if the pointer is in tail go and find the oldest
            if self.current == self.storage.tail:
                self.current = self.storage.head
            #If the oldest in not in the head because is not the first time that over write a number...
            else:
                #Find the new oldest that is the next position 
                self.current = self.current.next
            # overwrite the value
            self.current.value = item


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        pivot = self.storage.head
        while pivot is not None:
            list_buffer_contents.append(pivot.value)
            pivot = pivot.next
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Initialize the current position to insert an element
        self.current = 0
        # Create array with the full capacity
        self.storage = [None]*capacity

    def append(self, item):
        # An array starts from zero position, this means that the last position 
        # Of my array is 4
        # If the my current position is not the full capacity then I can insert a new element
        if self.current < self.capacity:
            # Insert item at the current index in the storage
            self.storage[self.current] = item
            # Increment the current position
            self.current += 1
         
        self.lenght =+ 1
        # If the storage is full
        if self.current == self.capacity:
            # Go to the position zero and re write the element
            self.current = 0

    def get(self):
        storage_items = []
        # Add items in the storage if item is not None
        [storage_items.append(item) for item in self.storage if item is not None]
        return storage_items