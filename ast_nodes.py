class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self, body):
        self.body = body
    
    def __eq__(self, value):
        if not isinstance(value, Program):
            return False
        return self.body == value.body
    
    def __repr__(self):
        return f"Program(body={self.body})"


class TypeDeclaration(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body
    
    def __eq__(self, value):
        if not isinstance(value, TypeDeclaration):
            return False
        return self.name == value.name and self.body == value.body
    
    def __repr__(self):
        return f"TypeDeclaration(name={self.name}, body={self.body})"


class TypeBody(ASTNode):
    def __init__(self, body):
        self.body = body
    
    def __eq__(self, value):
        if not isinstance(value, TypeBody):
            return False
        return self.body == value.body
    
    def __repr__(self):
        return f"TypeBody(body={self.body})"


class MethodDeclaration(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    
    def __eq__(self, value):
        if not isinstance(value, MethodDeclaration):
            return False
        return self.name == value.name and self.params == value.params and self.body == value.body
    
    def __repr__(self):
        return f"MethodDeclaration(name={self.name}, params={self.params}, body={self.body})"


class Params(ASTNode):
    def __init__(self, parameters):
        self.parameters = parameters
    
    def __eq__(self, value):
        if not isinstance(value, Params):
            return False
        return self.parameters == value.parameters
    
    def __repr__(self):
        return f"Params(parameters={self.parameters})"


class MethodBody(ASTNode):
    def __init__(self, body):
        self.body = body
    
    def __eq__(self, value):
        if not isinstance(value, MethodBody):
            return False
        return self.body == value.body
    
    def __repr__(self):
        return f"MethodBody(body={self.body})"


class VariableDeclaration(ASTNode):
    def __init__(self, type, name, expression=None):
        self.type = type
        self.name = name
        self.expression = expression
    
    def __eq__(self, value):
        if not isinstance(value, VariableDeclaration):
            return False
        return self.type == value.type and self.name == value.name and self.expression == value.expression
    
    def __repr__(self):
        return f"VariableDeclaration(type={self.type}, name={self.name}, expression={self.expression})"

class Expression(ASTNode):
    def __init__(self, term, ops=None):
        self.term = term
        self.ops = ops or []

    def __eq__(self, other):
        if not isinstance(other, Expression):
            return False
        return self.term == other.term and self.ops == other.ops

    def __repr__(self):
        return f"Expression(term={self.term}, ops={self.ops})"


class Term(ASTNode):
    def __init__(self, factor, ops=None):
        self.factor = factor
        self.ops = ops or []

    def __eq__(self, other):
        if not isinstance(other, Term):
            return False
        return self.factor == other.factor and self.ops == other.ops

    def __repr__(self):
        return f"Term(factor={self.factor}, ops={self.ops})"


class Factor(ASTNode):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Factor):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"Factor(value={self.value})"


class FunctionCall(ASTNode):
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []

    def __eq__(self, other):
        if not isinstance(other, FunctionCall):
            return False
        return self.name == other.name and self.args == other.args

    def __repr__(self):
        return f"FunctionCall(name={self.name}, args={self.args})"

class Statement(ASTNode):
    def __init__(self, body):
        self.body = body

    def __eq__(self, other):
        if not isinstance(other, Statement):
            return False
        return self.body == other.body

    def __repr__(self):
        return f"Statement(body={self.body})"

class IfStatement(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def __eq__(self, other):
        if not isinstance(other, IfStatement):
            return False
        return self.condition == other.condition and self.block == other.block

    def __repr__(self):
        return f"IfStatement(condition={self.condition}, block={self.block})"

class Relational(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Relational):
            return False
        return self.left == other.left and self.op == other.op and self.right == other.right

    def __repr__(self):
        return f"Relational(left={self.left}, op={self.op}, right={self.right})"


class Equality(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Equality):
            return False
        return self.left == other.left and self.op == other.op and self.right == other.right

    def __repr__(self):
        return f"Equality(left={self.left}, op={self.op}, right={self.right})"


class And(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, And):
            return False
        return self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"And(left={self.left}, right={self.right})"


class Or(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Or):
            return False
        return self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"Or(left={self.left}, right={self.right})"


class Logic(ASTNode):
    def __init__(self, or_expression):
        self.or_expression = or_expression

    def __eq__(self, other):
        if not isinstance(other, Logic):
            return False
        return self.or_expression == other.or_expression

    def __repr__(self):
        return f"Logic(or_expression={self.or_expression})"


class Placeholder(ASTNode):
    def __eq__(self, value):
        if not isinstance(value, Placeholder):
            return False
        return True
    
    def __repr__(self):
        return f"Placeholder()"