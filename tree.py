
from abc import abstractmethod
from typing import Type

class Node():
    def __init__(self, name, *args):
        if len(args) == 0: # 0 children, i.e. should have been a leaf
            raise TypeError

        self.parent = None
        self.children = []
        self.name = name

        for child in args:
            self.children.append(child)
            child.parent = self

    def accept(self, visitor):
        visitor.visit(self)

    def depth(self):
        depth = 0
        n = self
        while n.parent != None:
            depth += 1
            n = n.parent
        return depth

    def isRoot(self):
        return self.parent == None


class Leaf(Node):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

class Visitor():
    @abstractmethod
    def visit(self, node: Node):
        raise NotImplementedError
        
    @abstractmethod
    def traverse(self, node: Node):
        raise NotImplementedError

if __name__ == "__main__":
    pass