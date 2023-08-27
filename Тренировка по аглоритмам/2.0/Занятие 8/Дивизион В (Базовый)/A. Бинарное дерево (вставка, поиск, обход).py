import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root is not None
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def print_tree(root, depth=0):
    if root is None:
        return
    print_tree(root.left, depth + 1)
    print("." * depth + str(root.value))
    print_tree(root.right, depth + 1)

root = None
query = sys.stdin.readline()[0:-1].split(" ")

while not (query[0] == ""):
    if query[0] == "ADD":
        value = int(query[1])
        if search(root, value):
            print("ALREADY")
        else:
            root = insert(root, value)
            print("DONE")
    elif query[0] == "SEARCH":
        value = int(query[1])
        if search(root, value):
            print("YES")
        else:
            print("NO")
    elif query[0] == "PRINTTREE":
        print_tree(root)
        
    query = sys.stdin.readline()[0:-1].split(" ")