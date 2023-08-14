# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:

from SLNode import SLNode


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        The steps are to make the new node point to what the head sentinel points to, then point the head sentinel
        to new node.
        """
        new_node = SLNode(value)

        new_node.next = self.head.next

        self.head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        new_node = SLNode(value)
        cur = self.head

        while cur.next != self.tail:
            cur = cur.next

        new_node.next = cur.next

        cur.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length():
            raise SLLException
        else:
            new_node = SLNode(value)
            cur = self.head
            for i in range(index):
                cur = cur.next

            new_node.next = cur.next
            cur.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length() - 1:
            raise SLLException
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next

            cur.next = cur.next.next

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        cur = self.head
        while cur.next != self.tail:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            else:
                cur = cur.next

        return False

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        cur = self.head
        count = 0
        while cur.next != self.tail:
            cur = cur.next
            if cur.value == value:
                count += 1

        return count

    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        cur = self.head

        while cur.next != self.tail:
            cur = cur.next
            if cur.value == value:
                return True

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        if start_index < 0 or start_index + size - 1 > self.length() - 1 or size < 0:
            raise SLLException
        else:
            new_LL = LinkedList()
            cur = self.head
            for i in range(start_index + 1):
                cur = cur.next

            for i in range(size):
                new_LL.insert_back(cur.value)
                cur = cur.next

        return new_LL


if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
