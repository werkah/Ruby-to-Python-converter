# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser

# This class defines a complete generic visitor for a parse tree produced by RubyParser.

class RubyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RubyParser#program.
    def visitProgram(self, ctx:RubyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#statementList.
    def visitStatementList(self, ctx:RubyParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#terminator.
    def visitTerminator(self, ctx:RubyParser.TerminatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#statement.
    def visitStatement(self, ctx:RubyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#functions.
    def visitFunctions(self, ctx:RubyParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#instructions.
    def visitInstructions(self, ctx:RubyParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#loop.
    def visitLoop(self, ctx:RubyParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#bool.
    def visitBool(self, ctx:RubyParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#type.
    def visitType(self, ctx:RubyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#array.
    def visitArray(self, ctx:RubyParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#value.
    def visitValue(self, ctx:RubyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#ifInstruction.
    def visitIfInstruction(self, ctx:RubyParser.IfInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#unlessInstruction.
    def visitUnlessInstruction(self, ctx:RubyParser.UnlessInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#whileLoop.
    def visitWhileLoop(self, ctx:RubyParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#forLoop.
    def visitForLoop(self, ctx:RubyParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#untilLoop.
    def visitUntilLoop(self, ctx:RubyParser.UntilLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:RubyParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#operator.
    def visitOperator(self, ctx:RubyParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#condition.
    def visitCondition(self, ctx:RubyParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#variables.
    def visitVariables(self, ctx:RubyParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#sign.
    def visitSign(self, ctx:RubyParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#mathOperation.
    def visitMathOperation(self, ctx:RubyParser.MathOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#bracketExpression.
    def visitBracketExpression(self, ctx:RubyParser.BracketExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#function.
    def visitFunction(self, ctx:RubyParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#parameters.
    def visitParameters(self, ctx:RubyParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#class.
    def visitClass(self, ctx:RubyParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#classBody.
    def visitClassBody(self, ctx:RubyParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#functionCall.
    def visitFunctionCall(self, ctx:RubyParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:RubyParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#loopBody.
    def visitLoopBody(self, ctx:RubyParser.LoopBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#assignment.
    def visitAssignment(self, ctx:RubyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#classObject.
    def visitClassObject(self, ctx:RubyParser.ClassObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#methodCall.
    def visitMethodCall(self, ctx:RubyParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#putsFunction.
    def visitPutsFunction(self, ctx:RubyParser.PutsFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RubyParser#crlf.
    def visitCrlf(self, ctx:RubyParser.CrlfContext):
        return self.visitChildren(ctx)



del RubyParser