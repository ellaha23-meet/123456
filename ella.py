class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)

        return self._search(root.right, key)

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, root, elements):
        if root:
            self._inorder_traversal(root.left, elements)
            elements.append(root.val)
            self._inorder_traversal(root.right, elements)

    def preorder_traversal(self):
        elements = []
        self._preorder_traversal(self.root, elements)
        return elements

    def _preorder_traversal(self, root, elements):
        if root:
            elements.append(root.val)
            self._preorder_traversal(root.left, elements)
            self._preorder_traversal(root.right, elements)

    def postorder_traversal(self):
        elements = []
        self._postorder_traversal(self.root, elements)
        return elements

    def _postorder_traversal(self, root, elements):
        if root:
            self._postorder_traversal(root.left, elements)
            self._postorder_traversal(root.right, elements)
            elements.append(root.val)

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(30)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Preorder Traversal:", tree.preorder_traversal())
    print("Postorder Traversal:", tree.postorder_traversal())

    search_key = 15
    result = tree.search(search_key)
    if result:
        print(f"Element {search_key} found in the tree.")
    else:
        print(f"Element {search_key} not found in the tree.")
