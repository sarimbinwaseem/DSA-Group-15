# GitHub: https://github.com/sarimbinwaseem/DSA-Group-15
# Abdul Muteeb Shera (19B-121-SE)
# Sarim Bin Waseem (19B-072-SE)
import math
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Scapegoat:
    def __init__(self):
        self.root = None
        self.size = 0
        self.maxSize = 0

    def findScapegoat(self, node):
        if node == self.root:
            return None
        while self.isBalancedAtNode(node) == True:
            if node == self.root:
                return None
            node = node.parent
        print("ScapeGoat Found")
        return node

    def insert(self, key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return

        currentNode = self.root
        while currentNode != None:
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        node.parent = potentialParent
        if node.key < node.parent.key:
            node.parent.left = node
        else:
            node.parent.right = node
        node.left = None
        node.right = None
        self.size += 1
        scapegoat = self.findScapegoat(node)
        if scapegoat == None:
            return
        temporary = self.rebalance(scapegoat)

        scapegoat.left = temporary.left
        scapegoat.right = temporary.right
        scapegoat.key = temporary.key
        scapegoat.right.parent = scapegoat
        scapegoat.left.parent = scapegoat

    def isBalancedAtNode(self, node):
        if abs(self.sizeOfSubtree(node.left) - self.sizeOfSubtree(node.right)) <= 1:
            return True
        return False

    def sizeOfSubtree(self, node):
        if node == None:
            return 0
        return 1 + self.sizeOfSubtree(node.left) + self.sizeOfSubtree(node.right)

    def flatten(self, node, nodes):
        if node == None:
            return
        self.flatten(node.left, nodes)
        nodes.append(node)
        self.flatten(node.right, nodes)

    def rebalance(self, root):
        nodes = []
        self.flatten(root, nodes)
        return self.buildTreeFromSortedList(nodes, 0, len(nodes)-1)

    def buildTreeFromSortedList(self, nodes, start, end):
        if start > end:
            return None
        mid = int(math.ceil(start + (end - start) / 2.0))
        node = Node(nodes[mid].key)
        node.left = self.buildTreeFromSortedList(nodes, start, mid-1)
        node.right = self.buildTreeFromSortedList(nodes, mid+1, end)
        return node

t = Scapegoat()
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)