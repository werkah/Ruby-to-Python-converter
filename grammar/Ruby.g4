grammar Ruby;

//rules

program: statementList;

statementList: statement terminator |statementList statement terminator | terminator ; //czy do term crlf? np pusty program bez nowej linii

terminator: NEWLINE | SEMICOLON;

statement: functions | instructions | loop | variables |  assignment  | classObject | methodCall | COMMENT;

functions: function | functionCall;

instructions: ifInstruction | unlessInstruction;

loop: whileLoop |  forLoop | untilLoop;

bool: TRUE | FALSE;

type: AT | ATAT | DOLLAR;

//comment: HASH COMMENT;

array: LEFTBRACKET (value | bool) (COMMA (value | bool))* RIGTHBRACKET;

value: NUMBER | STRING;

ifInstruction: IF condition crlf loopBody (ELSIF condition crlf loopBody)* (ELSE crlf (loopBody | NEXT))? END;

unlessInstruction: UNLESS condition loopBody (ELSE (loopBody|NEXT))? END;

whileLoop: WHILE condition DO crlf loopBody END;

forLoop: FOR ID IN ID crlf loopBody END;

untilLoop: UNTIL condition DO loopBody END;

comparisonOperator: GREATER | LESS | LESSEQUAL | MOREEQUAL | LESSEQUALMORE | EQUALEQUAL | NOTEQUAL | EQUALEQUALEQUAL;

operator: PLUS | MINUS | MUL | DIVIDE | MOD | MULMUL | PLUSPLUS | MINUSMINUS;

condition: (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID) ((AND | OR) (ID comparisonOperator value | value comparisonOperator value | ID comparisonOperator ID))*;

variables: (type)? ID EQUAL (value | ID | array | mathOperation);

sign: PLUS | MINUS;

mathOperation: (sign)? (ID | value | bracketExpression) (operator (ID | value | bracketExpression))*;

bracketExpression: LEFTPAREN mathOperation RIGHTPAREN;

function: DEF ID (parameters)? crlf loopBody (RETURN (ID | value | array) (COMMA (ID | value | array))*)? END;

parameters: LEFTPAREN ID (COMMA ID)* RIGHTPAREN;

class: CLASS ID crlf (variables | function)* crlf END;

functionCall: ID LEFTPAREN ((ID | value | bool) (COMMA (ID | value | bool))*) RIGHTPAREN;  //// jak poprawnie zapisac

assignmentOperator: PLUSEQUAL | MINUSEQUAL | MULEQUAL | MULMULEQUAL | DIVIDEEQUAL | MODEQUAL;

loopBody: statement terminator;

assignment: ID assignmentOperator (value | ID);

classObject: ID EQUAL ID DOT NEW;

methodCall: ID DOT functionCall; //?

//putsFunction: PUTS LEFTPAREN (ID | value | array | functionCall | methodCall) RIGHTPAREN; //?

crlf: NEWLINE;







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
//CLASSNAME       : [A-Z][a-zA-Z0-9_]*;
NEW             : 'new';
CLASS           : 'class';
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
ID              : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER          : [0-9]+|([0-9]* DOT [0-9]+);
STRING          : '"'[a-zA-Z0-9_]*'"';
COMMENT         : '#' ~[^\r\n]*; //SKIP?
PUTS            : 'puts';
WHITE_SPACE : (' '|'\t')+ -> skip;
NIL : 'nil';
NEXT : 'next';