# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,366,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,
        1,1,1,1,1,1,1,1,5,1,86,8,1,10,1,12,1,89,9,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,3,4,107,8,4,1,5,
        1,5,3,5,111,8,5,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,9,3,9,125,8,9,1,9,1,9,1,9,3,9,130,8,9,5,9,132,8,9,10,9,12,9,135,
        9,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,146,8,11,10,
        11,12,11,149,9,11,1,11,3,11,152,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,3,12,160,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,
        14,3,14,172,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,3,20,206,8,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,216,8,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,231,8,
        20,5,20,233,8,20,10,20,12,20,236,9,20,1,21,3,21,239,8,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,3,21,248,8,21,1,22,1,22,1,22,3,22,253,
        8,22,1,22,1,22,1,22,1,22,3,22,259,8,22,5,22,261,8,22,10,22,12,22,
        264,9,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,274,8,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,283,8,24,1,24,1,24,1,25,1,
        25,1,25,3,25,290,8,25,1,25,1,25,1,25,1,25,3,25,296,8,25,5,25,298,
        8,25,10,25,12,25,301,9,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
        3,27,311,8,27,1,27,1,27,5,27,315,8,27,10,27,12,27,318,9,27,1,28,
        1,28,1,28,3,28,323,8,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,5,30,
        332,8,30,10,30,12,30,335,9,30,1,31,1,31,1,31,1,31,3,31,341,8,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,3,34,360,8,34,1,34,1,34,1,35,1,35,1,35,0,1,2,
        36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,8,1,0,32,33,1,0,20,21,
        1,0,22,24,2,0,12,12,60,60,1,0,48,55,1,0,40,47,1,0,18,19,1,0,34,39,
        383,0,72,1,0,0,0,2,79,1,0,0,0,4,90,1,0,0,0,6,102,1,0,0,0,8,106,1,
        0,0,0,10,110,1,0,0,0,12,115,1,0,0,0,14,117,1,0,0,0,16,119,1,0,0,
        0,18,121,1,0,0,0,20,138,1,0,0,0,22,140,1,0,0,0,24,155,1,0,0,0,26,
        161,1,0,0,0,28,166,1,0,0,0,30,175,1,0,0,0,32,182,1,0,0,0,34,190,
        1,0,0,0,36,197,1,0,0,0,38,199,1,0,0,0,40,215,1,0,0,0,42,238,1,0,
        0,0,44,252,1,0,0,0,46,265,1,0,0,0,48,269,1,0,0,0,50,289,1,0,0,0,
        52,302,1,0,0,0,54,316,1,0,0,0,56,319,1,0,0,0,58,326,1,0,0,0,60,333,
        1,0,0,0,62,336,1,0,0,0,64,342,1,0,0,0,66,348,1,0,0,0,68,352,1,0,
        0,0,70,363,1,0,0,0,72,73,3,2,1,0,73,1,1,0,0,0,74,75,6,1,-1,0,75,
        76,3,6,3,0,76,77,3,4,2,0,77,80,1,0,0,0,78,80,3,4,2,0,79,74,1,0,0,
        0,79,78,1,0,0,0,80,87,1,0,0,0,81,82,10,2,0,0,82,83,3,6,3,0,83,84,
        3,4,2,0,84,86,1,0,0,0,85,81,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,3,1,0,0,0,89,87,1,0,0,0,90,91,7,0,0,0,91,5,1,0,
        0,0,92,103,3,8,4,0,93,103,3,10,5,0,94,103,3,12,6,0,95,103,3,42,21,
        0,96,103,3,62,31,0,97,103,3,64,32,0,98,103,3,66,33,0,99,103,5,61,
        0,0,100,103,3,68,34,0,101,103,3,52,26,0,102,92,1,0,0,0,102,93,1,
        0,0,0,102,94,1,0,0,0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,
        0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,
        103,7,1,0,0,0,104,107,3,48,24,0,105,107,3,56,28,0,106,104,1,0,0,
        0,106,105,1,0,0,0,107,9,1,0,0,0,108,111,3,22,11,0,109,111,3,28,14,
        0,110,108,1,0,0,0,110,109,1,0,0,0,111,11,1,0,0,0,112,116,3,30,15,
        0,113,116,3,32,16,0,114,116,3,34,17,0,115,112,1,0,0,0,115,113,1,
        0,0,0,115,114,1,0,0,0,116,13,1,0,0,0,117,118,7,1,0,0,118,15,1,0,
        0,0,119,120,7,2,0,0,120,17,1,0,0,0,121,124,5,29,0,0,122,125,3,20,
        10,0,123,125,3,14,7,0,124,122,1,0,0,0,124,123,1,0,0,0,125,133,1,
        0,0,0,126,129,5,31,0,0,127,130,3,20,10,0,128,130,3,14,7,0,129,127,
        1,0,0,0,129,128,1,0,0,0,130,132,1,0,0,0,131,126,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,
        1,0,0,0,136,137,5,30,0,0,137,19,1,0,0,0,138,139,7,3,0,0,139,21,1,
        0,0,0,140,141,5,1,0,0,141,142,3,40,20,0,142,143,3,70,35,0,143,147,
        3,60,30,0,144,146,3,26,13,0,145,144,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,150,
        152,3,24,12,0,151,150,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,
        154,5,4,0,0,154,23,1,0,0,0,155,156,5,3,0,0,156,159,3,70,35,0,157,
        160,3,60,30,0,158,160,5,64,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,
        25,1,0,0,0,161,162,5,2,0,0,162,163,3,40,20,0,163,164,3,70,35,0,164,
        165,3,60,30,0,165,27,1,0,0,0,166,167,5,5,0,0,167,168,3,40,20,0,168,
        169,3,70,35,0,169,171,3,60,30,0,170,172,3,24,12,0,171,170,1,0,0,
        0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,4,0,0,174,29,1,0,0,0,
        175,176,5,7,0,0,176,177,3,40,20,0,177,178,5,6,0,0,178,179,3,70,35,
        0,179,180,3,60,30,0,180,181,5,4,0,0,181,31,1,0,0,0,182,183,5,10,
        0,0,183,184,5,59,0,0,184,185,5,11,0,0,185,186,5,59,0,0,186,187,3,
        70,35,0,187,188,3,60,30,0,188,189,5,4,0,0,189,33,1,0,0,0,190,191,
        5,9,0,0,191,192,3,40,20,0,192,193,5,6,0,0,193,194,3,70,35,0,194,
        195,3,60,30,0,195,196,5,4,0,0,196,35,1,0,0,0,197,198,7,4,0,0,198,
        37,1,0,0,0,199,200,7,5,0,0,200,39,1,0,0,0,201,202,5,59,0,0,202,205,
        3,36,18,0,203,206,3,20,10,0,204,206,3,14,7,0,205,203,1,0,0,0,205,
        204,1,0,0,0,206,216,1,0,0,0,207,208,3,20,10,0,208,209,3,36,18,0,
        209,210,3,20,10,0,210,216,1,0,0,0,211,212,5,59,0,0,212,213,3,36,
        18,0,213,214,5,59,0,0,214,216,1,0,0,0,215,201,1,0,0,0,215,207,1,
        0,0,0,215,211,1,0,0,0,216,234,1,0,0,0,217,230,7,6,0,0,218,219,5,
        59,0,0,219,220,3,36,18,0,220,221,3,20,10,0,221,231,1,0,0,0,222,223,
        3,20,10,0,223,224,3,36,18,0,224,225,3,20,10,0,225,231,1,0,0,0,226,
        227,5,59,0,0,227,228,3,36,18,0,228,229,5,59,0,0,229,231,1,0,0,0,
        230,218,1,0,0,0,230,222,1,0,0,0,230,226,1,0,0,0,231,233,1,0,0,0,
        232,217,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,
        235,41,1,0,0,0,236,234,1,0,0,0,237,239,3,16,8,0,238,237,1,0,0,0,
        238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,59,0,0,241,247,5,56,0,
        0,242,248,3,20,10,0,243,248,5,59,0,0,244,248,3,18,9,0,245,248,3,
        44,22,0,246,248,3,14,7,0,247,242,1,0,0,0,247,243,1,0,0,0,247,244,
        1,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,43,1,0,0,0,249,253,5,
        59,0,0,250,253,3,20,10,0,251,253,3,46,23,0,252,249,1,0,0,0,252,250,
        1,0,0,0,252,251,1,0,0,0,253,262,1,0,0,0,254,258,3,38,19,0,255,259,
        5,59,0,0,256,259,3,20,10,0,257,259,3,46,23,0,258,255,1,0,0,0,258,
        256,1,0,0,0,258,257,1,0,0,0,259,261,1,0,0,0,260,254,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,45,1,0,0,0,264,262,
        1,0,0,0,265,266,5,27,0,0,266,267,3,44,22,0,267,268,5,28,0,0,268,
        47,1,0,0,0,269,270,5,16,0,0,270,271,5,59,0,0,271,273,5,27,0,0,272,
        274,3,50,25,0,273,272,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,
        276,5,28,0,0,276,277,3,70,35,0,277,282,3,60,30,0,278,279,5,17,0,
        0,279,280,3,50,25,0,280,281,3,70,35,0,281,283,1,0,0,0,282,278,1,
        0,0,0,282,283,1,0,0,0,283,284,1,0,0,0,284,285,5,4,0,0,285,49,1,0,
        0,0,286,290,5,59,0,0,287,290,3,20,10,0,288,290,3,14,7,0,289,286,
        1,0,0,0,289,287,1,0,0,0,289,288,1,0,0,0,290,299,1,0,0,0,291,295,
        5,31,0,0,292,296,5,59,0,0,293,296,3,20,10,0,294,296,3,14,7,0,295,
        292,1,0,0,0,295,293,1,0,0,0,295,294,1,0,0,0,296,298,1,0,0,0,297,
        291,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,
        51,1,0,0,0,301,299,1,0,0,0,302,303,5,15,0,0,303,304,5,13,0,0,304,
        305,3,70,35,0,305,306,3,54,27,0,306,307,5,4,0,0,307,53,1,0,0,0,308,
        311,3,42,21,0,309,311,3,48,24,0,310,308,1,0,0,0,310,309,1,0,0,0,
        311,312,1,0,0,0,312,313,3,70,35,0,313,315,1,0,0,0,314,310,1,0,0,
        0,315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,55,1,0,0,0,
        318,316,1,0,0,0,319,320,5,59,0,0,320,322,5,27,0,0,321,323,3,50,25,
        0,322,321,1,0,0,0,322,323,1,0,0,0,323,324,1,0,0,0,324,325,5,28,0,
        0,325,57,1,0,0,0,326,327,7,7,0,0,327,59,1,0,0,0,328,329,3,6,3,0,
        329,330,3,70,35,0,330,332,1,0,0,0,331,328,1,0,0,0,332,335,1,0,0,
        0,333,331,1,0,0,0,333,334,1,0,0,0,334,61,1,0,0,0,335,333,1,0,0,0,
        336,337,5,59,0,0,337,340,3,58,29,0,338,341,3,20,10,0,339,341,5,59,
        0,0,340,338,1,0,0,0,340,339,1,0,0,0,341,63,1,0,0,0,342,343,5,59,
        0,0,343,344,5,56,0,0,344,345,5,13,0,0,345,346,5,57,0,0,346,347,5,
        14,0,0,347,65,1,0,0,0,348,349,5,59,0,0,349,350,5,57,0,0,350,351,
        3,56,28,0,351,67,1,0,0,0,352,353,5,58,0,0,353,359,5,27,0,0,354,360,
        5,59,0,0,355,360,3,20,10,0,356,360,3,18,9,0,357,360,3,56,28,0,358,
        360,3,66,33,0,359,354,1,0,0,0,359,355,1,0,0,0,359,356,1,0,0,0,359,
        357,1,0,0,0,359,358,1,0,0,0,360,361,1,0,0,0,361,362,5,28,0,0,362,
        69,1,0,0,0,363,364,5,32,0,0,364,71,1,0,0,0,33,79,87,102,106,110,
        115,124,129,133,147,151,159,171,205,215,230,234,238,247,252,258,
        262,273,282,289,295,299,310,316,322,333,340,359
    ]

