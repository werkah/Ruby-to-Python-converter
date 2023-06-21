# Ruby to Python converter

## Authors
- Weronika Hilaszek
- Karolina Surówka

## Introduction
The Ruby to Python Converter is a program that aims to convert Ruby code to Python code. It provides a user-friendly GUI for easy file selection and conversion. The converter utilizes the PySimpleGUI library for creating the user interface and the ANTLR4 parser generator for parsing the Ruby code.
## Program overview

### Overall program goal
- The goal of the program is to convert Ruby code to equivalent Python code.

### Type of translator
- compiler

### Program output
- The program outputs Python code corresponding to the input Ruby code.

### Implementation language
- Python


### Libraries Used
 - PySimpleGUI - A Python GUI library used for creating a user interface for the converter
 - ANTLR4 - A parser generator used for parsing the Ruby code

## Tokens
The following tokens are recognized by the converter:
``` antlr
IF              : 'if';
ELSIF           : 'elsif';
ELSE            : 'else';
END             : 'end';
UNLESS          : 'unless';
DO              : 'do';
WHILE           : 'while';
BEGIN           : 'begin';
UNTIL           : 'until';
FOR             : 'for';
IN              : 'in';
STRING          : '"'[ \t\n\r\fa-zA-Z0-9=]*'"';
CLASSNAME       : [A-Z][a-zA-Z0-9_]*;
NEW             : 'new';
CLASS           : 'class';
DEF             : 'def';
RETURN          : 'return';
AND             : 'and';
OR              : 'or';
NIL             : 'nil';
TRUE            : 'true';
FALSE           : 'false';
HASH            : '#';
APOSTROPHE      : '\'';
LEFTPAREN       : '(';
RIGHTPAREN      : ')';
LEFTBRACKET     : '[';
RIGTHBRACKET    : ']';
COMMA           : ',';
NEWLINE         : '\r'? '\n';
SEMICOLON       : ';';
PLUSEQUAL       : '+=';
MINUSEQUAL      : '-=';
MULEQUAL        : '*=';
DIVIDEEQUAL     : '/=';
MODEQUAL        : '%=';
MULMULEQUAL     : '**=';
PLUS            : '+';
MINUS           : '-';
MUL             : '*';
DIVIDE          : '/';
MOD             : '%';
MULMUL          : '**';
PLUSPLUS        : '++';
MINUSMINUS      : '--';
GREATER         : '>';
LESS            : '<';
LESSEQUAL       : '<=';
MOREEQUAL       : '>=';
LESSEQUALMORE   : '<=>';
EQUALEQUAL      : '==';
NOTEQUAL        : '!=';
EQUALEQUALEQUAL : '===';
EQUAL           : '=';
DOT             : '.';
PUTS            : 'puts';
ID              : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER          : '-'?([0-9]+|([0-9]* DOT [0-9]+));
COMMENT         : '#'~[^\r\n]*;
WHITE_SPACE     : (' '|'\t')+ -> skip;
```

## Grammar
The grammar defines the structure of the Ruby code recognized by the converter. Here is the grammar used by the converter:
``` antlr
program: statementList;
statementList: statement terminator |statementList statement terminator | terminator;
terminator: NEWLINE | SEMICOLON;
statement: functions | instructions | loop | variables |  assignment  | classObject | methodCall | COMMENT | putsFunction | class;
functions: function | functionCall;
instructions: ifInstruction | unlessInstruction;
loop: whileLoop |  forLoop | untilLoop;
bool: TRUE | FALSE | NIL;
array: LEFTBRACKET (value | bool) (COMMA (value | bool))* RIGTHBRACKET;
value: NUMBER | STRING;
ifInstruction: IF condition terminator loopBody elsifInstruction* elseInstruction? END;
elseInstruction: ELSE terminator loopBody;
elsifInstruction: ELSIF condition terminator loopBody;
unlessInstruction: UNLESS condition terminator loopBody elseInstruction? END;
whileLoop: WHILE condition DO terminator loopBody END;
forLoop: FOR ID IN ID terminator loopBody END;
untilLoop: UNTIL condition DO terminator loopBody END;
comparisonOperator: GREATER | LESS | LESSEQUAL | MOREEQUAL | LESSEQUALMORE | EQUALEQUAL | NOTEQUAL | EQUALEQUALEQUAL;
operator: PLUS | MINUS | MUL | DIVIDE | MOD | MULMUL | PLUSPLUS | MINUSMINUS;
condition: (ID comparisonOperator (value|bool) | value comparisonOperator value | ID comparisonOperator ID) ((AND | OR) (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID))*;
variables: ID EQUAL (value | ID | array | mathOperation | bool);
mathOperation: (ID | value | bracketExpression) (operator (ID | value | bracketExpression))*;
bracketExpression: LEFTPAREN mathOperation RIGHTPAREN;
function: DEF ID LEFTPAREN parameters? RIGHTPAREN terminator loopBody (RETURN parameters terminator)? END;
parameters:(ID | value | bool)(COMMA (ID | value | bool))*;
class: CLASS CLASSNAME terminator classBody END;
classBody: ((variables | function) terminator)*;
functionCall: ID LEFTPAREN parameters? RIGHTPAREN;
assignmentOperator: PLUSEQUAL | MINUSEQUAL | MULEQUAL | MULMULEQUAL | DIVIDEEQUAL | MODEQUAL;
loopBody: (statement terminator)*;
assignment: ID assignmentOperator (value | ID);
classObject: ID EQUAL CLASSNAME DOT NEW;
methodCall: ID DOT functionCall;
putsFunction: PUTS LEFTPAREN (ID | value | array | functionCall | methodCall) RIGHTPAREN;
```

## Quick start guide
- clone the repository or download the source code
- install the required dependencies by running the following commands:
``` shell
pip install PySimpleGUI
pip install antlr4-python3-runtime
```
- place your Ruby code file in the `examples` folder
- run the program by executing the following command:
``` shell
python3 main.py
```
- after running the program, a window will appear with options to select a file for conversion and enter an output file name
- select the desired Ruby code file and enter the output file name
- click the `Convert` button
- if the conversion is successful, the converted code will be displayed in the window, and the output file will be saved in the main folder
- in case of errors in the Ruby code, an error message will be displayed in the window, and the output file will not be created

## Example of use
- Ruby code:
``` ruby
def test(a1, a2, a3)
    puts(a3)
    if a1 > a2
        puts("a1 is bigger than a2");puts("a1 is bigger than a3")
    else
        puts("a1 is smaller than a2")
    end
    arrr = [1,5,7,8]
    for i in arrr
        if i > a1
            puts(i)
        end
    end
end
test(2,3, "ala");
```
- Output window:
  
<img width="350" alt="image" src="https://github.com/werkah/Ruby-to-Python-converter/assets/92488733/f490212c-45c0-48e6-ac97-e30873365e93">



