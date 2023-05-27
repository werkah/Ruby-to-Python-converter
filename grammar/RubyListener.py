# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser

# This class defines a complete listener for a parse tree produced by RubyParser.
class RubyListener(ParseTreeListener):

    # Enter a parse tree produced by RubyParser#program.
    def enterProgram(self, ctx:RubyParser.ProgramContext):
        pass

    # Exit a parse tree produced by RubyParser#program.
    def exitProgram(self, ctx:RubyParser.ProgramContext):
        pass


    # Enter a parse tree produced by RubyParser#statementList.
    def enterStatementList(self, ctx:RubyParser.StatementListContext):
        pass

    # Exit a parse tree produced by RubyParser#statementList.
    def exitStatementList(self, ctx:RubyParser.StatementListContext):
        pass


    # Enter a parse tree produced by RubyParser#terminator.
    def enterTerminator(self, ctx:RubyParser.TerminatorContext):
        pass

    # Exit a parse tree produced by RubyParser#terminator.
    def exitTerminator(self, ctx:RubyParser.TerminatorContext):
        pass


    # Enter a parse tree produced by RubyParser#statement.
    def enterStatement(self, ctx:RubyParser.StatementContext):
        pass

    # Exit a parse tree produced by RubyParser#statement.
    def exitStatement(self, ctx:RubyParser.StatementContext):
        pass


    # Enter a parse tree produced by RubyParser#functions.
    def enterFunctions(self, ctx:RubyParser.FunctionsContext):
        pass

    # Exit a parse tree produced by RubyParser#functions.
    def exitFunctions(self, ctx:RubyParser.FunctionsContext):
        pass


    # Enter a parse tree produced by RubyParser#instructions.
    def enterInstructions(self, ctx:RubyParser.InstructionsContext):
        pass

    # Exit a parse tree produced by RubyParser#instructions.
    def exitInstructions(self, ctx:RubyParser.InstructionsContext):
        pass


    # Enter a parse tree produced by RubyParser#loop.
    def enterLoop(self, ctx:RubyParser.LoopContext):
        pass

    # Exit a parse tree produced by RubyParser#loop.
    def exitLoop(self, ctx:RubyParser.LoopContext):
        pass


    # Enter a parse tree produced by RubyParser#bool.
    def enterBool(self, ctx:RubyParser.BoolContext):
        pass

    # Exit a parse tree produced by RubyParser#bool.
    def exitBool(self, ctx:RubyParser.BoolContext):
        pass


    # Enter a parse tree produced by RubyParser#array.
    def enterArray(self, ctx:RubyParser.ArrayContext):
        pass

    # Exit a parse tree produced by RubyParser#array.
    def exitArray(self, ctx:RubyParser.ArrayContext):
        pass


    # Enter a parse tree produced by RubyParser#value.
    def enterValue(self, ctx:RubyParser.ValueContext):
        pass

    # Exit a parse tree produced by RubyParser#value.
    def exitValue(self, ctx:RubyParser.ValueContext):
        pass


    # Enter a parse tree produced by RubyParser#ifInstruction.
    def enterIfInstruction(self, ctx:RubyParser.IfInstructionContext):
        pass

    # Exit a parse tree produced by RubyParser#ifInstruction.
    def exitIfInstruction(self, ctx:RubyParser.IfInstructionContext):
        pass


    # Enter a parse tree produced by RubyParser#elseInstruction.
    def enterElseInstruction(self, ctx:RubyParser.ElseInstructionContext):
        pass

    # Exit a parse tree produced by RubyParser#elseInstruction.
    def exitElseInstruction(self, ctx:RubyParser.ElseInstructionContext):
        pass


    # Enter a parse tree produced by RubyParser#elsifInstruction.
    def enterElsifInstruction(self, ctx:RubyParser.ElsifInstructionContext):
        pass

    # Exit a parse tree produced by RubyParser#elsifInstruction.
    def exitElsifInstruction(self, ctx:RubyParser.ElsifInstructionContext):
        pass


    # Enter a parse tree produced by RubyParser#unlessInstruction.
    def enterUnlessInstruction(self, ctx:RubyParser.UnlessInstructionContext):
        pass

    # Exit a parse tree produced by RubyParser#unlessInstruction.
    def exitUnlessInstruction(self, ctx:RubyParser.UnlessInstructionContext):
        pass


    # Enter a parse tree produced by RubyParser#whileLoop.
    def enterWhileLoop(self, ctx:RubyParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by RubyParser#whileLoop.
    def exitWhileLoop(self, ctx:RubyParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by RubyParser#forLoop.
    def enterForLoop(self, ctx:RubyParser.ForLoopContext):
        pass

    # Exit a parse tree produced by RubyParser#forLoop.
    def exitForLoop(self, ctx:RubyParser.ForLoopContext):
        pass


    # Enter a parse tree produced by RubyParser#untilLoop.
    def enterUntilLoop(self, ctx:RubyParser.UntilLoopContext):
        pass

    # Exit a parse tree produced by RubyParser#untilLoop.
    def exitUntilLoop(self, ctx:RubyParser.UntilLoopContext):
        pass


    # Enter a parse tree produced by RubyParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:RubyParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by RubyParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:RubyParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by RubyParser#operator.
    def enterOperator(self, ctx:RubyParser.OperatorContext):
        pass

    # Exit a parse tree produced by RubyParser#operator.
    def exitOperator(self, ctx:RubyParser.OperatorContext):
        pass


    # Enter a parse tree produced by RubyParser#condition.
    def enterCondition(self, ctx:RubyParser.ConditionContext):
        pass

    # Exit a parse tree produced by RubyParser#condition.
    def exitCondition(self, ctx:RubyParser.ConditionContext):
        pass


    # Enter a parse tree produced by RubyParser#variables.
    def enterVariables(self, ctx:RubyParser.VariablesContext):
        pass

    # Exit a parse tree produced by RubyParser#variables.
    def exitVariables(self, ctx:RubyParser.VariablesContext):
        pass


    # Enter a parse tree produced by RubyParser#mathOperation.
    def enterMathOperation(self, ctx:RubyParser.MathOperationContext):
        pass

    # Exit a parse tree produced by RubyParser#mathOperation.
    def exitMathOperation(self, ctx:RubyParser.MathOperationContext):
        pass


    # Enter a parse tree produced by RubyParser#bracketExpression.
    def enterBracketExpression(self, ctx:RubyParser.BracketExpressionContext):
        pass

    # Exit a parse tree produced by RubyParser#bracketExpression.
    def exitBracketExpression(self, ctx:RubyParser.BracketExpressionContext):
        pass


    # Enter a parse tree produced by RubyParser#function.
    def enterFunction(self, ctx:RubyParser.FunctionContext):
        pass

    # Exit a parse tree produced by RubyParser#function.
    def exitFunction(self, ctx:RubyParser.FunctionContext):
        pass


    # Enter a parse tree produced by RubyParser#parameters.
    def enterParameters(self, ctx:RubyParser.ParametersContext):
        pass

    # Exit a parse tree produced by RubyParser#parameters.
    def exitParameters(self, ctx:RubyParser.ParametersContext):
        pass


    # Enter a parse tree produced by RubyParser#class.
    def enterClass(self, ctx:RubyParser.ClassContext):
        pass

    # Exit a parse tree produced by RubyParser#class.
    def exitClass(self, ctx:RubyParser.ClassContext):
        pass


    # Enter a parse tree produced by RubyParser#classBody.
    def enterClassBody(self, ctx:RubyParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by RubyParser#classBody.
    def exitClassBody(self, ctx:RubyParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by RubyParser#functionCall.
    def enterFunctionCall(self, ctx:RubyParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by RubyParser#functionCall.
    def exitFunctionCall(self, ctx:RubyParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by RubyParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:RubyParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by RubyParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:RubyParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by RubyParser#loopBody.
    def enterLoopBody(self, ctx:RubyParser.LoopBodyContext):
        pass

    # Exit a parse tree produced by RubyParser#loopBody.
    def exitLoopBody(self, ctx:RubyParser.LoopBodyContext):
        pass


    # Enter a parse tree produced by RubyParser#assignment.
    def enterAssignment(self, ctx:RubyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#assignment.
    def exitAssignment(self, ctx:RubyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#classObject.
    def enterClassObject(self, ctx:RubyParser.ClassObjectContext):
        pass

    # Exit a parse tree produced by RubyParser#classObject.
    def exitClassObject(self, ctx:RubyParser.ClassObjectContext):
        pass


    # Enter a parse tree produced by RubyParser#methodCall.
    def enterMethodCall(self, ctx:RubyParser.MethodCallContext):
        pass

    # Exit a parse tree produced by RubyParser#methodCall.
    def exitMethodCall(self, ctx:RubyParser.MethodCallContext):
        pass


    # Enter a parse tree produced by RubyParser#putsFunction.
    def enterPutsFunction(self, ctx:RubyParser.PutsFunctionContext):
        pass

    # Exit a parse tree produced by RubyParser#putsFunction.
    def exitPutsFunction(self, ctx:RubyParser.PutsFunctionContext):
        pass


    # Enter a parse tree produced by RubyParser#crlf.
    def enterCrlf(self, ctx:RubyParser.CrlfContext):
        pass

    # Exit a parse tree produced by RubyParser#crlf.
    def exitCrlf(self, ctx:RubyParser.CrlfContext):
        pass



del RubyParser