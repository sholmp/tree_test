from tree import Visitor, Node, Leaf

class EvaluateExpression(Visitor):
    pass

class PrintExpression(Visitor):
    pass

class Integer(Leaf):
    def __init__(self, value):
        self.value = value
        name = "Integer(" + str(value) + ')'
        super().__init__(name)

class Float(Leaf):
    def __init__(self, value):
        self.value = value
        name = "Float(" + str(value) + ')'
        super().__init__(name)

class Add(Node):
    def __init__(self, *args):
        name = "Add"
        super().__init__(name, *args)

class Divide(Node):
    def __init__(self, *args):
        name = "Divide"
        super().__init__(name, *args)

class Multiply(Node):
    def __init__(self, *args):
        name = "Multiply"
        super().__init__(name, *args)


if __name__ == "__main__":
    i = Integer(123)

    f = Float(5.0)

    a = Add(i,f)

    print(issubclass(type(a), Node))
    print(issubclass(type(f), Node))



