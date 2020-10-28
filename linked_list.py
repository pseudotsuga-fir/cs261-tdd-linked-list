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
        if self.is_last():
            return self
        return self.next.last()
        
    
    def append(self, item):
        if self.is_empty():
            self.next = item
            self.prev = item
            item.next = self
            item.prev = self
        else:
            self.prev.next = item
            item.prev = self.prev
            item.next = self
            self.prev = item
        # if self.is_last():
        #     temp = self.next
        #     self.next = item
        #     item.next = temp
        #     item.prev = self
        #     item.next.prev = item
        #     return
        # self.next.append(item)

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def insert(self, item):
        item.next = self.next
        item.prev = self
        self.next.prev = item
        self.next = item

    def insert_in_order(self, item):
        if self.is_empty():
            self.append(item)
            return
        if self.next.value != None and item.value > self.next.value:
            self.next.insert_in_order(item)
            return
        self.insert(item)
        
    def at(self, i, place=0):
        if place == i:
            return self
        return self.next.at(i, place + 1)
    
    def search(self, item):
        if self.value == item:
            return self
        if self.is_last():
            return None
        return self.next.search(item)


    pass
