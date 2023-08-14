# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Overrides string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super().str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: contains for duplicates
        """
        # Insert value similar to bst tree add method
        new_node = AVLNode(value)

        if self.root is None:
            self.root = new_node
        else:
            par = None
            cur = self.root

            while cur is not None:
                par = cur
                if value < cur.value:
                    cur = cur.left
                elif value > cur.value:
                    cur = cur.right
                else:
                    # no duplicates
                    return

            if new_node.value < par.value:
                par.left = new_node
                par.left.parent = par
            else:
                par.right = new_node
                par.right.parent = par

            while par is not None:
                new_par = self.rebalance(par)

                if new_par:
                    par = par.parent.parent
                else:
                    par = par.parent

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        root = False
        par, cur, success, parent_right = self.find_helper(value)
        parent = par
        if par is None:
            root = True

        if not success:
            return False
        else:
            if cur.left is None and cur.right is None:
                if root:
                    self.root = None
                else:
                    if parent_right:
                        par.right = None
                    else:
                        par.left = None

            elif cur.left is None and cur.right is not None:
                if root:
                    self.root = cur.right
                    cur.right.parent = None
                else:
                    cur.right.parent = par
                    if parent_right:
                        par.right = cur.right
                    else:
                        par.left = cur.right
            elif cur.left is not None and cur.right is None:
                if root:
                    self.root = cur.left
                    cur.left.parent = None
                else:
                    cur.left.parent = par
                    if parent_right:
                        par.right = cur.left
                    else:
                        par.left = cur.left
            else:

                successor = cur.right

                while successor.left is not None:
                    successor = successor.left

                successor.left = cur.left
                cur.left.parent = successor
                parent = successor.parent

                if successor is not cur.right:
                    successor.parent.left = successor.right
                    if successor.right is not None:
                        successor.right.parent = successor.parent
                    successor.right = cur.right
                    cur.right.parent = successor
                else:
                    parent = successor

                successor.parent = cur.parent
                if root:
                    self.root = successor
                else:
                    if parent_right:
                        par.right = successor
                    else:
                        par.left = successor

            cur.right = None
            cur.left = None

            while parent is not None:
                new_par = self.rebalance(parent)

                if new_par:
                    parent = parent.parent.parent
                else:
                    parent = parent.parent

    # ------------------------------------------------------------------ #

    ################################################################
    # It's highly recommended, though not required,
    # to implement these methods for balancing the AVL Tree.
    ################################################################

    def balance_factor(self, node):
        """"""
        if node.right is None:
            right_subt = 0
        else:
            right_subt = node.right.height + 1

        if node.left is None:
            left_subt = 0
        else:
            left_subt = node.left.height + 1

        bf = right_subt - left_subt

        return bf

    def update_height(self, node):
        """"""
        # set max height to -1 not zero since we add one
        max_height = -1
        if node.left is not None and node.right is not None:
            if node.left.height > node.right.height:
                max_height = node.left.height
            else:
                max_height = node.right.height

        if node.left is None and node.right is not None:
            max_height = node.right.height
        elif node.left is not None and node.right is None:
            max_height = node.left.height

        node.height = max_height + 1

    def rotate_left(self, node):
        """ maybe update height after rotation here"""
        child = node.right
        node.right = child.left

        if child.left is not None:
            child.left.parent = node

        child.left = node

        if node is self.root:
            self.root = child

        child.parent = node.parent
        node.parent = child

        self.update_height(node)
        self.update_height(child)

        return child

    def rotate_right(self, node):
        """"""
        child = node.left
        node.left = child.right

        if child.right is not None:
            child.right.parent = node

        child.right = node

        if node is self.root:
            self.root = child

        child.parent = node.parent
        node.parent = child

        self.update_height(node)
        self.update_height(child)

        return child

    def rebalance(self, node):
        """"""
        # see whether current node is left or right of its parent
        rot_flag = True
        npar = node.parent
        lflag = False
        if node.parent is not None:
            if node.parent.left is node:
                lflag = True

        if self.balance_factor(node) < -1:
            if self.balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
                node.left.parent = node

            newSR = self.rotate_right(node)

            if npar is not None:
                if lflag:
                    npar.left = newSR
                else:
                    npar.right = newSR

        elif self.balance_factor(node) > 1:
            if self.balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
                node.right.parent = node

            newSR = self.rotate_left(node)

            if npar is not None:
                if lflag:
                    npar.left = newSR
                else:
                    npar.right = newSR

        else:
            self.update_height(node)
            rot_flag = False

        return rot_flag

    def find_helper(self, value):
        """
        :return: child and parent of importance
        """
        par = None
        cur = self.root
        success = False
        parent_right = True
        while cur is not None:
            if cur.value == value:
                success = True
                break
            elif value < cur.value:
                par = cur
                cur = cur.left
                parent_right = False
            else:
                par = cur
                cur = cur.right
                parent_right = True

        return par, cur, success, parent_right

    # ------------------------------------------------------------------ #

    ################################################################
    # Use the methods as a starting point if you'd like to override.
    # Otherwise, the AVL can simply call any BST method.
    ################################################################

    def contains(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        cur = self.root
        success = False

        while cur is not None:
            if cur.value == value:
                success = True
                break
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        return success

    '''
    def inorder_traversal(self) -> Queue:
        """
        TODO: Write your implementation
        """
        return super().inorder_traversal()

    def find_min(self) -> object:
        """
        TODO: Write your implementation
        """
        return super().find_min()

    def find_max(self) -> object:
        """
        TODO: Write your implementation
        """
        return super().find_max()

    def is_empty(self) -> bool:
        """
        TODO: Write your implementation
        """
        return super().is_empty()

    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        super().make_empty()
    '''


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),  # RR, RR
        (10, 20, 30, 50, 40),  # RR, RL
        (30, 20, 10, 5, 1),  # LL, LL
        (30, 20, 10, 1, 5),  # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', tree, tree.root.value)
        tree.remove(tree.root.value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
