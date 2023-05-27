grammar Ruby;

//rules

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

ifInstruction: IF condition crlf loopBody elsifInstruction* elseInstruction? END;

elseInstruction: ELSE crlf (loopBody|NEXT);

elsifInstruction: ELSIF condition crlf loopBody;

unlessInstruction: UNLESS condition crlf loopBody elseInstruction? END;

whileLoop: WHILE condition DO crlf loopBody END;

forLoop: FOR ID IN ID crlf loopBody END;

untilLoop: UNTIL condition DO crlf loopBody END;

comparisonOperator: GREATER | LESS | LESSEQUAL | MOREEQUAL | LESSEQUALMORE | EQUALEQUAL | NOTEQUAL | EQUALEQUALEQUAL;

operator: PLUS | MINUS | MUL | DIVIDE | MOD | MULMUL | PLUSPLUS | MINUSMINUS;

condition: (ID comparisonOperator (value|bool) | value comparisonOperator value | ID comparisonOperator ID) ((AND | OR) (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID))*;

variables: ID EQUAL (value | ID | array | mathOperation|bool);

mathOperation: (ID | value | bracketExpression) (operator (ID | value | bracketExpression))*;

bracketExpression: LEFTPAREN mathOperation RIGHTPAREN;

function: DEF ID LEFTPAREN parameters? RIGHTPAREN crlf loopBody (RETURN parameters crlf)? END;

parameters:(ID | value | bool)(COMMA (ID | value | bool))*;

class: CLASS CLASSNAME crlf classBody END;

classBody: ((variables | function) crlf)*;

functionCall: ID LEFTPAREN parameters? RIGHTPAREN;

assignmentOperator: PLUSEQUAL | MINUSEQUAL | MULEQUAL | MULMULEQUAL | DIVIDEEQUAL | MODEQUAL;

loopBody: (statement crlf)*;

assignment: ID assignmentOperator (value | ID);

classObject: ID EQUAL CLASSNAME DOT NEW;

methodCall: ID DOT functionCall;

putsFunction: PUTS LEFTPAREN (ID | value | array | functionCall | methodCall) RIGHTPAREN;

crlf: NEWLINE;

//tokens

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

AT              : '@';
ATAT            : '@@';
DOLLAR          : '$';
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
NEXT            : 'next';