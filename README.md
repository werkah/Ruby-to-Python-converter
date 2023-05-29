# Ruby to Python converter

## Dane studenta(-ów)
- Weronika Hilaszek
- Karolina Surówka

## Dane kontaktowe
- wehilaszek@student.agh.edu.pl
- karsur@student.agh.edu.pl

## Założenia programu
### Ogólne cele programu
- konwersja kodu Ruby do Pythona

### Rodzaj translatora
- kompilator

### Planowany wynik działania programu
- kod w języku Ruby zostanie przekonwertowany na kod w języku Python

### Planowany język implementacji
- Python

### Sposób realizacji skanera/parsera
- wykorzystanie generatora parserów ANTLR4

## Tokeny
    
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

## Gramatyka 

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
variables: ID EQUAL (value | ID | array | mathOperation|bool);
mathOperation: (ID | value | bracketExpression) (operator (ID | value | bracketExpression))*;
bracketExpression: LEFTPAREN mathOperation RIGHTPAREN;
function: DEF ID LEFTPAREN parameters? RIGHTPAREN terminator loopBody (RETURN parameters crlf)? END;
parameters:(ID | value | bool) (COMMA (ID | value | bool))*;
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

## Krótka instrukcja użycia
- instalacja ANTLR4: `pip install antlr4-python3-runtime`
- należy umieścić plik z kodem w języku Ruby w folderze `examples`
- w pliku `main.py` należy zmienić nazwę pliku z kodem Ruby na nazwę pliku, który chcemy przekonwertować
- uruchomienie programu: `python3 main.py`
- wygenerowany kod w języku Python znajduje się w głównym folderze w pliku `output.py`

## Przykład użycia 

### Przykładowy kod w języku Ruby

``` ruby

