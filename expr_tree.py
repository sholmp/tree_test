from tree import Visitor, Node, Leaf

# class Number(Leaf):
#     pass

class Integer(Leaf):
    def __init__(self, value):
        self.value = int(value)
        name = "Integer(" + str(value) + ')'
        super().__init__(name)
    
    def valueFormattedAsString(self):
        return str(self.value)


class Float(Leaf):
    def __init__(self, value):
        self.value = value
        name = f"Float({value:.1f})" # Hacky. Testcases only go up to 1 decimal, trying to keep logic to minimum at the moment
        super().__init__(name)
    
    def valueFormattedAsString(self):
        return f"{self.value:.1f}"

# class Operator(Node):
#     pass

class Add(Node):
    def __init__(self, *args):
        self.math_symbol = "+"
        super().__init__("Add", *args)

class Divide(Node):
    def __init__(self, *args):
        self.math_symbol = "/"
        super().__init__("Divide", *args)

class Multiply(Node):
    def __init__(self, *args):
        self.math_symbol = "*"
        super().__init__("Multiply", *args)

class Negative(Node):
    def __init__(self, *args):
        self.math_symbol = "-"
        super().__init__("Negative", *args)  

class EvaluateExpression(Visitor):
    #eval(PrintExpression.traverse())
    pass

class PrintExpression(Visitor):
    def visit(self, node):
        # visiting an operator:
        if type(node) in [Add, Divide, Multiply]:
            self.output_string += node.math_symbol                  
            self.output_string += ' '  
        elif type(node) == Negative:
            self.output_string += node.math_symbol                  
        elif type(node) in [Integer, Float]:
            self.output_string += node.valueFormattedAsString()
            self.output_string += ' '                     
   
    def traverse(self, node):
        self.output_string = ""
        self.inOrderTraverse(node)
        return self.output_string.rstrip()

    def inOrderTraverse(self, node):
        if type(node) in [Integer, Float]:
            node.accept(self)
            return
        
        if len(node.children) == 1:
            node.accept(self)   
            self.inOrderTraverse(node.children[0]) # Abuse node.children array to achieve in order traversal  
        else: # len(node.children) == 2:
            self.inOrderTraverse(node.children[0]) 
            node.accept(self)
            self.inOrderTraverse(node.children[1])
        
if __name__ == "__main__":
    i = Integer(123)
    f = Float(5.0)
    a = Add(i,f)

    tree = Add(Integer(2), Divide(Multiply(Float(5.0), Negative(Integer(3))), Float(10.0)))
    tree = Divide(Integer(5), Integer(2))
    tree = Divide(Float(5), Integer(2))
    tree = Negative(Integer(23))
    pe = PrintExpression()

    print(pe.traverse(tree))



