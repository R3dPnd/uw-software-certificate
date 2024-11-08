class LinkedList:
    class ListNode:
        def __init__(self, data=None):
            self.next = None
            self.prev = None
            self.data = data

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        self.char_count = 0

    def append(self, data):
        n = LinkedList.ListNode(data)

        if self.first is None:         # Special case for empty lists
            self.first = n
            self.last = n
        else:  # Add the node to the end.
            n.prev = self.last    # the old .last becomes the new nodes previous
            self.last.next = n    # the old .last needs it's next to point to the new node
            self.last = n         # point the .last node to be the new node.

        self.char_count += len(data)
        self.count += 1

    def size(self):
        return self.count

    def iter(self):
        curr = self.first
        while curr:
            ret = curr.data
            curr = curr.next
            yield ret

    def delete(self, data):
        curr = self.first
        deleted_fl = False

        if curr is None:  # LIST IS EMPTY, TRIVIAL CASE
            deleted_fl = False
        elif curr.data == data:  # REMOVE FROM FRONT
            if self.first == self.last:  # IF REMOVING THE FIRST AND ONLY NODE
                self.last = None
            self.first = curr.next
            deleted_fl = True
        elif self.last.data == data:  #REMOVE FROM END
            self.last = self.last.prev
            self.last.next = None
            deleted_fl = True
        else:  # SEARCH THE REST TO SEE IF IT MATCHES
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    deleted_fl = True
                    break
                curr = curr.next

        if deleted_fl:
            self.count -= 1
            self.char_count -= len(data)

    def contains(self, data):
        for n in self.iter():
            if data == n:
                return True
        return False

    def search(self, data):
        curr = self.first
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def clear(self):
        self.first = None
        self.last = None
        self.char_count = 0

#########################################################
####### IMPLEMENT THE FOLLOWING 2 FUNCTIONS  ############
#########################################################
    def charCount(self, aggregated=False):
         if self.first is None:
             return None
         if aggregated:
             return self.char_count
         else:
             curr = self.first
             count = []
             while curr:
                 count.append(len(curr.data))
                 curr = curr.next
             return count

    def reverse(self, in_place=False):
        if self is None or self.first is None:
            return None
        if in_place:
            ## REVERSE IN PLACE
            first = self.first
            last = self.last
            for i in range(self.count//2):
                temp = first.data
                first.data = last.data 
                last.data = temp
                first = first.next
                last = last.prev
        else:
            curr = self.last
            reversed_list = LinkedList()
            while curr:
                reversed_list.append(curr.data)
                curr = curr.prev
            self.first, self.last = reversed_list.first, reversed_list.last

class Deque:
## STUDENT TO RENAME TO class Deque ##
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        n = Deque.QueueNode(data)
        if self.first is None:  # EMPTY
            self.first = n
            self.last = n
        else:
            self.last.prev = n
            n.next = self.last
            self.last = n
        self.size += 1

    def dequeue(self):
        ret = self.first

        if self.size == 1:
            self.first = None
            self.last = None
        elif self.size > 1:
            self.first = self.first.prev
            self.first.next = None

        if self.size >= 1:
            self.size -= 1
            return ret.data

#########################################################
####### IMPLEMENT THE FOLLOWING 4 FUNCTIONS  ############
#########################################################
    def addFirst(self, data):
        """ Creates a new node at the beginning of the queue, containing the value of data.

        :param data: The data to be contained in the newly created element.
        :return: None
        """
        node = Deque.QueueNode(data)
        if self.first is None:
            self.first = node
            self.last = self.first
        if self.size == 1:
            self.first.prev = node
            self.last = node
        node.next = self.first
        self.first = node
        self.size += 1

    def addLast(self, data):
        """ Creates a new node at the beginning of the queue, containing the value of data.

        :param data: The data to be contained in the newly created element.
        :return: None
        """
        node = Deque.QueueNode(data)
        # check if the first node is empty
        if self.first is None:
            self.first = node
            self.last = self.first
        # check if the first node is the only node
        if self.size == 1:
            self.first.next = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def removeFirst(self):
        """ Returns the data of the node that is at the "start" of the Deque.
        :return: The data stored in the node that is at the "start" of the Deque.
        """
        # check if the first node is empty
        if self.first is None:
            return None
        # check if the first node is the only node
        if self.size == 1:
            # get the data from the first node
            data = self.first.data
            # remove the first node
            self.first = None
            self.last = None
            # decrement the size of the deque
            self.size = 0
            # return the data
            return data
        # get the data from the first node
        data = self.first.data
        # remove the first node
        self.first = self.first.next
        # decrement the size of the deque
        self.size -= 1
        # return the data
        return data

    def removeLast(self):
        """ Returns the data of the node that is at the "end" of the Deque.
        :return: The data stored in the node that is at the "end" of the Deque.
        """
        if self.first is None:
            return None
        if self.size == 1:
            data = self.first.data
            self.first = None
            self.last = None
            self.size = 0
            return data
        data = self.last.data
        self.last = self.last.prev
        self.size -= 1
        return data
