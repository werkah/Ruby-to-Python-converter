# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.12.0
from antlr4 import *
from grammar.RubyParser import RubyParser


# This class defines a complete generic visitor for a parse tree produced by RubyParser.

class RubyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RubyParser#program.
    def visitProgram(self, ctx: RubyParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#statementList.
    def visitStatementList(self, ctx: RubyParser.StatementListContext):
        result = []
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            if statement:
                result.append(statement)
        return ''.join(result)

    # Visit a parse tree produced by RubyParser#terminator.
    def visitTerminator(self, ctx:RubyParser.TerminatorContext):
        return "\n"

    # Visit a parse tree produced by RubyParser#statement.
    def visitStatement(self, ctx: RubyParser.StatementContext):
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
        else:
            raise NotImplementedError(f"Not implemented: {ctx.getText()}")

    # Visit a parse tree produced by RubyParser#functions.
    def visitFunctions(self, ctx: RubyParser.FunctionsContext):
        if ctx.function():
            return self.visit(ctx.function())
        else:
            return self.visit(ctx.functionCall())

    # Visit a parse tree produced by RubyParser#instructions.
    def visitInstructions(self, ctx: RubyParser.InstructionsContext):
        if ctx.ifInstruction():
            return self.visit(ctx.ifInstruction())
        else:
            return self.visit(ctx.unlessInstruction())

    # Visit a parse tree produced by RubyParser#loop.
    def visitLoop(self, ctx: RubyParser.LoopContext):
        if ctx.whileLoop():
            return self.visit(ctx.whileLoop())
        elif ctx.forLoop():
            return self.visit(ctx.forLoop())
        else:
            return self.visit(ctx.untilLoop())

    # Visit a parse tree produced by RubyParser#bool.
    def visitBool(self, ctx: RubyParser.BoolContext):
        return ctx.getText()[0].upper() + ctx.getText()[1:]

    # Visit a parse tree produced by RubyParser#type.
    def visitType(self, ctx: RubyParser.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#array.
    def visitArray(self, ctx: RubyParser.ArrayContext):
        result = ""
        for child in ctx.getChildren():
            if child.getChildCount() == 0:
                res = child.getText()
                result += res
            else:
                result += str(self.visit(child))
        return result

    # Visit a parse tree produced by RubyParser#value.
    def visitValue(self, ctx: RubyParser.ValueContext):
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
    def visitComparisonOperator(self, ctx: RubyParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#operator.
    def visitOperator(self, ctx: RubyParser.OperatorContext):
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
    def visitVariables(self, ctx: RubyParser.VariablesContext):
        var_value = self.visit(ctx.getChild(2))
        return f"{ctx.ID()[0].getText()} = {var_value}"

    # Visit a parse tree produced by RubyParser#sign.
    def visitSign(self, ctx: RubyParser.SignContext):
        if ctx.PLUS():
            return '+'
        else:
            return '-'

    # Visit a parse tree produced by RubyParser#mathOperation.
    def visitMathOperation(self, ctx):
        result = ""
        if ctx.sign():
            result += str(self.visitSign(ctx.sign()))
        result += str(self.visit(ctx.getChild(0)))
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getChildCount() == 0:
                res = child.getText()
                result += res
            else:
                result += str(self.visit(child))
        return result

    # Visit a parse tree produced by RubyParser#bracketExpression.
    def visitBracketExpression(self, ctx):
        return "(" + self.visit(ctx.mathOperation()) + ")"

    # Visit a parse tree produced by RubyParser#function.
    def visitFunction(self, ctx: RubyParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#parameters.
    def visitParameters(self, ctx: RubyParser.ParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#class.
    def visitClass_(self, ctx: RubyParser.ClassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#classBody.
    def visitClassBody(self, ctx: RubyParser.ClassBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#functionCall.
    def visitFunctionCall(self, ctx: RubyParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: RubyParser.AssignmentOperatorContext):
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
    def visitLoopBody(self, ctx: RubyParser.LoopBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#assignment.
    def visitAssignment(self, ctx: RubyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#classObject.
    def visitClassObject(self, ctx: RubyParser.ClassObjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#methodCall.
    def visitMethodCall(self, ctx: RubyParser.MethodCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#putsFunction.
    def visitPutsFunction(self, ctx: RubyParser.PutsFunctionContext):
        value = self.visit(ctx.getChild(2))
        return f"print({value})"

    # Visit a parse tree produced by RubyParser#crlf.
    def visitCrlf(self, ctx: RubyParser.CrlfContext):
        return "\n"


del RubyParser
