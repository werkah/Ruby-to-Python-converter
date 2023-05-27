# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser


# This class defines a complete generic visitor for a parse tree produced by RubyParser.

class RubyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RubyParser#program.
    def visitProgram(self, ctx: RubyParser.ProgramContext):  # ok
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#statementList.
    def visitStatementList(self, ctx: RubyParser.StatementListContext):  # ok
        result = []
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            if statement:
                result.append(statement)
        return ''.join(result)

    # Visit a parse tree produced by RubyParser#terminator.
    def visitTerminator(self, ctx: RubyParser.TerminatorContext):  # ?
        return "\n"

    # Visit a parse tree produced by RubyParser#statement.
    def visitStatement(self, ctx: RubyParser.StatementContext):  # ok
        if ctx.functions():
            return self.visitFunctions(ctx.functions())
        elif ctx.instructions():
            return self.visitInstructions(ctx.instructions())
        elif ctx.loop():
            return self.visitLoop(ctx.loop())
        elif ctx.variables():
            return self.visitVariables(ctx.variables())
        elif ctx.assignment():
            return self.visitAssignment(ctx.assignment())
        elif ctx.classObject():
            return self.visitClassObject(ctx.classObject())
        elif ctx.methodCall():
            return self.visitMethodCall(ctx.methodCall())
        elif ctx.COMMENT():
            return f"{ctx.getText()}"
        elif ctx.putsFunction():
            return self.visitPutsFunction(ctx.putsFunction())
        elif ctx.class_():
            return self.visitClass_(ctx.class_())

    # Visit a parse tree produced by RubyParser#functions.
    def visitFunctions(self, ctx: RubyParser.FunctionsContext):  # ok
        if ctx.function():
            return self.visit(ctx.function())
        else:
            return self.visit(ctx.functionCall())

    # Visit a parse tree produced by RubyParser#instructions.
    def visitInstructions(self, ctx: RubyParser.InstructionsContext):  # ok
        if ctx.ifInstruction():
            return self.visit(ctx.ifInstruction())
        else:
            return self.visit(ctx.unlessInstruction())

    # Visit a parse tree produced by RubyParser#loop.
    def visitLoop(self, ctx: RubyParser.LoopContext):  # ok
        if ctx.whileLoop():
            return self.visit(ctx.whileLoop())
        elif ctx.forLoop():
            return self.visit(ctx.forLoop())
        else:
            return self.visit(ctx.untilLoop())

    # Visit a parse tree produced by RubyParser#bool.
    def visitBool(self, ctx: RubyParser.BoolContext):
        if ctx.NIL():
            return "None"
        return ctx.getText()[0].upper() + ctx.getText()[1:]

    # Visit a parse tree produced by RubyParser#type.
    def visitType(self, ctx: RubyParser.TypeContext):  # usunac
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#array.
    def visitArray(self, ctx: RubyParser.ArrayContext):  # ok ale czy da sie zejsc nizej?
        result = ""
        for child in ctx.getChildren():
            if child.getChildCount() == 0:
                res = child.getText()
                result += res
            else:
                result += str(self.visit(child))
        return result

    # Visit a parse tree produced by RubyParser#value.
    def visitValue(self, ctx: RubyParser.ValueContext):  # ok ale czy da sie zejsc nizej?
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#ifInstruction.
    def visitIfInstruction(self, ctx: RubyParser.IfInstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#unlessInstruction.
    def visitUnlessInstruction(self, ctx: RubyParser.UnlessInstructionContext):
        return self.visitChildren(ctx)

    def visitElseInstruction(self, ctx: RubyParser.ElseInstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#elsifInstruction.
    def visitElsifInstruction(self, ctx: RubyParser.ElsifInstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#whileLoop.
    def visitWhileLoop(self, ctx: RubyParser.WhileLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#forLoop.
    def visitForLoop(self, ctx: RubyParser.ForLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#untilLoop.
    def visitUntilLoop(self, ctx: RubyParser.UntilLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#comparisonOperator.
    def visitComparisonOperator(self, ctx: RubyParser.ComparisonOperatorContext):  # ok
        operator = ctx.getText()
        if operator == '==':
            return '=='
        elif operator == '!=':
            return '!='
        elif operator == '>':
            return '>'
        elif operator == '>=':
            return '>='
        elif operator == '<':
            return '<'
        elif operator == '<=':
            return '<='
        elif operator == '<=>':
            return '<=>'
        elif operator == '===':
            return '==='

    # Visit a parse tree produced by RubyParser#operator.
    def visitOperator(self, ctx: RubyParser.OperatorContext):  # ok
        operator = ctx.getText()
        if operator == '+':
            return '+'
        elif operator == '-':
            return '-'
        elif operator == '*':
            return '*'
        elif operator == '/':
            return '/'
        elif operator == '%':
            return '%'
        elif operator == '**':
            return '**'
        elif operator == '++':
            return '++'
        elif operator == '--':
            return '--'

    # Visit a parse tree produced by RubyParser#condition.
    def visitCondition(self, ctx: RubyParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#variables.
    def visitVariables(self, ctx: RubyParser.VariablesContext):  # ok
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        return res

    # Visit a parse tree produced by RubyParser#mathOperation.
    def visitMathOperation(self, ctx: RubyParser.MathOperationContext):  # ok
        result = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                result += child.getText()
            else:
                result += str(self.visit(child))
        return result

    # Visit a parse tree produced by RubyParser#bracketExpression.
    def visitBracketExpression(self, ctx: RubyParser.BracketExpressionContext):  # ok
        return "(" + self.visit(ctx.mathOperation()) + ")"

    # Visit a parse tree produced by RubyParser#function.
    def visitFunction(self, ctx: RubyParser.FunctionContext):
        function_name = ctx.getChild(1).getText()
        if self.visitParameters(ctx.getChild(3)) != "":
            parameters = (self.visitParameters(ctx.getChild(3)))
            body = str(self.visitLoopBody(ctx.getChild(6)))
            indent = "    "
            result = f"def {function_name}({parameters}):\n"
            body_lines = body.strip().split("\n")
            if body_lines:
                result += "\n".join(indent + line for line in body_lines)
            else:
                result += indent + "pass"
            if ctx.RETURN() is not None:
                return_value = (self.visitParameters(ctx.getChild(8)))
                result += f"\n    return {return_value}"
        else:
            body = str(self.visitLoopBody(ctx.getChild(5)))
            indent = "    "
            result = f"def {function_name}():\n"
            body_lines = body.strip().split("\n")
            if body_lines:
                result += "\n".join(indent + line for line in body_lines)
            else:
                result += indent + "pass"
            if ctx.RETURN() is not None:
                return_value = (self.visitParameters(ctx.getChild(7)))
                result += f"\n    return {return_value}"
        return result

    # Visit a parse tree produced by RubyParser#parameters.
    def visitParameters(self, ctx: RubyParser.ParametersContext):  # ok
        result = ""
        for i in range(0, ctx.getChildCount()):
            result += ctx.getChild(i).getText()
        return result

    # Visit a parse tree produced by RubyParser#class.
    def visitClass_(self, ctx: RubyParser.ClassContext):
        class_name = ctx.CLASSNAME().getText()
        class_body = str(self.visitClassBody(ctx.getChild(3)))
        indent = "    "
        result = f"class {class_name}:\n"
        body_lines = class_body.strip().split("\n")
        if body_lines:
            result += "\n".join(indent + line for line in body_lines)
        else:
            result += indent + "pass"
        return result

    # Visit a parse tree produced by RubyParser#classBody.
    def visitClassBody(self, ctx: RubyParser.ClassBodyContext):
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        return res

    # Visit a parse tree produced by RubyParser#functionCall.
    def visitFunctionCall(self, ctx: RubyParser.FunctionCallContext):  # ok
        result = ""
        result += ctx.getChild(0).getText()
        result += "("
        result += str(self.visitParameters(ctx.getChild(2)))
        result += ")"
        return result

    # Visit a parse tree produced by RubyParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: RubyParser.AssignmentOperatorContext):  # ok
        operator = ctx.getText()
        if operator == '+=':
            return '+='
        elif operator == '-=':
            return '-='
        elif operator == '*=':
            return '*='
        elif operator == '**=':
            return '**='
        elif operator == '/=':
            return '%'
        elif operator == '%=':
            return '%='

    # Visit a parse tree produced by RubyParser#loopBody.
    def visitLoopBody(self, ctx: RubyParser.LoopBodyContext):  # ok
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        return res

    # Visit a parse tree produced by RubyParser#assignment.
    def visitAssignment(self, ctx: RubyParser.AssignmentContext):  # ok
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        return res

    # Visit a parse tree produced by RubyParser#classObject.
    def visitClassObject(self, ctx: RubyParser.ClassObjectContext):  # ok
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i) == ctx.ID():
                result = str(ctx.ID().getText())
            elif ctx.getChild(i) == ctx.DOT():
                result += str(ctx.DOT().getText())
            elif ctx.getChild(i) == ctx.CLASSNAME():
                result += str(ctx.CLASSNAME().getText())
            elif ctx.getChild(i) == ctx.NEW():
                result += str(ctx.NEW().getText())
            elif ctx.getChild(i) == ctx.EQUAL():
                result += str(ctx.EQUAL().getText())
        return result

    # Visit a parse tree produced by RubyParser#methodCall.
    def visitMethodCall(self, ctx: RubyParser.MethodCallContext):  # ok
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i) == ctx.ID():
                result = str(ctx.ID().getText())
            elif ctx.getChild(i) == ctx.DOT():
                result += str(ctx.DOT().getText())
            elif ctx.getChild(i) == ctx.functionCall():
                result += str(self.visit(ctx.functionCall()))
        return result

    # Visit a parse tree produced by RubyParser#putsFunction.
    def visitPutsFunction(self, ctx: RubyParser.PutsFunctionContext):  # ok
        res = ""
        children = ctx.children
        for child in children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        if children[0].getText() == "puts":
            res = res.replace("puts", "print")
        return res

    # Visit a parse tree produced by RubyParser#crlf.
    def visitCrlf(self, ctx: RubyParser.CrlfContext):  # ok?
        return "\n"


del RubyParser