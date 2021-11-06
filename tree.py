
from abc import abstractmethod
from typing import Type
import copy


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


from enum import Enum 

# class PrintTree(Visitor):
#     def __init__(self, node_style: NodeStyle):
#         if node_style == NodeStyle.INDENT:
#             self.visitorFunction = self.printWithIndent
#         elif node_style == NodeStyle.BULLET:
#             self.visitorFunction = self.printWithBullet

#     def printWithIndent(self, node: Node):
#         self.output_string += '  ' * node.depth() + node.name + '\n'
    
#     def printWithBullet(self, node: Node):
#         self.output_string += '  ' * node.depth() + '* ' + node.name + '\n'

#     def traverse(self, node: Node):
#         self.output_string = ""
#         self.traverseInternal(node)
#         return self.output_string[:-1]

#     def traverseInternal(self, node: Node):
#         node.accept(self)
#         if type(node) == Leaf:
#             return
#         for child in node.children:
#             self.traverseInternal(child)

#     def visit(self, node: Node):
#         self.visitorFunction(node)



if __name__ == "__main__":
    n = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))

    v = PrintTree(NodeStyle.INDENT)
    v = PrintTree(NodeStyle.BULLET)
    print(v.traverse(n))

    # pt = PrintTree()
    # pt.traverse(n)
