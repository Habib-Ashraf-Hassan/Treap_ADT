import random

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        priority = random.randint(1, 100)
        self.root = self._insert(self.root, key, priority)

    def _insert(self, node, key, priority):
        if node is None:
            return TreapNode(key, priority)
        
        if key < node.key:
            node.left = self._insert(node.left, key, priority)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, priority)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        
        return node

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)
        
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.key)

    def is_empty(self):
        return self.root is None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def merge(self, other_treap):
        new_treap = Treap()
        new_treap.root = self._merge(self.root, other_treap.root)
        return new_treap

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def split(self, nleftsize):
        left_treap = Treap()
        right_treap = Treap()
        left_treap.root, right_treap.root = self._split(self.root, nleftsize)
        return left_treap, right_treap

    def _split(self, node, nleftsize):
        if node is None:
            return None, None

        if self._size(node.left) >= nleftsize:
            left, right = self._split(node.left, nleftsize)
            node.left = right
            return left, node
        else:
            left, right = self._split(node.right, nleftsize - self._size(node.left) - 1)
            node.right = left
            return node, right

# Example usage:
treap = Treap()
treap.insert(5)
treap.insert(3)
treap.insert(8)
treap.insert(12)
treap.insert(11)
# Search example
found = treap.search(5)  # Returns True
not_found = treap.search(7)  # Returns False
print(found)
print(not_found)
print(treap.inorder_traversal())
print(treap.postorder_traversal())
print(treap.preorder_traversal())

# Delete example
treap.delete(5)  # Deletes the node with key 5

print(treap.inorder_traversal())  # show treap after deletion

treap.insert(9)  # add another so that we split into 3 by 2
# Perform a split at nleftsize = 3
nleftsize = 3
left_treap, right_treap = treap.split(nleftsize)

# Display the keys in the left and right treaps with left treap having three nodes
print("Keys in the left treap after split:", left_treap.inorder_traversal())
print("Keys in the right treap after split:", right_treap.inorder_traversal())
