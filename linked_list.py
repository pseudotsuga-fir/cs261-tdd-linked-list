# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Andrew Hepworth

class LinkedList:

    def __init__(self, value=None):
        print("Linked List Created")
        self.value = value
        self.next = self
        self.prev = self

    def is_sentinel(self):
        if self.value == None:
            return True
        return False

    def is_empty(self):
        if self.next != self or self.prev != self:
            return False
        return True
    
    def is_last(self):
        if self.next.is_sentinel():
            return True
        return False
    
    def last(self):
        if self.next.is_last():
            return self.next
        self.next.last()
    
    def append(self, item):
        print("I am appending and ")
        if self.is_empty():
            print("I went in empty")
            self.next = item
            self.prev = item
            item.next = self
            item.prev = self
            return
        if self.is_sentinel():
            print("I went in sentinel")
            self.next.append(item)
            return
        self.next = item
        item.prev = self

    pass
