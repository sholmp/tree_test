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
        super().__init__("Add", args)

if __name__ == "__main__":
    i = Integer(123)

    f = Float(5.0)
    print(f.name)
    print(i.name)

    a = Add(i,f)
