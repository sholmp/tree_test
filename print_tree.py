from tree import Node, Leaf, Visitor
from enum import Enum

class NodeStyle(Enum):
    INDENT = 1


class PrintTree(Visitor):
    def __init__(self, node_style):
        self.node_style = node_style

    def traverse(self, start_node: Node):
        print(start_node.name) # a tree is abstracted as a node with children
        if type(start_node) == Leaf:
            return
        for child in start_node.children:
            self.traverse(child)


if __name__ == "__main__":
    tree = Node("Scene", Leaf("Table"), Leaf("Object"))
    tree = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))

    pt = PrintTree(NodeStyle.INDENT)

    pt.traverse(tree)

