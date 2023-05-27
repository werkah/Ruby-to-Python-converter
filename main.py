from antlr4 import *
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from grammar.RubyVisitor import RubyVisitor

def main():
    inp = FileStream("examples/mathOperations.rb")
    lexer = RubyLexer(inp)
    stream = CommonTokenStream(lexer)

    parser = RubyParser(stream)
    tree = parser.program()

    visitor = RubyVisitor()
    res = visitor.visit(tree)

    output = open("output.py", "w")
    output.write(res)
    output.close()


if __name__ == '__main__':
    main()