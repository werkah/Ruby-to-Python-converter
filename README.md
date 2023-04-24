# Ruby to Python converter

## Tokeny

|      Opis       |      Token      |
| :--------------: | :------------: |
|“DOT” | . |
“COMMA” | ,
“PIPELINE” | \|
“BACKSLASH” | /
“AT” | @
“ATAT” | @@
“DOLAR” | $
“NEWLINE” | \n
“HASH” | #
“SEMICOLON” | ;
“ID” |  [a-zA-Z_][a-zA-Z0-9_]* 
“STRING” | [a-zA-Z0-9]* 
“NUMBER” |  [0-9]+ | ([0-9]* DOT [0-9]+) 
“COMMENT” |  [^\n]*
“APOSTROPHE” | “
“IF” | if
“ELSIF” | elsif
“ELSE” | else
“UNLESS” | unless
“CASE” | case
“WHEN” | when
“WHILE” | while
“DO” | do
“FOR” | for
“IN” | in
“UNTIL” | until
“BEGIN” |begin
“END” | end
“PUTS” | puts
“LEFTPAREN” | (
“RIGHTPAREN” | )
“LEFTBRACE” | {
“RIGHTBRACE” | }
“LEFTBRACKET” | [
“RIGHTBRACKET” | ]
“AND” | \(and \| &&)
“OR” | \(or \| \|\|)
“EQUAL” | =
“PLUS” | +
“MINUS” | -
“MUL” | *
“DIV” | \
“MOD” | %
“INTERJECT” | !
“LEFTMINSIGN” | <
“RIGHTMAXSIGN” | >
“RETURN” | return
“CLASS” | class
“EQUALEQUAL” | ==
“PLUSPLUS” | ++
“MINUSMINUS” | –
“MULMUL” | **
“NOTEQUAL” |  !=
“PLUSEQUAL” |  +=
“MINUSEQUAL” |  -=
“MULEQUAL” | *=
“MULMULEQUAL” | **=
“DIVIDEEQUAL” | /=
“MODEQUAL” | %=
“MORE” | >
“LESS” | <
“MOREEQUAL” | >=
“LESSEQUAL” | <=
“LESSEQUALMORE” | ⇔
“EQUALEQUALEQUAL” | ===

## Gramatyka 

``` antlr
<program>::= <statement_list>
<statement_list>::= <terminator> | <statement> <terminator> | <statement_list> <statement> <terminator>
<terminator>:: =NEWLINE | SEMICOLON
<statement>:: =<function> | COMMENT | <loop> | <variables> | <function_call>| <assignment>
<loop>::= <if_instruction> | <unless_instruction> | <while_loop> |
<do_while_loop> | <for_loop> | <until_loop> | <do_until_loop>
<bool>::= TRUE | FALSE
<type> ::= AT|ATAT|DOLLAR 
<string> ::= APOSTROPHE STRING APOSTROPHE
<comment> ::= HASH COMMENT 
<array> ::= LEFTBRACKET(<value>|<bool>)[COMMA (<value>|<bool>)]* RIGTHBRACKET
<value> ::= NUMBER| STRING
<if_instruction> ::=  IF<condition><loop_body>[ELSIF<condition><loop_body>]*[ELSE <condition><loop_body>] END
<unless_instruction> ::= UNLESS<condition><loop_body>[ELSE<condition><loop_body>] END
<while_loop> ::= WHILE<condition>DO<loop_body>END
<do_while_loop> ::= BEGIN<loop_body>END WHILE<condition>
<for_loop> ::= FOR ID IN(<array>|<value>)<loop_body>END
<until_loop> ::= BEGIN<loop_body>END UNTIL<condition>
<do_until_loop> ::= UNTIL<condition DO <loop_body>END
<comparisonOperator> ::= MORE| LESS| LESSEQUAL| MOREEQUAL| LESSEQUALMORE| EQUALEQUAL| NOTEQUAL|EQUALEQUALEQUAL
<operator> ::=PLUS |MINUS|MUL|DIVIDE|MOD|MULMUL
<condition> ::= (ID<comparisonOperator><value>|<value><comparisonOperator><value>|ID<comparisonOperator>ID)[[AND | OR][ID<comparisonOperator><value>|<value><comparisonOperator><value>|ID<comparisonOperator>ID]]*
<variables> ::=[<type>]ID EQUAL(<value>|ID|<mathoperations>|<array>)
<sign> ::= PLUS | MINUS
<mathoperation>::= [<sign>](ID|<value>|<bracketExpression>)<operator>(ID|<value>|<bracketExpression>)
<bracketExpression> ::= LEFTPAREN<mathoperations>RIGHTPAREN
<function> ::= DEF ID [<parameters>] <loop_body>[RETURN (ID|<value>|<array>)[COMMA(ID>|<value>|<array>)]*] END 
<parameters> ::= LEFTPAREN ID [COMMA ID]  RIGHTPAREN
<function_call> ::= ID [LEFTPAREN <value> [ COMMA <value> ]* RIGHTPAREN]
<assignmentOperator> ::= PLUSEQUAL |  MINUSEQUAL |  MULEQUAL | MULMULEQUAL | DIVIDEEQUAL | MODEQUAL|
<loop_body> ::= <statement> [<statement>]*
<assignment> ::= ID<assignmentOperator><value>|ID<assignmentOperator>ID|ID<assignmentOperator><array>
```
