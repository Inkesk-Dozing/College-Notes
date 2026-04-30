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

def search(root, key):
    if root is None:
        return False
    if key == root.key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

if __name__ == "__main__":
    keys_to_insert = [50, 30, 70, 20, 40, 60, 80]
    keys_to_search = [40, 25, 70, 90]

    root = None
    for k in keys_to_insert:
        root = insert(root, k)

    print("Inorder:", inorder(root))

    for k in keys_to_search:
        print(f"{k}:", "Found" if search(root, k) else "Not Found")