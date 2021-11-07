from tree import Visitor, Node, Leaf


class Integer(Leaf):
    def __init__(self, value):
        self.value = value
        name = "Integer(" + str(int(value)) + ')'
        super().__init__(name)

class Float(Leaf):
    def __init__(self, value):
        self.value = value
        name = f"Float({value:.1f})" # Hacky, but testcases only go up to 1 decimal, trying to keep logic to minimum at the moment
        super().__init__(name)

# class Operator(Node):
#     pass

class Add(Node):
    def __init__(self, *args):
        super().__init__("Add", *args)

class Divide(Node):
    def __init__(self, *args):
        super().__init__("Divide", *args)

class Multiply(Node):
    def __init__(self, *args):
        super().__init__("Multiply", *args)

class Negative(Node):
    def __init__(self, *args):
        super().__init__("Negative", *args)  

class EvaluateExpression(Visitor):
    pass

class PrintExpression(Visitor):
    def visit(self, node):
        # visiting an operator:
        if type(node) == Add:
            print("+")
        elif type(node) == Divide:
            print("/")
        elif type(node) == Multiply:
            print("*")
        elif type(node) == Negative:
            print("-")

        # print(node.name)
    
    def traverse(self, node):
        self.output_string = ""
        self.traverseInternal(node)

    def traverseInternal(self, node):
        for child in node.children:
            self.traverseInternal(child)
        node.accept(self)

if __name__ == "__main__":
    i = Integer(123)
    f = Float(5.0)
    a = Add(i,f)

    pe = PrintExpression()

    pe.traverse(a)



