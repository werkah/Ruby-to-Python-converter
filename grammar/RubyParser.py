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
        4,1,64,365,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,1,1,1,1,1,1,1,5,1,
        82,8,1,10,1,12,1,85,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,99,8,3,1,4,1,4,3,4,103,8,4,1,5,1,5,3,5,107,8,5,1,6,1,
        6,1,6,3,6,112,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,3,9,121,8,9,1,9,1,
        9,1,9,3,9,126,8,9,5,9,128,8,9,10,9,12,9,131,9,9,1,9,1,9,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,146,8,11,10,11,
        12,11,149,9,11,1,11,1,11,1,11,1,11,3,11,155,8,11,3,11,157,8,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,169,8,12,3,
        12,171,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,3,18,205,8,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,215,8,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,230,8,18,5,
        18,232,8,18,10,18,12,18,235,9,18,1,19,3,19,238,8,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,3,19,247,8,19,1,20,1,20,1,20,3,20,252,8,20,
        1,20,1,20,1,20,1,20,3,20,258,8,20,5,20,260,8,20,10,20,12,20,263,
        9,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,273,8,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,3,22,282,8,22,1,22,1,22,1,23,1,23,
        1,23,3,23,289,8,23,1,23,1,23,1,23,1,23,3,23,295,8,23,5,23,297,8,
        23,10,23,12,23,300,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,
        3,25,310,8,25,1,25,1,25,5,25,314,8,25,10,25,12,25,317,9,25,1,26,
        1,26,1,26,3,26,322,8,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,5,28,
        331,8,28,10,28,12,28,334,9,28,1,29,1,29,1,29,1,29,3,29,340,8,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,3,32,359,8,32,1,32,1,32,1,33,1,33,1,33,0,1,2,
        34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,0,8,1,0,32,33,1,0,20,21,1,0,
        22,24,2,0,12,12,60,60,1,0,48,55,1,0,40,47,1,0,18,19,1,0,34,39,385,
        0,68,1,0,0,0,2,75,1,0,0,0,4,86,1,0,0,0,6,98,1,0,0,0,8,102,1,0,0,
        0,10,106,1,0,0,0,12,111,1,0,0,0,14,113,1,0,0,0,16,115,1,0,0,0,18,
        117,1,0,0,0,20,134,1,0,0,0,22,136,1,0,0,0,24,160,1,0,0,0,26,174,
        1,0,0,0,28,181,1,0,0,0,30,189,1,0,0,0,32,196,1,0,0,0,34,198,1,0,
        0,0,36,214,1,0,0,0,38,237,1,0,0,0,40,251,1,0,0,0,42,264,1,0,0,0,
        44,268,1,0,0,0,46,288,1,0,0,0,48,301,1,0,0,0,50,315,1,0,0,0,52,318,
        1,0,0,0,54,325,1,0,0,0,56,332,1,0,0,0,58,335,1,0,0,0,60,341,1,0,
        0,0,62,347,1,0,0,0,64,351,1,0,0,0,66,362,1,0,0,0,68,69,3,2,1,0,69,
        1,1,0,0,0,70,71,6,1,-1,0,71,72,3,6,3,0,72,73,3,4,2,0,73,76,1,0,0,
        0,74,76,3,4,2,0,75,70,1,0,0,0,75,74,1,0,0,0,76,83,1,0,0,0,77,78,
        10,2,0,0,78,79,3,6,3,0,79,80,3,4,2,0,80,82,1,0,0,0,81,77,1,0,0,0,
        82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,3,1,0,0,0,85,83,1,0,
        0,0,86,87,7,0,0,0,87,5,1,0,0,0,88,99,3,8,4,0,89,99,3,10,5,0,90,99,
        3,12,6,0,91,99,3,38,19,0,92,99,3,58,29,0,93,99,3,60,30,0,94,99,3,
        62,31,0,95,99,5,61,0,0,96,99,3,64,32,0,97,99,3,48,24,0,98,88,1,0,
        0,0,98,89,1,0,0,0,98,90,1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,93,
        1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,
        99,7,1,0,0,0,100,103,3,44,22,0,101,103,3,52,26,0,102,100,1,0,0,0,
        102,101,1,0,0,0,103,9,1,0,0,0,104,107,3,22,11,0,105,107,3,24,12,
        0,106,104,1,0,0,0,106,105,1,0,0,0,107,11,1,0,0,0,108,112,3,26,13,
        0,109,112,3,28,14,0,110,112,3,30,15,0,111,108,1,0,0,0,111,109,1,
        0,0,0,111,110,1,0,0,0,112,13,1,0,0,0,113,114,7,1,0,0,114,15,1,0,
        0,0,115,116,7,2,0,0,116,17,1,0,0,0,117,120,5,29,0,0,118,121,3,20,
        10,0,119,121,3,14,7,0,120,118,1,0,0,0,120,119,1,0,0,0,121,129,1,
        0,0,0,122,125,5,31,0,0,123,126,3,20,10,0,124,126,3,14,7,0,125,123,
        1,0,0,0,125,124,1,0,0,0,126,128,1,0,0,0,127,122,1,0,0,0,128,131,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,
        1,0,0,0,132,133,5,30,0,0,133,19,1,0,0,0,134,135,7,3,0,0,135,21,1,
        0,0,0,136,137,5,1,0,0,137,138,3,36,18,0,138,139,3,66,33,0,139,147,
        3,56,28,0,140,141,5,2,0,0,141,142,3,36,18,0,142,143,3,66,33,0,143,
        144,3,56,28,0,144,146,1,0,0,0,145,140,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,156,1,0,0,0,149,147,1,0,0,0,150,
        151,5,3,0,0,151,154,3,66,33,0,152,155,3,56,28,0,153,155,5,64,0,0,
        154,152,1,0,0,0,154,153,1,0,0,0,155,157,1,0,0,0,156,150,1,0,0,0,
        156,157,1,0,0,0,157,158,1,0,0,0,158,159,5,4,0,0,159,23,1,0,0,0,160,
        161,5,5,0,0,161,162,3,36,18,0,162,163,3,66,33,0,163,170,3,56,28,
        0,164,165,5,3,0,0,165,168,3,66,33,0,166,169,3,56,28,0,167,169,5,
        64,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,171,1,0,0,0,170,164,1,
        0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,4,0,0,173,25,1,0,
        0,0,174,175,5,7,0,0,175,176,3,36,18,0,176,177,5,6,0,0,177,178,3,
        66,33,0,178,179,3,56,28,0,179,180,5,4,0,0,180,27,1,0,0,0,181,182,
        5,10,0,0,182,183,5,59,0,0,183,184,5,11,0,0,184,185,5,59,0,0,185,
        186,3,66,33,0,186,187,3,56,28,0,187,188,5,4,0,0,188,29,1,0,0,0,189,
        190,5,9,0,0,190,191,3,36,18,0,191,192,5,6,0,0,192,193,3,66,33,0,
        193,194,3,56,28,0,194,195,5,4,0,0,195,31,1,0,0,0,196,197,7,4,0,0,
        197,33,1,0,0,0,198,199,7,5,0,0,199,35,1,0,0,0,200,201,5,59,0,0,201,
        204,3,32,16,0,202,205,3,20,10,0,203,205,3,14,7,0,204,202,1,0,0,0,
        204,203,1,0,0,0,205,215,1,0,0,0,206,207,3,20,10,0,207,208,3,32,16,
        0,208,209,3,20,10,0,209,215,1,0,0,0,210,211,5,59,0,0,211,212,3,32,
        16,0,212,213,5,59,0,0,213,215,1,0,0,0,214,200,1,0,0,0,214,206,1,
        0,0,0,214,210,1,0,0,0,215,233,1,0,0,0,216,229,7,6,0,0,217,218,5,
        59,0,0,218,219,3,32,16,0,219,220,3,20,10,0,220,230,1,0,0,0,221,222,
        3,20,10,0,222,223,3,32,16,0,223,224,3,20,10,0,224,230,1,0,0,0,225,
        226,5,59,0,0,226,227,3,32,16,0,227,228,5,59,0,0,228,230,1,0,0,0,
        229,217,1,0,0,0,229,221,1,0,0,0,229,225,1,0,0,0,230,232,1,0,0,0,
        231,216,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,
        234,37,1,0,0,0,235,233,1,0,0,0,236,238,3,16,8,0,237,236,1,0,0,0,
        237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,59,0,0,240,246,5,56,0,
        0,241,247,3,20,10,0,242,247,5,59,0,0,243,247,3,18,9,0,244,247,3,
        40,20,0,245,247,3,14,7,0,246,241,1,0,0,0,246,242,1,0,0,0,246,243,
        1,0,0,0,246,244,1,0,0,0,246,245,1,0,0,0,247,39,1,0,0,0,248,252,5,
        59,0,0,249,252,3,20,10,0,250,252,3,42,21,0,251,248,1,0,0,0,251,249,
        1,0,0,0,251,250,1,0,0,0,252,261,1,0,0,0,253,257,3,34,17,0,254,258,
        5,59,0,0,255,258,3,20,10,0,256,258,3,42,21,0,257,254,1,0,0,0,257,
        255,1,0,0,0,257,256,1,0,0,0,258,260,1,0,0,0,259,253,1,0,0,0,260,
        263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,41,1,0,0,0,263,261,
        1,0,0,0,264,265,5,27,0,0,265,266,3,40,20,0,266,267,5,28,0,0,267,
        43,1,0,0,0,268,269,5,16,0,0,269,270,5,59,0,0,270,272,5,27,0,0,271,
        273,3,46,23,0,272,271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,
        275,5,28,0,0,275,276,3,66,33,0,276,281,3,56,28,0,277,278,5,17,0,
        0,278,279,3,46,23,0,279,280,3,66,33,0,280,282,1,0,0,0,281,277,1,
        0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,284,5,4,0,0,284,45,1,0,
        0,0,285,289,5,59,0,0,286,289,3,20,10,0,287,289,3,14,7,0,288,285,
        1,0,0,0,288,286,1,0,0,0,288,287,1,0,0,0,289,298,1,0,0,0,290,294,
        5,31,0,0,291,295,5,59,0,0,292,295,3,20,10,0,293,295,3,14,7,0,294,
        291,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,297,1,0,0,0,296,
        290,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,
        47,1,0,0,0,300,298,1,0,0,0,301,302,5,15,0,0,302,303,5,13,0,0,303,
        304,3,66,33,0,304,305,3,50,25,0,305,306,5,4,0,0,306,49,1,0,0,0,307,
        310,3,38,19,0,308,310,3,44,22,0,309,307,1,0,0,0,309,308,1,0,0,0,
        310,311,1,0,0,0,311,312,3,66,33,0,312,314,1,0,0,0,313,309,1,0,0,
        0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,51,1,0,0,0,
        317,315,1,0,0,0,318,319,5,59,0,0,319,321,5,27,0,0,320,322,3,46,23,
        0,321,320,1,0,0,0,321,322,1,0,0,0,322,323,1,0,0,0,323,324,5,28,0,
        0,324,53,1,0,0,0,325,326,7,7,0,0,326,55,1,0,0,0,327,328,3,6,3,0,
        328,329,3,66,33,0,329,331,1,0,0,0,330,327,1,0,0,0,331,334,1,0,0,
        0,332,330,1,0,0,0,332,333,1,0,0,0,333,57,1,0,0,0,334,332,1,0,0,0,
        335,336,5,59,0,0,336,339,3,54,27,0,337,340,3,20,10,0,338,340,5,59,
        0,0,339,337,1,0,0,0,339,338,1,0,0,0,340,59,1,0,0,0,341,342,5,59,
        0,0,342,343,5,56,0,0,343,344,5,13,0,0,344,345,5,57,0,0,345,346,5,
        14,0,0,346,61,1,0,0,0,347,348,5,59,0,0,348,349,5,57,0,0,349,350,
        3,52,26,0,350,63,1,0,0,0,351,352,5,58,0,0,352,358,5,27,0,0,353,359,
        5,59,0,0,354,359,3,20,10,0,355,359,3,18,9,0,356,359,3,52,26,0,357,
        359,3,62,31,0,358,353,1,0,0,0,358,354,1,0,0,0,358,355,1,0,0,0,358,
        356,1,0,0,0,358,357,1,0,0,0,359,360,1,0,0,0,360,361,5,28,0,0,361,
        65,1,0,0,0,362,363,5,32,0,0,363,67,1,0,0,0,34,75,83,98,102,106,111,
        120,125,129,147,154,156,168,170,204,214,229,233,237,246,251,257,
        261,272,281,288,294,298,309,315,321,332,339,358
    ]

