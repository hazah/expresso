# Generated from Expresso.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExpressoParser import ExpressoParser
else:
    from ExpressoParser import ExpressoParser

# This class defines a complete listener for a parse tree produced by ExpressoParser.
class ExpressoListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressoParser#program.
    def enterProgram(self, ctx:ExpressoParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExpressoParser#program.
    def exitProgram(self, ctx:ExpressoParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExpressoParser#type_declaration.
    def enterType_declaration(self, ctx:ExpressoParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by ExpressoParser#type_declaration.
    def exitType_declaration(self, ctx:ExpressoParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by ExpressoParser#type_body.
    def enterType_body(self, ctx:ExpressoParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by ExpressoParser#type_body.
    def exitType_body(self, ctx:ExpressoParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by ExpressoParser#method_declaration.
    def enterMethod_declaration(self, ctx:ExpressoParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by ExpressoParser#method_declaration.
    def exitMethod_declaration(self, ctx:ExpressoParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by ExpressoParser#params.
    def enterParams(self, ctx:ExpressoParser.ParamsContext):
        pass

    # Exit a parse tree produced by ExpressoParser#params.
    def exitParams(self, ctx:ExpressoParser.ParamsContext):
        pass


    # Enter a parse tree produced by ExpressoParser#method_body.
    def enterMethod_body(self, ctx:ExpressoParser.Method_bodyContext):
        pass

    # Exit a parse tree produced by ExpressoParser#method_body.
    def exitMethod_body(self, ctx:ExpressoParser.Method_bodyContext):
        pass


    # Enter a parse tree produced by ExpressoParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ExpressoParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ExpressoParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ExpressoParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ExpressoParser#statement.
    def enterStatement(self, ctx:ExpressoParser.StatementContext):
        pass

    # Exit a parse tree produced by ExpressoParser#statement.
    def exitStatement(self, ctx:ExpressoParser.StatementContext):
        pass


    # Enter a parse tree produced by ExpressoParser#block.
    def enterBlock(self, ctx:ExpressoParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpressoParser#block.
    def exitBlock(self, ctx:ExpressoParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpressoParser#value.
    def enterValue(self, ctx:ExpressoParser.ValueContext):
        pass

    # Exit a parse tree produced by ExpressoParser#value.
    def exitValue(self, ctx:ExpressoParser.ValueContext):
        pass


    # Enter a parse tree produced by ExpressoParser#logic.
    def enterLogic(self, ctx:ExpressoParser.LogicContext):
        pass

    # Exit a parse tree produced by ExpressoParser#logic.
    def exitLogic(self, ctx:ExpressoParser.LogicContext):
        pass


    # Enter a parse tree produced by ExpressoParser#or.
    def enterOr(self, ctx:ExpressoParser.OrContext):
        pass

    # Exit a parse tree produced by ExpressoParser#or.
    def exitOr(self, ctx:ExpressoParser.OrContext):
        pass


    # Enter a parse tree produced by ExpressoParser#and.
    def enterAnd(self, ctx:ExpressoParser.AndContext):
        pass

    # Exit a parse tree produced by ExpressoParser#and.
    def exitAnd(self, ctx:ExpressoParser.AndContext):
        pass


    # Enter a parse tree produced by ExpressoParser#equality.
    def enterEquality(self, ctx:ExpressoParser.EqualityContext):
        pass

    # Exit a parse tree produced by ExpressoParser#equality.
    def exitEquality(self, ctx:ExpressoParser.EqualityContext):
        pass


    # Enter a parse tree produced by ExpressoParser#relational.
    def enterRelational(self, ctx:ExpressoParser.RelationalContext):
        pass

    # Exit a parse tree produced by ExpressoParser#relational.
    def exitRelational(self, ctx:ExpressoParser.RelationalContext):
        pass


    # Enter a parse tree produced by ExpressoParser#expression.
    def enterExpression(self, ctx:ExpressoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressoParser#expression.
    def exitExpression(self, ctx:ExpressoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpressoParser#term.
    def enterTerm(self, ctx:ExpressoParser.TermContext):
        pass

    # Exit a parse tree produced by ExpressoParser#term.
    def exitTerm(self, ctx:ExpressoParser.TermContext):
        pass


    # Enter a parse tree produced by ExpressoParser#factor.
    def enterFactor(self, ctx:ExpressoParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpressoParser#factor.
    def exitFactor(self, ctx:ExpressoParser.FactorContext):
        pass


    # Enter a parse tree produced by ExpressoParser#method_call.
    def enterMethod_call(self, ctx:ExpressoParser.Method_callContext):
        pass

    # Exit a parse tree produced by ExpressoParser#method_call.
    def exitMethod_call(self, ctx:ExpressoParser.Method_callContext):
        pass


    # Enter a parse tree produced by ExpressoParser#placeholder.
    def enterPlaceholder(self, ctx:ExpressoParser.PlaceholderContext):
        pass

    # Exit a parse tree produced by ExpressoParser#placeholder.
    def exitPlaceholder(self, ctx:ExpressoParser.PlaceholderContext):
        pass


    # Enter a parse tree produced by ExpressoParser#type_name.
    def enterType_name(self, ctx:ExpressoParser.Type_nameContext):
        pass

    # Exit a parse tree produced by ExpressoParser#type_name.
    def exitType_name(self, ctx:ExpressoParser.Type_nameContext):
        pass



del ExpressoParser