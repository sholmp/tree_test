from tree import Node, Leaf, Visitor
from enum import Enum

class NodeStyle(Enum):
    INDENT = 1
    BULLET = 2
    TREE = 3


vertical_line = '│'

root = '╿'

node_not_last_child = '├─┮'
node_last_child = '└─┮'

leaf_not_last_child = '├─╼'
leaf_last_child = '└─╼'

class PrintTree(Visitor):

    output = ""
    def traverseTreeStyle(self, node):
        line = ""
        if node.isRoot():
            line = root + node.name + '\n'
            self.output += line
            
        elif type(node) == Node:
            if node.parent.children[-1] == node: #last node on parents children
                line = node_last_child + node.name + '\n'
            else: #not last node of parents children
                line = node_not_last_child + node.name + '\n'
            self.output += line

        elif type(node) == Leaf:
            if node.parent.children[-1] == node: #last node on parents children
                line = leaf_last_child + node.name + '\n'
            else: #not the last leaf
                line = leaf_not_last_child + node.name + '\n'
            self.output += line
            return


        for child in node.children:
            self.traverseTreeStyle(child)



    def __init__(self, node_style: NodeStyle):
        if node_style == NodeStyle.INDENT:
            self.visitorFunction = self.printWithIndent
        elif node_style == NodeStyle.BULLET:
            self.visitorFunction = self.printWithBullet

    def printWithIndent(self, node: Node):
        self.output_string += '  ' * node.depth() + node.name + '\n'
    
    def printWithBullet(self, node: Node):
        self.output_string += '  ' * node.depth() + '* ' + node.name + '\n'

    

    def traverse(self, node: Node):
        self.output_string = ""
        self.traverseInternal(node)
        return self.output_string[:-1]

    def traverseInternal(self, node: Node):
        node.accept(self)
        if type(node) == Leaf:
            return
        for child in node.children:
            self.traverseInternal(child)

    def visit(self, node: Node):
        self.visitorFunction(node)




if __name__ == "__main__":
    tree = Leaf("Scene")
    tree = Node("Scene", Leaf("Table"), Leaf("Object"))
    # tree = Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))

    pt = PrintTree(NodeStyle.INDENT)

    # print(pt.traverse(tree))



    pt.traverseTreeStyle(tree)
    # pt.forwarder(tree)
    print(pt.output)


 






# def printNodeNameNothingElse(node: Node):
#     print(node.name)

# class PrintTree(Visitor):
#     def __init__(self, node_style):
#         self.node_style = node_style
#         if node_style == NodeStyle.INDENT:
#             self.prefix_token = ''
#         elif node_style == NodeStyle.BULLET:
#             self.prefix_token = '* '

#     def traverse(self, start_node: Node):
#         self.output_string = ""
#         self.traverseInternal(start_node)
#         self.output_string = self.output_string[:-1] # strip final new line to pass testcase
#         return self.output_string

#     def traverseInternal(self, start_node):
#         self.output_string += '  ' * start_node.depth() + self.prefix_token + start_node.name + '\n'

#         if type(start_node) == Leaf:
#             return
#         for child in start_node.children:
#             self.traverseInternal(child)

#     def forwarder(self, node):
#         self.output_string = ""
#         self.traverseFolderStructureWay(node)
#         return self.output_string

#     # not quite working... yet!
#     def traverseFolderStructureWay(self, node : Node):
#         if node.depth() > 1:
#             for i in range(1,node.depth()):
#                 self.output_string += " │  "

#         if type(node) == Leaf:
#             if node.parent == None: #
#                 self.output_string += f"─╼ {node.name}"
#             elif node.parent.children[-1] == node: # last element in current branch
#                 self.output_string += f"└─╼ {node.name}\n"
#             else: # we must be a leaf node on the middle of a branch
#                 self.output_string += f" ├─╼ {node.name}\n"
#             return
#         else: # we are a regular node
#             if node.isRoot():
#                 self.output_string += f" ╿ {node.name}\n"
#             elif node.parent.children[-1] == node: # last element in current branch
#                 self.output_string += f" └─┮ {node.name}\n"
#             else: # regular node middle of a branch
#                 self.output_string += f" ├─┮ {node.name}\n"

#         for child in node.children:
#             self.traverseFolderStructureWay(child)

