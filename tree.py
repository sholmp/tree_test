
from typing import Type


class Node():
    children = []
    parent = None
    def __init__(self, name, *children):
        if len(children) == 0: # 0 children, i.e. should have been a leaf
            raise TypeError
        self.name = name
        for child in children:
            self.children.append(child)
            child.parent = self

    def accept(self):
        pass


class Leaf(Node):
    parent = None
    def __init__(self, name):
        self.name = name

    


class Visitor():
    def traverse(self):
        pass

    def visit(self):
        pass
















# class SelfRef():
#     name = ""
#     child = None
#     parent = None

#     def __init__(self, name, child = None):
#         self.name = name
#         if child:
#             self.child = child
#             child.parent = self


# if __name__ == "__main__":
    

#     c = SelfRef("foo")
#     p = SelfRef("par", c)


#     print(p.child.name)
#     print(c.parent.name)
