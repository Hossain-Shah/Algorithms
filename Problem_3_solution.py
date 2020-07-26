class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, node1, node2):
    if root is None:
        return None
    if (root.data > node1 and root.data > node2):
        return lca(root.left, node1, node2)
    if (root.data < node1 and root.data < node2):
        return lca(root.right, node1, node2)
    return root
