
from abc import abstractmethod
from typing import Type
import copy


class Node():
    children = []
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
    parent = None
    def __init__(self, name):
        self.name = name

class Visitor():
    @abstractmethod
    def visit(self, node: Node):
        raise NotImplementedError

    @abstractmethod
    def traverse(self, node: Node):
        node.accept(self)
        if type(node) == Leaf:
            return
        for child in node.children:
            self.traverse(child)

if __name__ == "__main__":
    pass