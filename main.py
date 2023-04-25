from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExpressoLexer import ExpressoLexer
from ExpressoParser import ExpressoParser
from expresso_listener import ExpressoListener

def main():
    input_str = "type Example { method test() { } }"
    input_stream = InputStream(input_str)
    lexer = ExpressoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExpressoParser(token_stream)
    tree = parser.program()

    listener = ExpressoListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Process the result, e.g., print the AST, execute the code, etc.
    program = listener.stack[0]  # Get the root Program node
    # ... (do something with the generated AST)

if __name__ == "__main__":
    main()
