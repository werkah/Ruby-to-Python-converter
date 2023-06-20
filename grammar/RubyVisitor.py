# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser


# This class defines a complete generic visitor for a parse tree produced by RubyParser.

class RubyVisitor(ParseTreeVisitor):
    def __init__(self):
        self.vars = []
        self.functions = []
        self.classes = []
        self.current_class = None
        self.objects = []
        self.errors = []


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
    def visitTerminator(self, ctx: RubyParser.TerminatorContext):
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
        res = ""
        if ctx.NIL() is not None:
            res += "None"
        else:
            res += ctx.getText()[0].upper() + ctx.getText()[1:]
        return res

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
        result = ""
        i = 0
        result += ctx.getChild(0).getText()
        result += str(self.visitCondition(ctx.getChild(1))) + "\n"
        body = str(self.visitLoopBody(ctx.getChild(3)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        for i in range(4, ctx.getChildCount()):
            if i == ctx.getChildCount() - 1:
                result += ""
            else:
                result += str(self.visit(ctx.getChild(i))) + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#unlessInstruction.
    def visitUnlessInstruction(self, ctx: RubyParser.UnlessInstructionContext):
        result = ""
        if ctx.getChild(0) == ctx.UNLESS():
            result += "if not"
        result += str(self.visitCondition(ctx.getChild(1))) + "\n"
        body = str(self.visitLoopBody(ctx.getChild(3)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        for i in range(4, ctx.getChildCount()):
            if i == ctx.getChildCount() - 1:
                result += ""
            else:
                result += str(self.visit(ctx.getChild(i))) + "\n"
        return result[:-1]

    def visitElseInstruction(self, ctx: RubyParser.ElseInstructionContext):
        result = ""
        result += ctx.getChild(0).getText() + ":\n"
        body = self.visitLoopBody(ctx.getChild(2))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#elsifInstruction.
    def visitElsifInstruction(self, ctx: RubyParser.ElsifInstructionContext):
        result = ""
        r = ctx.getChild(0)
        if r == ctx.ELSIF():
            result += "elif"
        result += str(self.visitCondition(ctx.getChild(1))) + "\n"
        body = str(self.visitLoopBody(ctx.getChild(3)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#whileLoop.
    def visitWhileLoop(self, ctx: RubyParser.WhileLoopContext):
        result = ""
        result += ctx.getChild(0).getText()
        result += str(self.visitCondition(ctx.getChild(1))) + "\n"
        body = str(self.visitLoopBody(ctx.getChild(4)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#forLoop.
    def visitForLoop(self, ctx: RubyParser.ForLoopContext):
        result = ""
        result += ctx.getChild(0).getText() + " "
        # result += ctx.getChild(1).getText() + " "
        if ctx.getChild(1).getText() in self.vars:
            result += ctx.getChild(1).getText() + " "
        else:
            self.vars.append(ctx.getChild(1).getText())
            result += ctx.getChild(1).getText() + " "
        result += ctx.getChild(2).getText() + " "
        result += ctx.getChild(3).getText() + ":\n"
        body = str(self.visitLoopBody(ctx.getChild(5)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#untilLoop.
    def visitUntilLoop(self, ctx: RubyParser.UntilLoopContext):
        result = ""
        if ctx.getChild(0) == ctx.UNTIL():
            result += "while not"
        result += str(self.visitCondition(ctx.getChild(1))) + "\n"
        body = str(self.visitLoopBody(ctx.getChild(4)))
        body_lines = body.strip().split("\n")
        for line in body_lines:
            result += "    " + line + "\n"
        return result[:-1]

    # Visit a parse tree produced by RubyParser#comparisonOperator.
    def visitComparisonOperator(self, ctx: RubyParser.ComparisonOperatorContext):
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
        result = " "
        for i in range(0, ctx.getChildCount()):
            if str(ctx.getChild(i)) == "and":
                result += " and "
            elif str(ctx.getChild(i)) == "or":
                result += " or "
            elif ctx.getChild(i).getChildCount() == 0:
                if ctx.getChild(i).getText() in self.vars:
                    result += ctx.getChild(i).getText()
                else:
                    error = f"Variable '{ctx.getChild(i).getText()}' does not exist."
                    self.errors.append(error)
            else:
                result += str(self.visit(ctx.getChild(i)))
        return result + ":"

    # Visit a parse tree produced by RubyParser#variables.
    def visitVariables(self, ctx: RubyParser.VariablesContext):
        res = ""
        if ctx.getChild(0) not in self.vars:
            self.vars.append(ctx.getChild(0).getText())
            res += ctx.getChild(0).getText()
            res += ctx.getChild(1).getText()
        else:
            res += ctx.getChild(0).getText()
            res += ctx.getChild(1).getText()

        if ctx.getChild(2) == ctx.value():
            res += str(self.visit(ctx.getChild(2)))
        if ctx.getChild(2) != ctx.mathOperation() and ctx.getChild(2) != ctx.value() and ctx.getChild(2) != ctx.array() \
                and ctx.getChild(2) != ctx.bool_() and ctx.EQUAL():
            if ctx.getChild(2).getText() in self.vars:
                res += ctx.getChild(2).getText()
            else:
                error = f"Variable '{ctx.getChild(2).getText()}' does not exist."
                self.errors.append(error)
        if ctx.getChild(2) == ctx.mathOperation():
            res += str(self.visit(ctx.getChild(2)))
        if ctx.getChild(2) == ctx.array():
            res += str(self.visit(ctx.getChild(2)))
        if ctx.getChild(2) == ctx.bool_():
            res += str(self.visit(ctx.getChild(2)))
        return res
    # Visit a parse tree produced by RubyParser#mathOperation.
    def visitMathOperation(self, ctx: RubyParser.MathOperationContext):
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i).getChildCount() == 0:
                if ctx.getChild(i).getText() in self.vars:
                    result += ctx.getChild(i).getText()
                else:
                    error = f"Variable '{ctx.getChild(i).getText()}' does not exist."
                    self.errors.append(error)
            else:
                result += str(self.visit(ctx.getChild(i)))
        return result


    # Visit a parse tree produced by RubyParser#bracketExpression.
    def visitBracketExpression(self, ctx: RubyParser.BracketExpressionContext):
        return "(" + self.visit(ctx.mathOperation()) + ")"

    # Visit a parse tree produced by RubyParser#function.
    def visitFunction(self, ctx: RubyParser.FunctionContext):
        function_name = ctx.getChild(1).getText()
        if self.current_class is not None:
            class_function_list = getattr(self, self.current_class, [])
            class_function_list.append(function_name)
            setattr(self, self.current_class, class_function_list)
        elif function_name in self.functions:
            error = f"Function '{function_name}' is already declared."
            self.errors.append(error)
        else:
            self.functions.append(function_name)
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
    def visitParameters(self, ctx: RubyParser.ParametersContext):
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i).getText() in self.vars:
                result += ctx.getChild(i).getText()
            else:
                self.vars.append(ctx.getChild(i).getText())
                result += ctx.getChild(i).getText()
        return result

    # Visit a parse tree produced by RubyParser#class.
    def visitClass_(self, ctx: RubyParser.ClassContext):
        class_name = ctx.CLASSNAME().getText()
        if class_name in self.classes:
            error = f"Class '{class_name}' is already declared."
            self.errors.append(error)
        else:
            self.classes.append(class_name)
            self.current_class = class_name
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
    def visitFunctionCall(self, ctx: RubyParser.FunctionCallContext):
        function_name = ctx.getChild(0).getText()
        if self.current_class is not None:
            class_function_list = getattr(self, self.current_class, [])
            if function_name not in class_function_list:
                error = f"Function '{function_name}' is not defined in class '{self.current_class}'."
                self.errors.append(error)
        elif function_name not in self.functions:
            error = f"Function '{function_name}' is not defined."
            self.errors.append(error)
        result = ""
        result += function_name
        result += "("
        result += str(self.visitParameters(ctx.getChild(2)))
        result += ")"
        return result

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
        res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))
        return res

    # Visit a parse tree produced by RubyParser#assignment.
    def visitAssignment(self, ctx: RubyParser.AssignmentContext):
        res = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i).getChildCount() == 0:
                if ctx.getChild(i).getText() in self.vars:
                    res += ctx.getChild(i).getText()
                else:
                    error = f"Variable'{ctx.getChild(i).getText()}' does not exist."
                    self.errors.append(error)
            else:
                res += str(self.visit(ctx.getChild(i)))
        return res



    # Visit a parse tree produced by RubyParser#classObject.
    def visitClassObject(self, ctx: RubyParser.ClassObjectContext):
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i) == ctx.ID():
                object_id = str(ctx.ID().getText())
                self.objects.append(object_id)
                result = object_id
            elif ctx.getChild(i) == ctx.CLASSNAME():
                obj_class = str(ctx.CLASSNAME().getText())
                if obj_class not in self.classes:
                    error = f"Class '{obj_class}' is not declared."
                    self.errors.append(error)
                else:
                    result += obj_class
            elif ctx.getChild(i) == ctx.NEW():
                result += "()"
            elif ctx.getChild(i) == ctx.EQUAL():
                result += str(ctx.EQUAL().getText())
        return result

    # Visit a parse tree produced by RubyParser#methodCall.
    def visitMethodCall(self, ctx: RubyParser.MethodCallContext):
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i) == ctx.ID():
                objct_id = str(ctx.ID().getText())
                if objct_id not in self.objects:
                    error = f"Object '{objct_id}' is not declared."
                    self.errors.append(error)
                else:
                    result += objct_id
            elif ctx.getChild(i) == ctx.DOT():
                result += str(ctx.DOT().getText())
            elif ctx.getChild(i) == ctx.functionCall():
                result += str(self.visit(ctx.functionCall()))
        return result

    # Visit a parse tree produced by RubyParser#putsFunction.
    def visitPutsFunction(self, ctx: RubyParser.PutsFunctionContext):
        res = ""
        children = ctx.children

        for child in children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += str(self.visit(child))

        if children[0].getText() == "puts":
            res = res.replace("puts", "print")
        if ctx.getChild(2).getText() == ctx.ID():
            id_name = ctx.getChild(2).getText()
            if id_name not in self.vars:
                raise ValueError(f"Variable '{id_name}' is not declared.")

        return res

del RubyParser