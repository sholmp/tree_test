
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

    def accept(self):
        pass


    def depth(self):
        depth = 0
        n = self
        while n.parent != None:
            depth += 1
            n = n.parent
        return depth


class Leaf(Node):
    parent = None
    def __init__(self, name):
        self.name = name

    


class Visitor():
    def traverse(self):
        pass

    def visit(self):
        pass




if __name__ == "__main__":
    n = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))
    # print(n.name)

    # print(len(n.children))
    for child in n.children:
        print(child.name)