class RubyParser ( Parser ):

    grammarFileName = "Ruby.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elsif'", "'else'", "'end'", 
                     "'unless'", "'do'", "'while'", "'begin'", "'until'", 
                     "'for'", "'in'", "<INVALID>", "<INVALID>", "'new'", 
                     "'class'", "'def'", "'return'", "' and '", "' or '", 
                     "'true'", "'false'", "'@'", "'@@'", "'$'", "'#'", "'''", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "';'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'**='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'**'", "'++'", "'--'", 
                     "'>'", "'<'", "'<='", "'>='", "'<=>'", "'=='", "'!='", 
                     "'==='", "'='", "'.'", "'puts'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'nil'", "'next'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSIF", "ELSE", "END", "UNLESS", 
                      "DO", "WHILE", "BEGIN", "UNTIL", "FOR", "IN", "STRING", 
                      "CLASSNAME", "NEW", "CLASS", "DEF", "RETURN", "AND", 
                      "OR", "TRUE", "FALSE", "AT", "ATAT", "DOLLAR", "HASH", 
                      "APOSTROPHE", "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", 
                      "RIGTHBRACKET", "COMMA", "NEWLINE", "SEMICOLON", "PLUSEQUAL", 
                      "MINUSEQUAL", "MULEQUAL", "DIVIDEEQUAL", "MODEQUAL", 
                      "MULMULEQUAL", "PLUS", "MINUS", "MUL", "DIVIDE", "MOD", 
                      "MULMUL", "PLUSPLUS", "MINUSMINUS", "GREATER", "LESS", 
                      "LESSEQUAL", "MOREEQUAL", "LESSEQUALMORE", "EQUALEQUAL", 
                      "NOTEQUAL", "EQUALEQUALEQUAL", "EQUAL", "DOT", "PUTS", 
                      "ID", "NUMBER", "COMMENT", "WHITE_SPACE", "NIL", "NEXT" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_terminator = 2
    RULE_statement = 3
    RULE_functions = 4
    RULE_instructions = 5
    RULE_loop = 6
    RULE_bool = 7
    RULE_type = 8
    RULE_array = 9
    RULE_value = 10
    RULE_ifInstruction = 11
    RULE_elseInstruction = 12
    RULE_elsifInstruction = 13
    RULE_unlessInstruction = 14
    RULE_whileLoop = 15
    RULE_forLoop = 16
    RULE_untilLoop = 17
    RULE_comparisonOperator = 18
    RULE_operator = 19
    RULE_condition = 20
    RULE_variables = 21
    RULE_mathOperation = 22
    RULE_bracketExpression = 23
    RULE_function = 24
    RULE_parameters = 25
    RULE_class = 26
    RULE_classBody = 27
    RULE_functionCall = 28
    RULE_assignmentOperator = 29
    RULE_loopBody = 30
    RULE_assignment = 31
    RULE_classObject = 32
    RULE_methodCall = 33
    RULE_putsFunction = 34
    RULE_crlf = 35

    ruleNames =  [ "program", "statementList", "terminator", "statement", 
                   "functions", "instructions", "loop", "bool", "type", 
                   "array", "value", "ifInstruction", "elseInstruction", 
                   "elsifInstruction", "unlessInstruction", "whileLoop", 
                   "forLoop", "untilLoop", "comparisonOperator", "operator", 
                   "condition", "variables", "mathOperation", "bracketExpression", 
                   "function", "parameters", "class", "classBody", "functionCall", 
                   "assignmentOperator", "loopBody", "assignment", "classObject", 
                   "methodCall", "putsFunction", "crlf" ]

    EOF = Token.EOF
    IF=1
    ELSIF=2
    ELSE=3
    END=4
    UNLESS=5
    DO=6
    WHILE=7
    BEGIN=8
    UNTIL=9
    FOR=10
    IN=11
    STRING=12
    CLASSNAME=13
    NEW=14
    CLASS=15
    DEF=16
    RETURN=17
    AND=18
    OR=19
    TRUE=20
    FALSE=21
    AT=22
    ATAT=23
    DOLLAR=24
    HASH=25
    APOSTROPHE=26
    LEFTPAREN=27
    RIGHTPAREN=28
    LEFTBRACKET=29
    RIGTHBRACKET=30
    COMMA=31
    NEWLINE=32
    SEMICOLON=33
    PLUSEQUAL=34
    MINUSEQUAL=35
    MULEQUAL=36
    DIVIDEEQUAL=37
    MODEQUAL=38
    MULMULEQUAL=39
    PLUS=40
    MINUS=41
    MUL=42
    DIVIDE=43
    MOD=44
    MULMUL=45
    PLUSPLUS=46
    MINUSMINUS=47
    GREATER=48
    LESS=49
    LESSEQUAL=50
    MOREEQUAL=51
    LESSEQUALMORE=52
    EQUALEQUAL=53
    NOTEQUAL=54
    EQUALEQUALEQUAL=55
    EQUAL=56
    DOT=57
    PUTS=58
    ID=59
    NUMBER=60
    COMMENT=61
    WHITE_SPACE=62
    NIL=63
    NEXT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(RubyParser.StatementListContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RubyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.statementList(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(RubyParser.StatementContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def statementList(self):
            return self.getTypedRuleContext(RubyParser.StatementListContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)



    def statementList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.StatementListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_statementList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 7, 9, 10, 15, 16, 22, 23, 24, 58, 59, 61]:
                self.state = 75
                self.statement()
                self.state = 76
                self.terminator()
                pass
            elif token in [32, 33]:
                self.state = 78
                self.terminator()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.StatementListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statementList)
                    self.state = 81
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 82
                    self.statement()
                    self.state = 83
                    self.terminator() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(RubyParser.NEWLINE, 0)

        def SEMICOLON(self):
            return self.getToken(RubyParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_terminator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminator" ):
                listener.enterTerminator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminator" ):
                listener.exitTerminator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminator" ):
                return visitor.visitTerminator(self)
            else:
                return visitor.visitChildren(self)




    def terminator(self):

        localctx = RubyParser.TerminatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_terminator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functions(self):
            return self.getTypedRuleContext(RubyParser.FunctionsContext,0)


        def instructions(self):
            return self.getTypedRuleContext(RubyParser.InstructionsContext,0)


        def loop(self):
            return self.getTypedRuleContext(RubyParser.LoopContext,0)


        def variables(self):
            return self.getTypedRuleContext(RubyParser.VariablesContext,0)


        def assignment(self):
            return self.getTypedRuleContext(RubyParser.AssignmentContext,0)


        def classObject(self):
            return self.getTypedRuleContext(RubyParser.ClassObjectContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(RubyParser.MethodCallContext,0)


        def COMMENT(self):
            return self.getToken(RubyParser.COMMENT, 0)

        def putsFunction(self):
            return self.getTypedRuleContext(RubyParser.PutsFunctionContext,0)


        def class_(self):
            return self.getTypedRuleContext(RubyParser.ClassContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RubyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.functions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.instructions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.variables()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.classObject()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.methodCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.match(RubyParser.COMMENT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.putsFunction()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 101
                self.class_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(RubyParser.FunctionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RubyParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = RubyParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functions)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.function()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.functionCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifInstruction(self):
            return self.getTypedRuleContext(RubyParser.IfInstructionContext,0)


        def unlessInstruction(self):
            return self.getTypedRuleContext(RubyParser.UnlessInstructionContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructions" ):
                listener.enterInstructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructions" ):
                listener.exitInstructions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructions" ):
                return visitor.visitInstructions(self)
            else:
                return visitor.visitChildren(self)




    def instructions(self):

        localctx = RubyParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instructions)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.ifInstruction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.unlessInstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileLoop(self):
            return self.getTypedRuleContext(RubyParser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(RubyParser.ForLoopContext,0)


        def untilLoop(self):
            return self.getTypedRuleContext(RubyParser.UntilLoopContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = RubyParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.whileLoop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.forLoop()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.untilLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RubyParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RubyParser.FALSE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = RubyParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(RubyParser.AT, 0)

        def ATAT(self):
            return self.getToken(RubyParser.ATAT, 0)

        def DOLLAR(self):
            return self.getToken(RubyParser.DOLLAR, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = RubyParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTBRACKET(self):
            return self.getToken(RubyParser.LEFTBRACKET, 0)

        def RIGTHBRACKET(self):
            return self.getToken(RubyParser.RIGTHBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ValueContext)
            else:
                return self.getTypedRuleContext(RubyParser.ValueContext,i)


        def bool_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.BoolContext)
            else:
                return self.getTypedRuleContext(RubyParser.BoolContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.COMMA)
            else:
                return self.getToken(RubyParser.COMMA, i)

        def getRuleIndex(self):
            return RubyParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = RubyParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(RubyParser.LEFTBRACKET)
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 60]:
                self.state = 122
                self.value()
                pass
            elif token in [20, 21]:
                self.state = 123
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 126
                self.match(RubyParser.COMMA)
                self.state = 129
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 60]:
                    self.state = 127
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 128
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(RubyParser.RIGTHBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RubyParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(RubyParser.STRING, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = RubyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==12 or _la==60):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RubyParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(RubyParser.ConditionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def elsifInstruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ElsifInstructionContext)
            else:
                return self.getTypedRuleContext(RubyParser.ElsifInstructionContext,i)


        def elseInstruction(self):
            return self.getTypedRuleContext(RubyParser.ElseInstructionContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_ifInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfInstruction" ):
                listener.enterIfInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfInstruction" ):
                listener.exitIfInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInstruction" ):
                return visitor.visitIfInstruction(self)
            else:
                return visitor.visitChildren(self)




    def ifInstruction(self):

        localctx = RubyParser.IfInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(RubyParser.IF)
            self.state = 141
            self.condition()
            self.state = 142
            self.crlf()
            self.state = 143
            self.loopBody()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 144
                self.elsifInstruction()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 150
                self.elseInstruction()


            self.state = 153
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(RubyParser.ELSE, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def NEXT(self):
            return self.getToken(RubyParser.NEXT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_elseInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseInstruction" ):
                listener.enterElseInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseInstruction" ):
                listener.exitElseInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseInstruction" ):
                return visitor.visitElseInstruction(self)
            else:
                return visitor.visitChildren(self)




    def elseInstruction(self):

        localctx = RubyParser.ElseInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elseInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(RubyParser.ELSE)
            self.state = 156
            self.crlf()
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4, 5, 7, 9, 10, 15, 16, 22, 23, 24, 58, 59, 61]:
                self.state = 157
                self.loopBody()
                pass
            elif token in [64]:
                self.state = 158
                self.match(RubyParser.NEXT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsifInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSIF(self):
            return self.getToken(RubyParser.ELSIF, 0)

        def condition(self):
            return self.getTypedRuleContext(RubyParser.ConditionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_elsifInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsifInstruction" ):
                listener.enterElsifInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsifInstruction" ):
                listener.exitElsifInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsifInstruction" ):
                return visitor.visitElsifInstruction(self)
            else:
                return visitor.visitChildren(self)




    def elsifInstruction(self):

        localctx = RubyParser.ElsifInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elsifInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(RubyParser.ELSIF)
            self.state = 162
            self.condition()
            self.state = 163
            self.crlf()
            self.state = 164
            self.loopBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnlessInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNLESS(self):
            return self.getToken(RubyParser.UNLESS, 0)

        def condition(self):
            return self.getTypedRuleContext(RubyParser.ConditionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def elseInstruction(self):
            return self.getTypedRuleContext(RubyParser.ElseInstructionContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_unlessInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlessInstruction" ):
                listener.enterUnlessInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlessInstruction" ):
                listener.exitUnlessInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnlessInstruction" ):
                return visitor.visitUnlessInstruction(self)
            else:
                return visitor.visitChildren(self)




    def unlessInstruction(self):

        localctx = RubyParser.UnlessInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unlessInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(RubyParser.UNLESS)
            self.state = 167
            self.condition()
            self.state = 168
            self.crlf()
            self.state = 169
            self.loopBody()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 170
                self.elseInstruction()


            self.state = 173
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(RubyParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(RubyParser.ConditionContext,0)


        def DO(self):
            return self.getToken(RubyParser.DO, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = RubyParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(RubyParser.WHILE)
            self.state = 176
            self.condition()
            self.state = 177
            self.match(RubyParser.DO)
            self.state = 178
            self.crlf()
            self.state = 179
            self.loopBody()
            self.state = 180
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RubyParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def IN(self):
            return self.getToken(RubyParser.IN, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = RubyParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(RubyParser.FOR)
            self.state = 183
            self.match(RubyParser.ID)
            self.state = 184
            self.match(RubyParser.IN)
            self.state = 185
            self.match(RubyParser.ID)
            self.state = 186
            self.crlf()
            self.state = 187
            self.loopBody()
            self.state = 188
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UntilLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNTIL(self):
            return self.getToken(RubyParser.UNTIL, 0)

        def condition(self):
            return self.getTypedRuleContext(RubyParser.ConditionContext,0)


        def DO(self):
            return self.getToken(RubyParser.DO, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_untilLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntilLoop" ):
                listener.enterUntilLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntilLoop" ):
                listener.exitUntilLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntilLoop" ):
                return visitor.visitUntilLoop(self)
            else:
                return visitor.visitChildren(self)




    def untilLoop(self):

        localctx = RubyParser.UntilLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_untilLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(RubyParser.UNTIL)
            self.state = 191
            self.condition()
            self.state = 192
            self.match(RubyParser.DO)
            self.state = 193
            self.crlf()
            self.state = 194
            self.loopBody()
            self.state = 195
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(RubyParser.GREATER, 0)

        def LESS(self):
            return self.getToken(RubyParser.LESS, 0)

        def LESSEQUAL(self):
            return self.getToken(RubyParser.LESSEQUAL, 0)

        def MOREEQUAL(self):
            return self.getToken(RubyParser.MOREEQUAL, 0)

        def LESSEQUALMORE(self):
            return self.getToken(RubyParser.LESSEQUALMORE, 0)

        def EQUALEQUAL(self):
            return self.getToken(RubyParser.EQUALEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(RubyParser.NOTEQUAL, 0)

        def EQUALEQUALEQUAL(self):
            return self.getToken(RubyParser.EQUALEQUALEQUAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = RubyParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71776119061217280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(RubyParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def MULMUL(self):
            return self.getToken(RubyParser.MULMUL, 0)

        def PLUSPLUS(self):
            return self.getToken(RubyParser.PLUSPLUS, 0)

        def MINUSMINUS(self):
            return self.getToken(RubyParser.MINUSMINUS, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = RubyParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 280375465082880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def comparisonOperator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ComparisonOperatorContext)
            else:
                return self.getTypedRuleContext(RubyParser.ComparisonOperatorContext,i)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ValueContext)
            else:
                return self.getTypedRuleContext(RubyParser.ValueContext,i)


        def bool_(self):
            return self.getTypedRuleContext(RubyParser.BoolContext,0)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.AND)
            else:
                return self.getToken(RubyParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.OR)
            else:
                return self.getToken(RubyParser.OR, i)

        def getRuleIndex(self):
            return RubyParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = RubyParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 201
                self.match(RubyParser.ID)
                self.state = 202
                self.comparisonOperator()
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 60]:
                    self.state = 203
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 204
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 207
                self.value()
                self.state = 208
                self.comparisonOperator()
                self.state = 209
                self.value()
                pass

            elif la_ == 3:
                self.state = 211
                self.match(RubyParser.ID)
                self.state = 212
                self.comparisonOperator()
                self.state = 213
                self.match(RubyParser.ID)
                pass


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 218
                    self.match(RubyParser.ID)
                    self.state = 219
                    self.comparisonOperator()
                    self.state = 220
                    self.value()
                    pass

                elif la_ == 2:
                    self.state = 222
                    self.value()
                    self.state = 223
                    self.comparisonOperator()
                    self.state = 224
                    self.value()
                    pass

                elif la_ == 3:
                    self.state = 226
                    self.match(RubyParser.ID)
                    self.state = 227
                    self.comparisonOperator()
                    self.state = 228
                    self.match(RubyParser.ID)
                    pass


                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def EQUAL(self):
            return self.getToken(RubyParser.EQUAL, 0)

        def value(self):
            return self.getTypedRuleContext(RubyParser.ValueContext,0)


        def array(self):
            return self.getTypedRuleContext(RubyParser.ArrayContext,0)


        def mathOperation(self):
            return self.getTypedRuleContext(RubyParser.MathOperationContext,0)


        def bool_(self):
            return self.getTypedRuleContext(RubyParser.BoolContext,0)


        def type_(self):
            return self.getTypedRuleContext(RubyParser.TypeContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = RubyParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 237
                self.type_()


            self.state = 240
            self.match(RubyParser.ID)
            self.state = 241
            self.match(RubyParser.EQUAL)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 242
                self.value()
                pass

            elif la_ == 2:
                self.state = 243
                self.match(RubyParser.ID)
                pass

            elif la_ == 3:
                self.state = 244
                self.array()
                pass

            elif la_ == 4:
                self.state = 245
                self.mathOperation()
                pass

            elif la_ == 5:
                self.state = 246
                self.bool_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ValueContext)
            else:
                return self.getTypedRuleContext(RubyParser.ValueContext,i)


        def bracketExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.BracketExpressionContext)
            else:
                return self.getTypedRuleContext(RubyParser.BracketExpressionContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.OperatorContext)
            else:
                return self.getTypedRuleContext(RubyParser.OperatorContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_mathOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathOperation" ):
                listener.enterMathOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathOperation" ):
                listener.exitMathOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOperation" ):
                return visitor.visitMathOperation(self)
            else:
                return visitor.visitChildren(self)




    def mathOperation(self):

        localctx = RubyParser.MathOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mathOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.state = 249
                self.match(RubyParser.ID)
                pass
            elif token in [12, 60]:
                self.state = 250
                self.value()
                pass
            elif token in [27]:
                self.state = 251
                self.bracketExpression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 280375465082880) != 0):
                self.state = 254
                self.operator()
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 255
                    self.match(RubyParser.ID)
                    pass
                elif token in [12, 60]:
                    self.state = 256
                    self.value()
                    pass
                elif token in [27]:
                    self.state = 257
                    self.bracketExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTPAREN(self):
            return self.getToken(RubyParser.LEFTPAREN, 0)

        def mathOperation(self):
            return self.getTypedRuleContext(RubyParser.MathOperationContext,0)


        def RIGHTPAREN(self):
            return self.getToken(RubyParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_bracketExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketExpression" ):
                listener.enterBracketExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketExpression" ):
                listener.exitBracketExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketExpression" ):
                return visitor.visitBracketExpression(self)
            else:
                return visitor.visitChildren(self)




    def bracketExpression(self):

        localctx = RubyParser.BracketExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_bracketExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(RubyParser.LEFTPAREN)
            self.state = 266
            self.mathOperation()
            self.state = 267
            self.match(RubyParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(RubyParser.DEF, 0)

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def LEFTPAREN(self):
            return self.getToken(RubyParser.LEFTPAREN, 0)

        def RIGHTPAREN(self):
            return self.getToken(RubyParser.RIGHTPAREN, 0)

        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def loopBody(self):
            return self.getTypedRuleContext(RubyParser.LoopBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ParametersContext)
            else:
                return self.getTypedRuleContext(RubyParser.ParametersContext,i)


        def RETURN(self):
            return self.getToken(RubyParser.RETURN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = RubyParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(RubyParser.DEF)
            self.state = 270
            self.match(RubyParser.ID)
            self.state = 271
            self.match(RubyParser.LEFTPAREN)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382256913420288) != 0):
                self.state = 272
                self.parameters()


            self.state = 275
            self.match(RubyParser.RIGHTPAREN)
            self.state = 276
            self.crlf()
            self.state = 277
            self.loopBody()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 278
                self.match(RubyParser.RETURN)
                self.state = 279
                self.parameters()
                self.state = 280
                self.crlf()


            self.state = 284
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ValueContext)
            else:
                return self.getTypedRuleContext(RubyParser.ValueContext,i)


        def bool_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.BoolContext)
            else:
                return self.getTypedRuleContext(RubyParser.BoolContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.COMMA)
            else:
                return self.getToken(RubyParser.COMMA, i)

        def getRuleIndex(self):
            return RubyParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = RubyParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.state = 286
                self.match(RubyParser.ID)
                pass
            elif token in [12, 60]:
                self.state = 287
                self.value()
                pass
            elif token in [20, 21]:
                self.state = 288
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 291
                self.match(RubyParser.COMMA)
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 292
                    self.match(RubyParser.ID)
                    pass
                elif token in [12, 60]:
                    self.state = 293
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 294
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(RubyParser.CLASS, 0)

        def CLASSNAME(self):
            return self.getToken(RubyParser.CLASSNAME, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def classBody(self):
            return self.getTypedRuleContext(RubyParser.ClassBodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass" ):
                listener.enterClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass" ):
                listener.exitClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass" ):
                return visitor.visitClass(self)
            else:
                return visitor.visitChildren(self)




    def class_(self):

        localctx = RubyParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(RubyParser.CLASS)
            self.state = 303
            self.match(RubyParser.CLASSNAME)
            self.state = 304
            self.crlf()
            self.state = 305
            self.classBody()
            self.state = 306
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.VariablesContext)
            else:
                return self.getTypedRuleContext(RubyParser.VariablesContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.FunctionContext)
            else:
                return self.getTypedRuleContext(RubyParser.FunctionContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = RubyParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752332849152) != 0):
                self.state = 310
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22, 23, 24, 59]:
                    self.state = 308
                    self.variables()
                    pass
                elif token in [16]:
                    self.state = 309
                    self.function()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 312
                self.crlf()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def LEFTPAREN(self):
            return self.getToken(RubyParser.LEFTPAREN, 0)

        def RIGHTPAREN(self):
            return self.getToken(RubyParser.RIGHTPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(RubyParser.ParametersContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = RubyParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(RubyParser.ID)
            self.state = 320
            self.match(RubyParser.LEFTPAREN)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382256913420288) != 0):
                self.state = 321
                self.parameters()


            self.state = 324
            self.match(RubyParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUSEQUAL(self):
            return self.getToken(RubyParser.PLUSEQUAL, 0)

        def MINUSEQUAL(self):
            return self.getToken(RubyParser.MINUSEQUAL, 0)

        def MULEQUAL(self):
            return self.getToken(RubyParser.MULEQUAL, 0)

        def MULMULEQUAL(self):
            return self.getToken(RubyParser.MULMULEQUAL, 0)

        def DIVIDEEQUAL(self):
            return self.getToken(RubyParser.DIVIDEEQUAL, 0)

        def MODEQUAL(self):
            return self.getToken(RubyParser.MODEQUAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = RubyParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.StatementContext)
            else:
                return self.getTypedRuleContext(RubyParser.StatementContext,i)


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_loopBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopBody" ):
                listener.enterLoopBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopBody" ):
                listener.exitLoopBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopBody" ):
                return visitor.visitLoopBody(self)
            else:
                return visitor.visitChildren(self)




    def loopBody(self):

        localctx = RubyParser.LoopBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_loopBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3170534137698289314) != 0):
                self.state = 328
                self.statement()
                self.state = 329
                self.crlf()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ID)
            else:
                return self.getToken(RubyParser.ID, i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(RubyParser.AssignmentOperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(RubyParser.ValueContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = RubyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(RubyParser.ID)
            self.state = 337
            self.assignmentOperator()
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 60]:
                self.state = 338
                self.value()
                pass
            elif token in [59]:
                self.state = 339
                self.match(RubyParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def EQUAL(self):
            return self.getToken(RubyParser.EQUAL, 0)

        def CLASSNAME(self):
            return self.getToken(RubyParser.CLASSNAME, 0)

        def DOT(self):
            return self.getToken(RubyParser.DOT, 0)

        def NEW(self):
            return self.getToken(RubyParser.NEW, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_classObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassObject" ):
                listener.enterClassObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassObject" ):
                listener.exitClassObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassObject" ):
                return visitor.visitClassObject(self)
            else:
                return visitor.visitChildren(self)




    def classObject(self):

        localctx = RubyParser.ClassObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_classObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(RubyParser.ID)
            self.state = 343
            self.match(RubyParser.EQUAL)
            self.state = 344
            self.match(RubyParser.CLASSNAME)
            self.state = 345
            self.match(RubyParser.DOT)
            self.state = 346
            self.match(RubyParser.NEW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def DOT(self):
            return self.getToken(RubyParser.DOT, 0)

        def functionCall(self):
            return self.getTypedRuleContext(RubyParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = RubyParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(RubyParser.ID)
            self.state = 349
            self.match(RubyParser.DOT)
            self.state = 350
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PutsFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUTS(self):
            return self.getToken(RubyParser.PUTS, 0)

        def LEFTPAREN(self):
            return self.getToken(RubyParser.LEFTPAREN, 0)

        def RIGHTPAREN(self):
            return self.getToken(RubyParser.RIGHTPAREN, 0)

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(RubyParser.ValueContext,0)


        def array(self):
            return self.getTypedRuleContext(RubyParser.ArrayContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RubyParser.FunctionCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(RubyParser.MethodCallContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_putsFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPutsFunction" ):
                listener.enterPutsFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPutsFunction" ):
                listener.exitPutsFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutsFunction" ):
                return visitor.visitPutsFunction(self)
            else:
                return visitor.visitChildren(self)




    def putsFunction(self):

        localctx = RubyParser.PutsFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_putsFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(RubyParser.PUTS)
            self.state = 353
            self.match(RubyParser.LEFTPAREN)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 354
                self.match(RubyParser.ID)
                pass

            elif la_ == 2:
                self.state = 355
                self.value()
                pass

            elif la_ == 3:
                self.state = 356
                self.array()
                pass

            elif la_ == 4:
                self.state = 357
                self.functionCall()
                pass

            elif la_ == 5:
                self.state = 358
                self.methodCall()
                pass


            self.state = 361
            self.match(RubyParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CrlfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(RubyParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_crlf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrlf" ):
                listener.enterCrlf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrlf" ):
                listener.exitCrlf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrlf" ):
                return visitor.visitCrlf(self)
            else:
                return visitor.visitChildren(self)




    def crlf(self):

        localctx = RubyParser.CrlfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_crlf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(RubyParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.statementList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statementList_sempred(self, localctx:StatementListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




