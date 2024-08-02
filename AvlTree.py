class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node:
            return node.height
        return 0

    def get_size(self, node):
        if node:
            return node.size
        return 0

    def balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, trev):
        trev2 = trev.right
        temp = trev2.left
        trev2.left = trev
        trev.right = temp

        trev.height = 1 + max(self.get_height(trev.left), self.get_height(trev.right))
        trev2.height = 1 + max(self.get_height(trev2.left), self.get_height(trev2.right))

        trev.size = 1 + self.get_size(trev.left) + self.get_size(trev.right)
        trev2.size = 1 + self.get_size(trev2.left) + self.get_size(trev2.right)

        return trev2

    def right_rotate(self, trev):
        trev2 = trev.left
        temp = trev2.right
        trev2.right = trev
        trev.left = temp

        trev.height = 1 + max(self.get_height(trev.left), self.get_height(trev.right))
        trev2.height = 1 + max(self.get_height(trev2.left), self.get_height(trev2.right))

        trev.size = 1 + self.get_size(trev.left) + self.get_size(trev.right)
        trev2.size = 1 + self.get_size(trev2.left) + self.get_size(trev2.right)

        return trev2

    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        node.size = 1 + self.get_size(node.left) + self.get_size(node.right)

        b = self.balance(node)
        if b > 1 and key < node.left.key:
            return self.right_rotate(node)
        if b < -1 and key > node.right.key:
            return self.left_rotate(node)
        if b > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if b < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def find(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self.find(node.left, key)
        return self.find(node.right, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        node.size = 1 + self.get_size(node.left) + self.get_size(node.right)

        b = self.balance(node)
        if b > 1 and self.balance(node.left) >= 0:
            return self.right_rotate(node)
        if b > 1 and self.balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if b < -1 and self.balance(node.right) <= 0:
            return self.left_rotate(node)
        if b < -1 and self.balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def order_of_key(self, node, key):
        if not node:
            return 0
        if key < node.key:
            return self.order_of_key(node.left, key)
        elif key > node.key:
            return 1 + self.get_size(node.left) + self.order_of_key(node.right, key)
        else:
            return self.get_size(node.left)

    def get_by_order(self, node, k):
        if not node:
            return -1
        left_size = self.get_size(node.left)
        if k < left_size:
            return self.get_by_order(node.left, k)
        elif k > left_size:
            return self.get_by_order(node.right, k - left_size - 1)
        else:
            return node.key

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete_node(self.root, key)

    def find_key(self, key):
        return self.find(self.root, key)

    def order_of_key(self, key):
        return self.order_of_key(self.root, key)

    def get_by_order(self, k):
        return self.get_by_order(self.root, k - 1)


