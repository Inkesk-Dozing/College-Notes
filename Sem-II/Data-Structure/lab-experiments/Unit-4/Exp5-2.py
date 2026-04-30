class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    return root

def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

if __name__ == "__main__":
    keys = [50, 30, 70, 20, 40, 60, 80]
    delete_keys = [20, 30, 50]

    root = None
    for k in keys:
        root = insert(root, k)

    print("Initial:", inorder(root))

    for k in delete_keys:
        root = delete(root, k)
        print(f"After deleting {k}:", inorder(root))