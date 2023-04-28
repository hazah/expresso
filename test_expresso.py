import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExpressoLexer import ExpressoLexer
from ExpressoParser import ExpressoParser
from ast_nodes import *
from expresso_listener import ExpressoListener

def parse_expresso_code(code):
    input_stream = InputStream(code)
    lexer = ExpressoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExpressoParser(token_stream)
    tree = parser.program()
    
    listener = ExpressoListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    return listener.stack[0]  # The AST for the whole program

class TestExpresso(unittest.TestCase):

    def test_type_declaration(self):
        code = "type Example;"
        expected_ast = [TypeDeclaration('Example', None)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_method_declaration(self):
        code = """
        type Example {
            method doSomething() {
            }
        }
        """
        method_body = MethodBody([])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        type_body = TypeBody([method_decl])
        expected_ast = [TypeDeclaration('Example', type_body)]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)
    
    def test_global_variable_declaration(self):
        code = "int ExampleVar = 0;"
        factor = Factor(0)
        term = Term(factor)
        expression = Expression(term)
        expected_ast = [VariableDeclaration('int', 'ExampleVar', expression)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_type_declaration_with_variable(self):
        code = """
        type Example {
            int exampleVar = 0;
        }
        """
        factor = Factor(0)
        term = Term(factor)
        expression = Expression(term)
        type_body = TypeBody([VariableDeclaration('int', 'exampleVar', expression)])
        expected_ast = [TypeDeclaration('Example', type_body)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_global_method_declaration(self):
        code = """
        method doSomething() {
        }
        """
        method_body = MethodBody([])
        expected_ast = [MethodDeclaration('doSomething', Params([]), method_body)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_multiple_declarations(self):
        code = """
        type Example {
            int exampleVar = 0;
            method doSomething() {
            }
        }
        int globalVar = 0;
        method doAnotherThing() {
        }
        """
        factor = Factor(0)
        term = Term(factor)
        expression = Expression(term)
        type_body = TypeBody([
            VariableDeclaration('int', 'exampleVar', expression),
            MethodDeclaration('doSomething', Params([]), MethodBody([]))
        ])
        expected_ast = [
            TypeDeclaration('Example', type_body),
            VariableDeclaration('int', 'globalVar', expression),
            MethodDeclaration('doAnotherThing', Params([]), MethodBody([]))
        ]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)
    
    def test_method_declaration_without_body(self):
        code = """
        method doSomething();
        """
        method_decl = MethodDeclaration('doSomething', Params([]), None)
        expected_ast = [method_decl]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_method_declaration_with_params_without_body(self):
        code = """
        method doSomething(int a, float b);
        """
        params_list = [VariableDeclaration("int", "a"), VariableDeclaration("float", "b")]
        params = Params(params_list)
        method_decl = MethodDeclaration('doSomething', params, None)
        expected_ast = [method_decl]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_method_declaration_without_body_inside_type(self):
        code = """
        type Example {
            method doSomething();
        }
        """
        method_decl = MethodDeclaration('doSomething', Params([]), None)
        type_body = TypeBody([method_decl])
        expected_ast = [TypeDeclaration('Example', type_body)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_variable_declaration_inside_method(self):
        code = """
        method doSomething() {
            int exampleVar = 0;
        }
        """
        factor = Factor(0)
        term = Term(factor)
        expression = Expression(term)
        variable_decl = VariableDeclaration("int", "exampleVar", expression)
        method_body = MethodBody([variable_decl])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)
    
    def test_variable_declaration_inside_method_inside_type(self):
        code = """
        type Example {
            method doSomething() {
                int exampleVar = 0;
            }
        }
        """
        factor = Factor(0)
        term = Term(factor)
        expression = Expression(term)
        variable_decl = VariableDeclaration("int", "exampleVar", expression)
        method_body = MethodBody([variable_decl])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        type_body = TypeBody([method_decl])
        expected_ast = [TypeDeclaration('Example', type_body)]
        self.assertEqual(parse_expresso_code(code).body, expected_ast)

        def test_single_number(self):
            code = """
            method doSomething() {
                42;
            }
            """
            method_body = MethodBody([
                Statement(Expression(Term(Factor(42))))
            ])
            method_decl = MethodDeclaration('doSomething', Params([]), method_body)
            expected_ast = [method_decl]

            self.assertEqual(parse_expresso_code(code).body, expected_ast)

        def test_single_variable(self):
            code = """
            method doSomething() {
                x;
            }
            """
            method_body = MethodBody([
                Statement(Expression(Term(Factor("x"))))
            ])
            method_decl = MethodDeclaration('doSomething', Params([]), method_body)
            expected_ast = [method_decl]

            self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_simple_addition(self):
        code = """
        method doSomething() {
            3 + 5;
        }
        """
        method_body = MethodBody([
            Statement(Expression(Term(Factor(3)), [('+', Term(Factor(5)))]))
        ])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_simple_multiplication(self):
        code = """
        method doSomething() {
            3 * 5;
        }
        """
        method_body = MethodBody([
            Statement(Expression(Term(Factor(3), [('*', Factor(5))])))
        ])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_combined_expression(self):
        code = """
        method doSomething() {
            1 + 2 * 3;
        }
        """
        method_body = MethodBody([
            Statement(Expression(Term(Factor(1)), [('+', Term(Factor(2), [('*', Factor(3))]))]))
        ])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_function_call_no_arguments(self):
        code = """
        method doSomething() {
            foo();
        }
        """
        method_body = MethodBody([
            Statement(Expression(Term(Factor(MethodCall("foo", [])))))
        ])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)

    def test_function_call_with_arguments(self):
        code = """
        method doSomething() {
            foo(1, 2, x);
        }
        """
        method_body = MethodBody([
            Statement(Expression(Term(Factor(MethodCall("foo", [
                Expression(Term(Factor(1))),
                Expression(Term(Factor(2))),
                Expression(Term(Factor("x")))
            ])))))
        ])
        method_decl = MethodDeclaration('doSomething', Params([]), method_body)
        expected_ast = [method_decl]

        self.assertEqual(parse_expresso_code(code).body, expected_ast)

# Add more test cases for other language features
if __name__ == '__main__':
    unittest.main()
