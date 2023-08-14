# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        for i in range(self.da.length()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0
        for i in range(self.da.length()):
            if self.da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        TODO: Write this implementation
        """
        dict1 = {}
        dict2 = {}
        for i in range(self.da.length()):
            if self.da.get_at_index(i) not in dict1:
                dict1[self.da.get_at_index(i)] = 1
            else:
                dict1[self.da.get_at_index(i)] += 1

        for i in range(second_bag.da.length()):
            if second_bag.da.get_at_index(i) not in dict2:
                dict2[second_bag.da.get_at_index(i)] = 1
            else:
                dict2[second_bag.da.get_at_index(i)] += 1

        if dict1 == dict2:
            return True
        else:
            return False

    def __iter__(self):
        """
        TODO: Write this implementation
        """
        self.da.index = 0
        return self

    def __next__(self):
        """
        TODO: Write this implementation
        """
        try:
            value = self.da[self.da.index]
        except DynamicArrayException:
            raise StopIteration
        self.da.index = self.da.index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
