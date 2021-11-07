from tree import Node, Leaf, Visitor
from enum import Enum

from indentation_symbols import TreeStyleSymbols as tss

class NodeStyle(Enum):
    INDENT = 1
    BULLET = 2
    TREE = 3
    
class PrintTree(Visitor):
    def __init__(self, node_style: NodeStyle):
        if node_style == NodeStyle.INDENT:
            self.visitorFunction = self.printWithIndent
        elif node_style == NodeStyle.BULLET:
            self.visitorFunction = self.printWithBullet
        elif node_style == NodeStyle.TREE:
            self.visitorFunction = self.printWithTreeStyle
        else:
            self.visitorFunction = self.doNothing

    def doNothing():
        pass

    def printWithIndent(self, node: Node):
        self.output_string += '  ' * node.depth() + node.name + '\n'
    
    def printWithBullet(self, node: Node):
        self.output_string += '  ' * node.depth() + '* ' + node.name + '\n'

    def printWithTreeStyle(self, node):
        line = ""
        if node.isRoot():
            if len(node.children) == 0:
                line = f"{tss.root_alone_symbol} {node.name}\n"
            else:
                line = f" {tss.root_symbol} {node.name}\n "
            
        elif type(node) == Node:
            if node.parent.children[-1] == node: #last node on parents children
                line = f"{tss.node_last_child} {node.name}\n "
            else: #not last node of parents children
                line = f"{tss.node_not_last_child} {node.name}\n "

        elif type(node) == Leaf:
            if node.parent.children[-1] == node: #last node on parents children
                line = f"{tss.leaf_last_child} {node.name}\n "
            else: #not the last leaf
                line = f"{tss.leaf_not_last_child} {node.name}\n "

        # add vertical lines or spaces
        temp = node
        while temp.depth() >= 2:
            if temp.parent == temp.parent.parent.children[-1]: # last child in parent's parent's children
                line = tss.dead_space + line
            else:
                line = tss.vertical_line + line
            temp = temp.parent
           
        self.output_string += line
       

    def traverse(self, node: Node):
        self.output_string = ""
        self.traverseInternal(node)
        return self.output_string.rstrip() #remove trailing newline (also removes a trailing space applying to tree style visitor)

    def traverseInternal(self, node: Node):
        node.accept(self)
        if type(node) == Leaf:
            return
        for child in node.children:
            self.traverseInternal(child)

    def visit(self, node: Node):
        self.visitorFunction(node)




if __name__ == "__main__":
    # tree1 = Leaf("Scene")
    # tree2 = Node("Scene", Leaf("Table"), Leaf("Object"))
    tree3 = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))

    pt1 = PrintTree(NodeStyle.INDENT)
    pt2 = PrintTree(NodeStyle.BULLET)
    pt3 = PrintTree(NodeStyle.TREE)

    
    print("-" * 5 + "Indent style" + "-" * 5)
    print(pt1.traverse(tree3))
    print("\n" + "-" * 5 + "Bullet style" + "-" * 5)
    print(pt2.traverse(tree3))
    print("\n" + "-" * 5 + "Tree style" + "-" * 5)
    print(pt3.traverse(tree3))

