# Import DynamicArray from Assignment 2
from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self.heap[i] for i in range(self.heap.length())]
        return 'HEAP ' + str(heap_data)

    def is_empty(self) -> bool:
        """
        TODO: If the array is empty.
        """
        if self.heap.is_empty():
            return True
        else:
            return False

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        self.heap.append(node)
        child_index = self.heap.length()-1
        parent_index = (child_index-1) // 2

        while parent_index >= 0:

            if self.heap[parent_index] > node:
                self.heap.set_at_index(child_index, self.heap.get_at_index(parent_index))
                self.heap.set_at_index(parent_index, node)

                child_index = parent_index
                parent_index = (child_index - 1) // 2

            else:
                break

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        min = self.heap.get_at_index(0)
        self.heap.set_at_index(0,self.heap.get_at_index(self.heap.length()-1))
        self.heap.remove_at_index(self.heap.length()-1)

        if self.heap.length() > 1:
            c1_index = 1
            c2_index = 2
            p_index = 0
            parent = self.heap.get_at_index(0)
        else:
            return min

        while c1_index <= self.heap.length()-1:

            if c2_index <= self.heap.length()-1:
                if self.heap.get_at_index(c1_index) < self.heap.get_at_index(c2_index):
                    percolate_index = c1_index
                else:
                    percolate_index = c2_index
            else:
                percolate_index = c1_index

            if parent > self.heap.get_at_index(percolate_index):
                self.heap.set_at_index(p_index,self.heap.get_at_index(percolate_index))
                self.heap.set_at_index(percolate_index,parent)

                p_index = percolate_index
                c1_index = 2*p_index + 1
                c2_index = 2*p_index + 2

            else:
                break

        return min

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: start with first leaf heap, percolate down and repeat with nodes above
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))

        p_index = (self.heap.length()-2)//2
        c1_index = p_index*2 + 1
        c2_index = p_index*2 + 2

        og_index = p_index
        while og_index >= 0:
            if c2_index > self.heap.length()-1:
                perco_index = c1_index
            else:
                if self.heap.get_at_index(c1_index) < self.heap.get_at_index(c2_index):
                    perco_index = c1_index
                else:
                    perco_index = c2_index

            if self.heap.get_at_index(p_index) > self.heap.get_at_index(perco_index):
                perco = self.heap.get_at_index(p_index)
                self.heap.set_at_index(p_index, self.heap.get_at_index(perco_index))
                self.heap.set_at_index(perco_index, perco)


            p_index = perco_index
            c1_index = p_index*2 + 1
            c2_index = p_index*2 + 2

            if c1_index > self.heap.length()-1:
                og_index -= 1
                p_index = og_index
                c1_index = p_index * 2 + 1
                c2_index = p_index * 2 + 2
                continue
            elif c2_index > self.heap.length()-1:
                if self.heap.get_at_index(p_index) > self.heap.get_at_index(c1_index):
                    continue
                else:
                    og_index -= 1
                    p_index = og_index
                    c1_index = p_index * 2 + 1
                    c2_index = p_index * 2 + 2
            else:
                if self.heap.get_at_index(c1_index) > self.heap.get_at_index(c2_index):
                    new_index = c2_index
                else:
                    new_index = c1_index

                if self.heap.get_at_index(p_index) > self.heap.get_at_index(new_index):
                    continue
                else:
                    og_index -= 1
                    p_index = og_index
                    c1_index = p_index * 2 + 1
                    c2_index = p_index * 2 + 2



    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return self.heap.length()

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        self.heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    # start with building the heap
    p_index = (da.length() - 2) // 2
    c1_index = p_index * 2 + 1
    c2_index = p_index * 2 + 2

    og_index = p_index
    while og_index >= 0:
        if c2_index > da.length() - 1:
            perco_index = c1_index
        else:
            if da.get_at_index(c1_index) < da.get_at_index(c2_index):
                perco_index = c1_index
            else:
                perco_index = c2_index

        if da.get_at_index(p_index) > da.get_at_index(perco_index):
            perco = da.get_at_index(p_index)
            da.set_at_index(p_index, da.get_at_index(perco_index))
            da.set_at_index(perco_index, perco)

        p_index = perco_index
        c1_index = p_index * 2 + 1
        c2_index = p_index * 2 + 2

        if c1_index > da.length() - 1:
            og_index -= 1
            p_index = og_index
            c1_index = p_index * 2 + 1
            c2_index = p_index * 2 + 2
            continue
        elif c2_index > da.length() - 1:
            if da.get_at_index(p_index) > da.get_at_index(c1_index):
                continue
            else:
                og_index -= 1
                p_index = og_index
                c1_index = p_index * 2 + 1
                c2_index = p_index * 2 + 2
        else:
            if da.get_at_index(c1_index) > da.get_at_index(c2_index):
                new_index = c2_index
            else:
                new_index = c1_index

            if da.get_at_index(p_index) > da.get_at_index(new_index):
                continue
            else:
                og_index -= 1
                p_index = og_index
                c1_index = p_index * 2 + 1
                c2_index = p_index * 2 + 2

    k = da.length()-1
    par_ind = 0

    while k >= 0:
        parent = da.get_at_index(par_ind)
        da.set_at_index(par_ind, da.get_at_index(k))
        da.set_at_index(k,parent)
        temp_par = 0
        c1_ind = 1
        c2_ind = 2
        k -= 1

        while c1_ind <= k:
            parent = da.get_at_index(temp_par)
            if c2_ind <= k:
                if da.get_at_index(c1_ind) < da.get_at_index(c2_ind):
                    percolate_index = c1_ind
                else:
                    percolate_index = c2_ind
            else:
                percolate_index = c1_ind

            if parent > da.get_at_index(percolate_index):
                da.set_at_index(temp_par, da.get_at_index(percolate_index))
                da.set_at_index(percolate_index, parent)

                temp_par = percolate_index
                c1_ind = 2 * temp_par + 1
                c2_ind = 2 * temp_par + 2

            else:
                break






# BASIC TESTING
if __name__ == '__main__':
    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap()
    h.heap = DynamicArray([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100,20,6,200,90,150,300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da[0] = 500
    print(da)
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