class RubyParser ( Parser ):

    grammarFileName = "Ruby.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elsif'", "'else'", "'end'", 
                     "'unless'", "'do'", "'while'", "'begin'", "'until'", 
                     "'for'", "'in'", "<INVALID>", "<INVALID>", "'new'", 
                     "'class'", "'def'", "'return'", "'and'", "'or'", "'true'", 
                     "'false'", "'@'", "'@@'", "'$'", "'#'", "'''", "'('", 
                     "')'", "'['", "']'", "','", "<INVALID>", "';'", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'**='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'**'", "'++'", "'--'", "'>'", 
                     "'<'", "'<='", "'>='", "'<=>'", "'=='", "'!='", "'==='", 
                     "'='", "'.'", "'puts'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'", "'next'" ]

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
    RULE_unlessInstruction = 12
    RULE_whileLoop = 13
    RULE_forLoop = 14
    RULE_untilLoop = 15
    RULE_comparisonOperator = 16
    RULE_operator = 17
    RULE_condition = 18
    RULE_variables = 19
    RULE_mathOperation = 20
    RULE_bracketExpression = 21
    RULE_function = 22
    RULE_parameters = 23
    RULE_class = 24
    RULE_classBody = 25
    RULE_functionCall = 26
    RULE_assignmentOperator = 27
    RULE_loopBody = 28
    RULE_assignment = 29
    RULE_classObject = 30
    RULE_methodCall = 31
    RULE_putsFunction = 32
    RULE_crlf = 33

    ruleNames =  [ "program", "statementList", "terminator", "statement", 
                   "functions", "instructions", "loop", "bool", "type", 
                   "array", "value", "ifInstruction", "unlessInstruction", 
                   "whileLoop", "forLoop", "untilLoop", "comparisonOperator", 
                   "operator", "condition", "variables", "mathOperation", 
                   "bracketExpression", "function", "parameters", "class", 
                   "classBody", "functionCall", "assignmentOperator", "loopBody", 
                   "assignment", "classObject", "methodCall", "putsFunction", 
                   "crlf" ]

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
            self.state = 68
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 7, 9, 10, 15, 16, 22, 23, 24, 58, 59, 61]:
                self.state = 71
                self.statement()
                self.state = 72
                self.terminator()
                pass
            elif token in [32, 33]:
                self.state = 74
                self.terminator()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.StatementListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statementList)
                    self.state = 77
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 78
                    self.statement()
                    self.state = 79
                    self.terminator() 
                self.state = 85
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
            self.state = 86
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.functions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.instructions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.variables()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.classObject()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.methodCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.match(RubyParser.COMMENT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.putsFunction()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 97
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.function()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
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
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.ifInstruction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
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
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.whileLoop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.forLoop()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
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
            self.state = 113
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
            self.state = 115
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
            self.state = 117
            self.match(RubyParser.LEFTBRACKET)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 60]:
                self.state = 118
                self.value()
                pass
            elif token in [20, 21]:
                self.state = 119
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 122
                self.match(RubyParser.COMMA)
                self.state = 125
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 60]:
                    self.state = 123
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 124
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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
            self.state = 134
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

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ConditionContext)
            else:
                return self.getTypedRuleContext(RubyParser.ConditionContext,i)


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def loopBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.LoopBodyContext)
            else:
                return self.getTypedRuleContext(RubyParser.LoopBodyContext,i)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def ELSIF(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.ELSIF)
            else:
                return self.getToken(RubyParser.ELSIF, i)

        def ELSE(self):
            return self.getToken(RubyParser.ELSE, 0)

        def NEXT(self):
            return self.getToken(RubyParser.NEXT, 0)

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
            self.state = 136
            self.match(RubyParser.IF)
            self.state = 137
            self.condition()
            self.state = 138
            self.crlf()
            self.state = 139
            self.loopBody()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 140
                self.match(RubyParser.ELSIF)
                self.state = 141
                self.condition()
                self.state = 142
                self.crlf()
                self.state = 143
                self.loopBody()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 150
                self.match(RubyParser.ELSE)
                self.state = 151
                self.crlf()
                self.state = 154
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 5, 7, 9, 10, 15, 16, 22, 23, 24, 58, 59, 61]:
                    self.state = 152
                    self.loopBody()
                    pass
                elif token in [64]:
                    self.state = 153
                    self.match(RubyParser.NEXT)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 158
            self.match(RubyParser.END)
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


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def loopBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.LoopBodyContext)
            else:
                return self.getTypedRuleContext(RubyParser.LoopBodyContext,i)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def ELSE(self):
            return self.getToken(RubyParser.ELSE, 0)

        def NEXT(self):
            return self.getToken(RubyParser.NEXT, 0)

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
        self.enterRule(localctx, 24, self.RULE_unlessInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(RubyParser.UNLESS)
            self.state = 161
            self.condition()
            self.state = 162
            self.crlf()
            self.state = 163
            self.loopBody()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 164
                self.match(RubyParser.ELSE)
                self.state = 165
                self.crlf()
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 5, 7, 9, 10, 15, 16, 22, 23, 24, 58, 59, 61]:
                    self.state = 166
                    self.loopBody()
                    pass
                elif token in [64]:
                    self.state = 167
                    self.match(RubyParser.NEXT)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 172
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
        self.enterRule(localctx, 26, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(RubyParser.WHILE)
            self.state = 175
            self.condition()
            self.state = 176
            self.match(RubyParser.DO)
            self.state = 177
            self.crlf()
            self.state = 178
            self.loopBody()
            self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(RubyParser.FOR)
            self.state = 182
            self.match(RubyParser.ID)
            self.state = 183
            self.match(RubyParser.IN)
            self.state = 184
            self.match(RubyParser.ID)
            self.state = 185
            self.crlf()
            self.state = 186
            self.loopBody()
            self.state = 187
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
        self.enterRule(localctx, 30, self.RULE_untilLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(RubyParser.UNTIL)
            self.state = 190
            self.condition()
            self.state = 191
            self.match(RubyParser.DO)
            self.state = 192
            self.crlf()
            self.state = 193
            self.loopBody()
            self.state = 194
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
        self.enterRule(localctx, 32, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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
        self.enterRule(localctx, 34, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 36, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 200
                self.match(RubyParser.ID)
                self.state = 201
                self.comparisonOperator()
                self.state = 204
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 60]:
                    self.state = 202
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 203
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 206
                self.value()
                self.state = 207
                self.comparisonOperator()
                self.state = 208
                self.value()
                pass

            elif la_ == 3:
                self.state = 210
                self.match(RubyParser.ID)
                self.state = 211
                self.comparisonOperator()
                self.state = 212
                self.match(RubyParser.ID)
                pass


            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 216
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 217
                    self.match(RubyParser.ID)
                    self.state = 218
                    self.comparisonOperator()
                    self.state = 219
                    self.value()
                    pass

                elif la_ == 2:
                    self.state = 221
                    self.value()
                    self.state = 222
                    self.comparisonOperator()
                    self.state = 223
                    self.value()
                    pass

                elif la_ == 3:
                    self.state = 225
                    self.match(RubyParser.ID)
                    self.state = 226
                    self.comparisonOperator()
                    self.state = 227
                    self.match(RubyParser.ID)
                    pass


                self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 236
                self.type_()


            self.state = 239
            self.match(RubyParser.ID)
            self.state = 240
            self.match(RubyParser.EQUAL)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 241
                self.value()
                pass

            elif la_ == 2:
                self.state = 242
                self.match(RubyParser.ID)
                pass

            elif la_ == 3:
                self.state = 243
                self.array()
                pass

            elif la_ == 4:
                self.state = 244
                self.mathOperation()
                pass

            elif la_ == 5:
                self.state = 245
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
        self.enterRule(localctx, 40, self.RULE_mathOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.state = 248
                self.match(RubyParser.ID)
                pass
            elif token in [12, 60]:
                self.state = 249
                self.value()
                pass
            elif token in [27]:
                self.state = 250
                self.bracketExpression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 280375465082880) != 0):
                self.state = 253
                self.operator()
                self.state = 257
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 254
                    self.match(RubyParser.ID)
                    pass
                elif token in [12, 60]:
                    self.state = 255
                    self.value()
                    pass
                elif token in [27]:
                    self.state = 256
                    self.bracketExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 263
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
        self.enterRule(localctx, 42, self.RULE_bracketExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(RubyParser.LEFTPAREN)
            self.state = 265
            self.mathOperation()
            self.state = 266
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
        self.enterRule(localctx, 44, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RubyParser.DEF)
            self.state = 269
            self.match(RubyParser.ID)
            self.state = 270
            self.match(RubyParser.LEFTPAREN)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382256913420288) != 0):
                self.state = 271
                self.parameters()


            self.state = 274
            self.match(RubyParser.RIGHTPAREN)
            self.state = 275
            self.crlf()
            self.state = 276
            self.loopBody()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 277
                self.match(RubyParser.RETURN)
                self.state = 278
                self.parameters()
                self.state = 279
                self.crlf()


            self.state = 283
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
        self.enterRule(localctx, 46, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.state = 285
                self.match(RubyParser.ID)
                pass
            elif token in [12, 60]:
                self.state = 286
                self.value()
                pass
            elif token in [20, 21]:
                self.state = 287
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 290
                self.match(RubyParser.COMMA)
                self.state = 294
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 291
                    self.match(RubyParser.ID)
                    pass
                elif token in [12, 60]:
                    self.state = 292
                    self.value()
                    pass
                elif token in [20, 21]:
                    self.state = 293
                    self.bool_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 300
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
        self.enterRule(localctx, 48, self.RULE_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(RubyParser.CLASS)
            self.state = 302
            self.match(RubyParser.CLASSNAME)
            self.state = 303
            self.crlf()
            self.state = 304
            self.classBody()
            self.state = 305
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
        self.enterRule(localctx, 50, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752332849152) != 0):
                self.state = 309
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22, 23, 24, 59]:
                    self.state = 307
                    self.variables()
                    pass
                elif token in [16]:
                    self.state = 308
                    self.function()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 311
                self.crlf()
                self.state = 317
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
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(RubyParser.ID)
            self.state = 319
            self.match(RubyParser.LEFTPAREN)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382256913420288) != 0):
                self.state = 320
                self.parameters()


            self.state = 323
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
        self.enterRule(localctx, 54, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 56, self.RULE_loopBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3170534137698289314) != 0):
                self.state = 327
                self.statement()
                self.state = 328
                self.crlf()
                self.state = 334
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
        self.enterRule(localctx, 58, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(RubyParser.ID)
            self.state = 336
            self.assignmentOperator()
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 60]:
                self.state = 337
                self.value()
                pass
            elif token in [59]:
                self.state = 338
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
        self.enterRule(localctx, 60, self.RULE_classObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(RubyParser.ID)
            self.state = 342
            self.match(RubyParser.EQUAL)
            self.state = 343
            self.match(RubyParser.CLASSNAME)
            self.state = 344
            self.match(RubyParser.DOT)
            self.state = 345
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
        self.enterRule(localctx, 62, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(RubyParser.ID)
            self.state = 348
            self.match(RubyParser.DOT)
            self.state = 349
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
        self.enterRule(localctx, 64, self.RULE_putsFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(RubyParser.PUTS)
            self.state = 352
            self.match(RubyParser.LEFTPAREN)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 353
                self.match(RubyParser.ID)
                pass

            elif la_ == 2:
                self.state = 354
                self.value()
                pass

            elif la_ == 3:
                self.state = 355
                self.array()
                pass

            elif la_ == 4:
                self.state = 356
                self.functionCall()
                pass

            elif la_ == 5:
                self.state = 357
                self.methodCall()
                pass


            self.state = 360
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
        self.enterRule(localctx, 66, self.RULE_crlf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
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
         




