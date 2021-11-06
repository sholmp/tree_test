from tree import Node, Leaf, Visitor
from enum import Enum

class NodeStyle(Enum):
    INDENT = 1
    BULLET = 2



# ╿ Scene
#  ├─┮ Robot
#  │ ├─┮ Flange
#  │ │ └─┮ Gripper
#  │ │   └─╼ Objec

class PrintTree(Visitor):
    def __init__(self, node_style):
        self.node_style = node_style
        if node_style == NodeStyle.INDENT:
            self.prefix_token = ''
        elif node_style == NodeStyle.BULLET:
            self.prefix_token = '* '

    def traverse(self, start_node: Node):
        self.output_string = ""
        self.traverseInternal(start_node)
        self.output_string = self.output_string[:-1] # strip final new line to pass testcase
        return self.output_string

    def traverseInternal(self, start_node):
        self.output_string += '  ' * start_node.depth() + self.prefix_token + start_node.name + '\n'

        if type(start_node) == Leaf:
            return
        for child in start_node.children:
            self.traverseInternal(child)

if __name__ == "__main__":
    tree = Node("Scene", Leaf("Table"), Leaf("Object"))
    tree = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))
    
    trees = [
        Leaf("Scene"),
        Node("Scene", Leaf("Table"), Leaf("Object")),
        Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))
    ]
    expected = [
        "Scene",
        "Scene\n  Table\n  Object",
        "Scene\n  Robot\n    Flange\n      Gripper\n        Object\n    Camera\n  Table\n    Box"
    ]

    visitor = PrintTree(NodeStyle.INDENT)

    result = visitor.traverse(trees[1])
    print(result)

    # for i, c in enumerate(zip(trees, expected)):
    #     print(f"{i} -- {c}")
    #         # with self.subTest(i=i):
    #         #     self.assertEqual(visitor.traverse(c[0]), c[1])



