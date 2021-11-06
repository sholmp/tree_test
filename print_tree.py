from tree import Node, Leaf, Visitor
from enum import Enum

class NodeStyle(Enum):
    INDENT = 1
    BULLET = 2
    TREE = 3

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

    def forwarder(self, node):
        self.output_string = ""
        self.traverseFolderStructureWay(node)
        return self.output_string

    # not quite working... yet!
    def traverseFolderStructureWay(self, node : Node):
        if node.depth() > 1:
            for i in range(1,node.depth()):
                self.output_string += " │  "

        if type(node) == Leaf:
            if node.parent == None: #
                self.output_string += f"─╼ {node.name}"
            elif node.parent.children[-1] == node: # last element in current branch
                self.output_string += f"└─╼ {node.name}\n"
            else: # we must be a leaf node on the middle of a branch
                self.output_string += f" ├─╼ {node.name}\n"
            return
        else: # we are a regular node
            if node.isRoot():
                self.output_string += f" ╿ {node.name}\n"
            elif node.parent.children[-1] == node: # last element in current branch
                self.output_string += f" └─┮ {node.name}\n"
            else: # regular node middle of a branch
                self.output_string += f" ├─┮ {node.name}\n"

        for child in node.children:
            self.traverseFolderStructureWay(child)


if __name__ == "__main__":
    tree = Leaf("Scene")
    tree = Node("Scene", Leaf("Table"), Leaf("Object"))
    tree = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))

    pt = PrintTree(NodeStyle.TREE)

    output = pt.forwarder(tree)
    print(output)

 





