class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.bucket_array = [None] * size

    def hash(self, key):
        return key % self.size

    def find(self, key):
        bucket_index = self.hash(key)
        current_node = self.bucket_array[bucket_index]
        while current_node:
            if current_node.key == key:
                return True
            current_node = current_node.next
        return False

    def insert(self, key, value):
        bucket_index = self.hash(key)
        current_node = self.bucket_array[bucket_index]
        previous_node = None

        while current_node:
            if current_node.key == key:
                current_node.value = value
                return
            previous_node = current_node
            current_node = current_node.next

        new_node = Node(key, value)
        if previous_node is None:
            self.bucket_array[bucket_index] = new_node
        else:
            previous_node.next = new_node

    def remove(self, key):
        bucket_index = self.hash(key)
        current_node = self.bucket_array[bucket_index]
        previous_node = None

        while current_node and current_node.key != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        if previous_node is None:
            self.bucket_array[bucket_index] = current_node.next
        else:
            previous_node.next = current_node.next
