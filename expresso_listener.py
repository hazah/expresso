# Purpose: Listener for the Expresso language

if __name__ is not None and "." in __name__:
    from .ExpressoParser import ExpressoParser
    from .ExpressoListener import ExpressoListener as ExpressoListenerBase
else:
    from ExpressoParser import ExpressoParser
    from ExpressoListener import ExpressoListener as ExpressoListenerBase

from ast_nodes import *


# This class defines a complete listener for a parse tree produced by ExpressoParser.
class ExpressoListener(ExpressoListenerBase):

    def __init__(self):
        self.stack = []

    # Enter a parse tree produced by ExpressoParser#program.
    def enterProgram(self, ctx:ExpressoParser.ProgramContext):
        program = Program([])
        self.stack.append(program)

    # Exit a parse tree produced by ExpressoParser#program.
    def exitProgram(self, ctx:ExpressoParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExpressoParser#type_declaration.
    def enterType_declaration(self, ctx:ExpressoParser.Type_declarationContext):
        type_name = ctx.ID().getText()
        type_node = TypeDeclaration(type_name, None)
        self.stack.append(type_node)

    # Exit a parse tree produced by ExpressoParser#type_declaration.
    def exitType_declaration(self, ctx:ExpressoParser.Type_declarationContext):
        type_node = self.stack.pop()  # Pop the list of nodes within the type
        self.stack[-1].body.append(type_node)  # Add the list of nodes to the type declaration



    # Enter a parse tree produced by ExpressoParser#type_body.
    def enterType_body(self, ctx:ExpressoParser.Type_bodyContext):
        type_body = TypeBody([])
        self.stack.append(type_body)

    # Exit a parse tree produced by ExpressoParser#type_body.
    def exitType_body(self, ctx:ExpressoParser.Type_bodyContext):
        type_body = self.stack.pop()
        self.stack[-1].body = type_body


    # Enter a parse tree produced by ExpressoParser#method_declaration.
    def enterMethod_declaration(self, ctx:ExpressoParser.Method_declarationContext):
        method_name = ctx.ID().getText()
        method_declration = MethodDeclaration(method_name, None, None)
        self.stack.append(method_declration)

    # Exit a parse tree produced by ExpressoParser#method_declaration.
    def exitMethod_declaration(self, ctx:ExpressoParser.Method_declarationContext):
        method_declaration = self.stack.pop()
        self.stack[-1].body.append(method_declaration)

    # Process a parameter
    def processParam(self, type_token, id_token):
        param_type = type_token.getText()
        param_name = id_token.getText()
        return VariableDeclaration(param_type, param_name)

    # Enter a parse tree produced by ExpressoParser#params.
    def enterParams(self, ctx:ExpressoParser.ParamsContext):
        param_count = len(ctx.type_name())
        params_list = [self.processParam(ctx.type_name(i), ctx.ID(i)) for i in range(param_count)]
        self.stack.append(params_list)

    # Exit a parse tree produced by ExpressoParser#params.
    def exitParams(self, ctx:ExpressoParser.ParamsContext):
        params_list = self.stack.pop()
        params = Params(params_list)
        method_declaration = self.stack[-1]
        method_declaration.params = params


    # Enter a parse tree produced by ExpressoParser#method_body.
    def enterMethod_body(self, ctx:ExpressoParser.Method_bodyContext):
        method_body = MethodBody([])
        self.stack.append(method_body)

    # Exit a parse tree produced by ExpressoParser#method_body.
    def exitMethod_body(self, ctx:ExpressoParser.Method_bodyContext):
        method_body = self.stack.pop()
        method_declaration = self.stack[-1]
        method_declaration.body = method_body


    # Enter a parse tree produced by ExpressoParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ExpressoParser.Variable_declarationContext):
        variable_type = ctx.type_name().getText()
        variable_name = ctx.ID().getText()
        variable_declaration = VariableDeclaration(variable_type, variable_name, None)
        self.stack.append(variable_declaration)

    # Exit a parse tree produced by ExpressoParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ExpressoParser.Variable_declarationContext):
        expression = self.stack.pop()
        variable_declaration = self.stack.pop()
        variable_declaration.expression = expression
        self.stack[-1].body.append(variable_declaration)


    # Enter a parse tree produced by ExpressoParser#statement.
    def enterStatement(self, ctx:ExpressoParser.StatementContext):
        statement = Statement(None)
        self.stack.append(statement)

    # Exit a parse tree produced by ExpressoParser#statement.
    def exitStatement(self, ctx:ExpressoParser.StatementContext):
        expression = self.stack.pop()
        statement = self.stack.pop()
        statement.body = expression
        self.stack[-1].body.append(statement)


    # Enter a parse tree produced by ExpressoParser#expression.
    def enterExpression(self, ctx:ExpressoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressoParser#expression.
    def exitExpression(self, ctx:ExpressoParser.ExpressionContext):
        terms = [self.stack.pop() for i in range(len(ctx.term()))][::-1]
        ops = [op.getText() for op in ctx.children if op.getText() in ('+', '-')]
        self.stack.append(Expression(terms.pop(0), [(op, terms.pop(0)) for op in ops]))


    # Enter a parse tree produced by ExpressoParser#term.
    def enterTerm(self, ctx:ExpressoParser.TermContext):
        pass

    # Exit a parse tree produced by ExpressoParser#term.
    def exitTerm(self, ctx:ExpressoParser.TermContext):
        factors = [self.stack.pop() for i in range(len(ctx.factor()))][::-1]
        ops = [op.getText() for op in ctx.children if op.getText() in ('*', '/')]
        self.stack.append(Term(factors.pop(0), [(op, factors.pop(0)) for op in ops]))


    # Enter a parse tree produced by ExpressoParser#factor.
    def enterFactor(self, ctx:ExpressoParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpressoParser#factor.
    def exitFactor(self, ctx:ExpressoParser.FactorContext):
        if ctx.expression():
            expr = self.stack.pop()
            self.stack.append(Factor(expr))
        elif ctx.method_call():
            method_call = self.stack.pop()
            self.stack.append(Factor(method_call))
        elif ctx.ID():
            id = ctx.ID().getText()
            self.stack.append(Factor(id))
        elif ctx.NUMBER():
            number = int(ctx.NUMBER().getText())
            self.stack.append(Factor(number))

    # Enter a parse tree produced by ExpressoParser#function_call.
    def enterMethod_call(self, ctx:ExpressoParser.Method_callContext):
        pass

    # Exit a parse tree produced by ExpressoParser#function_call.
    def exitMethod_call(self, ctx:ExpressoParser.Method_callContext):
        name = ctx.ID().getText()
        args = [self.stack.pop() for _ in range(len(ctx.value()))][::-1]
        self.stack.append(MethodCall(name, args))


    def enterRelational(self, ctx:ExpressoParser.RelationalContext):
        pass

    def exitRelational(self, ctx:ExpressoParser.RelationalContext):
        left = self.stack.pop()
        right = self.stack.pop()
        op = ctx.getChild(1).getText()
        relational = Relational(left, op, right)
        self.stack.append(relational)

    def enterEquality(self, ctx:ExpressoParser.EqualityContext):
        pass

    def exitEquality(self, ctx:ExpressoParser.EqualityContext):
        left = self.stack.pop()
        right = self.stack.pop()
        op = ctx.getChild(1).getText()
        equality = Equality(left, op, right)
        self.stack.append(equality)

    def enterAnd(self, ctx:ExpressoParser.AndContext):
        pass

    def exitAnd(self, ctx:ExpressoParser.AndContext):
        left = self.stack.pop()
        right = self.stack.pop()
        and_node = And(left, right)
        self.stack.append(and_node)

    def enterOr(self, ctx:ExpressoParser.OrContext):
        pass

    def exitOr(self, ctx:ExpressoParser.OrContext):
        left = self.stack.pop()
        right = self.stack.pop()
        or_node = Or(left, right)
        self.stack.append(or_node)

    def enterLogic(self, ctx:ExpressoParser.LogicContext):
        pass

    def exitLogic(self, ctx:ExpressoParser.LogicContext):
        or_expression = self.stack.pop()
        logic_node = Logic(or_expression)
        self.stack.append(logic_node)


    # Enter a parse tree produced by ExpressoParser#placeholder.
    def enterPlaceholder(self, ctx:ExpressoParser.PlaceholderContext):
        pass

    # Exit a parse tree produced by ExpressoParser#placeholder.
    def exitPlaceholder(self, ctx:ExpressoParser.PlaceholderContext):
        pass


    # Enter a parse tree produced by ExpressoParser#type.
    def enterType(self, ctx:ExpressoParser.Type_nameContext):
        pass

    # Exit a parse tree produced by ExpressoParser#type.
    def exitType(self, ctx:ExpressoParser.Type_nameContext):
        pass



del ExpressoParser