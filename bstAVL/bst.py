# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Overrides string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self.str_helper(self.root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self.str_helper(node.left, values)
        self.str_helper(node.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
        else:
            par = None
            cur = self.root

            while cur is not None:
                par = cur
                if value < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right

            if new_node.value < par.value:
                par.left = new_node
            else:
                par.right = new_node

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """

        par, cur, success = self.find_helper(value)

        if not success:
            return False
        if cur is self.root:
            par = BSTNode(None)
            par.right = cur

        if par.right is cur:
            if cur.left is None and cur.right is None:
                par.right = None
            elif cur.left is None and cur.right is not None:
                par.right = cur.right
                if cur is self.root:
                    self.root = cur.right
            elif cur.left is not None and cur.right is None:
                par.right = cur.left
                if cur is self.root:
                    self.root = cur.right
            else:
                par_successor = None
                successor = cur.right
                while successor.left is not None:
                    par_successor = successor
                    successor = successor.left

                successor.left = cur.left

                if successor is not cur.right:
                    par_successor.left = successor.right
                    successor.right = cur.right

                if cur is self.root:
                    self.root = successor
                par.right = successor

        if par.left is cur:
            if cur.left is None and cur.right is None:
                par.left = None
            elif cur.left is None and cur.right is not None:
                par.left = cur.right
            elif cur.left is not None and cur.right is None:
                par.left = cur.left
            else:
                par_successor = None
                successor = cur.right
                while successor.left is not None:
                    par_successor = successor
                    successor = successor.left

                successor.left = cur.left

                if successor is not cur.right:
                    par_successor.left = successor.right
                    successor.right = cur.right
                par.left = successor

        cur.left = None
        cur.right = None

    def contains(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        par, cur, success = self.find_helper(value)

        if success:
            return True
        else:
            return False

    def inorder_traversal(self) -> Queue:
        """
        TODO: Write your implementation
        """
        temp_qu = Queue()
        qu = self.inorder_helper(self.root, temp_qu)

        return qu

    def find_min(self) -> object:
        """
        TODO: Write your implementation
        """
        if self.root is None:
            return None
        else:
            cur = self.root
            while cur.left is not None:
                cur = cur.left
        return cur

    def find_max(self) -> object:
        """
        TODO: Write your implementation
        """
        if self.root is None:
            return None
        else:
            cur = self.root
            while cur.right is not None:
                cur = cur.right
        return cur

    def is_empty(self) -> bool:
        """
        TODO: Write your implementation
        """
        if self.root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        self.root = None

    def find_helper(self, value):
        """
        :return: child and parent of importance
        """
        par = None
        cur = self.root
        success = False

        while cur is not None:
            if cur.value == value:
                success = True
                break
            elif value < cur.value:
                par = cur
                cur = cur.left
            else:
                par = cur
                cur = cur.right

        return par, cur, success

    def inorder_helper(self, cur, qu):

        if cur is None:
            return qu

        if cur.left is not None:
            self.inorder_helper(cur.left, qu)

        qu.enqueue(cur.value)

        if cur.right is not None:
            self.inorder_helper(cur.right, qu)

        return qu


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        print('INPUT  :', tree, tree.root.value)
        tree.remove(tree.root.value)
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
