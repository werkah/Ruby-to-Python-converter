grammar Ruby;

//rules

program: statementList;

statementList: terminator | statement terminator | statementList statement terminator;

terminator: NEWLINE | SEMICOLON;

statement: function | COMMENT | instructions | loop | variables | functionCall | assignment | class | classObject | methodCall;

instructions: ifInstruction | unlessInstruction;

loop: whileLoop | doWhileLoop | forLoop | untilLoop | doUntilLoop;

bool: TRUE | FALSE;

type: AT | ATAT | DOLLAR;

string: APOSTROPHE STRING APOSTROPHE;

comment: HASH COMMENT;

array: LEFTBRACKET (value | bool) (COMMA (value | bool))* RIGTHBRACKET;

value: NUMBER | STRING;

ifInstruction: IF condition loopBody (ELSIF condition loopBody)* (ELSE loopBody)? END;

unlessInstruction: UNLESS condition loopBody (ELSE loopBody)? END;

whileLoop: WHILE condition DO loopBody END;

doWhileLoop: BEGIN loopBody END WHILE condition;

forLoop: FOR ID IN (array | value) loopBody END;

untilLoop: BEGIN loopBody END UNTIL condition;

doUntilLoop: UNTIL condition DO loopBody END;

comparisonOperator: MOREE | LESS | LESSEQUAL | MOREEQUAL | LESSEQUALMORE | EQUALEQUAL | NOTEQUAL | EQUALEQUALEQUAL;

operator: PLUS | MINUS | MUL | DIVIDE | MOD | MULMUL | PLUSPLUS | MINUSMINUS;

condition: (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID) ((AND | OR) (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID))*;

variables: (type)? ID EQUAL (value | ID | mathOperation | array);

sign: PLUS | MINUS;

mathOperation: (sign)? (ID | value | bracketExpression) operator (ID | value | bracketExpression);

bracketExpression: LEFTPAREN mathOperation RIGHTPAREN;

function: DEF ID (parameters)? loopBody (RETURN (ID | value | array) (COMMA (ID | value | array))*)? END;

parameters: LEFTPAREN ID (COMMA ID)* RIGHTPAREN;

functionCall: ID (LEFTPAREN (ID | value | bool) (COMMA (ID | value | bool))* RIGHTPAREN)? ;

assignmentOperator: PLUSEQUAL | MINUSEQUAL | MULEQUAL | MULMULEQUAL | DIVIDEEQUAL | MODEQUAL;

loopBody: statement+;

assignment: ID assignmentOperator (value | ID | array);

class: CLASS ID (variables | function)* END;

classObject: ID EQUAL ID DOT NEW (LEFTPAREN (ID | value | bool) (COMMA (ID | value | bool))*) RIGHTPAREN);

methodCall: ID DOT functionCall;

putsFunction: PUTS LEFTPAREN (ID | value | array | functionCall | methodCall) RIGHTPAREN;



//keywords

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
DEF             : 'def';
RETURN          : 'return';
AND             : 'and';
OR              : 'or';
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
MODEQUAL       : '%=';
MULMULEQUAL     : '**=';
PLUS            : '+';
MINUS           : '-';
MUL             : '*';
DIVIDE          : '/';
MOD             : '%';
MULMUL          : '**';
PLUSPLUS        : '++';
MINUSMINUS      : '--';
MOREE            : '>';
LESS            : '<';
LESSEQUAL       : '<=';
MOREEQUAL       : '>=';
LESSEQUALMORE   : '<=>';
EQUALEQUAL      : '==';
NOTEQUAL        : '!=';
EQUALEQUALEQUAL : '===';
EQUAL           : '=';
DOT             : '.';
ID              : '[a-zA-Z_][a-zA-Z0-9_]*';
NUMBER          : '[0-9]+|([0-9]* DOT [0-9]+)';
STRING          : '[a-zA-Z0-9_]*';
COMMENT         : '[^\n]*';
PUTS            : 'puts';
NEW             : 'new';
CLASS           : 'class';

