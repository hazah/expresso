grammar Expresso;

// Parser rules
program: (type_declaration | method_declaration | variable_declaration)*;

type_declaration: TYPE ID (LCURLY type_body RCURLY | SEMI);
type_body: (method_declaration | variable_declaration)*;
method_declaration: METHOD ID LPAREN params RPAREN (LCURLY method_body RCURLY | SEMI);
params: (type ID (COMMA type ID)*)?;
method_body: (variable_declaration | statement)*;

variable_declaration: type ID (ASSIGN expression)? SEMI;

statement: expression;

// if: IF LPAREN logic RPAREN block;
// block: LCURLY (variable_declaration | statement)* RCURLY;

logic: or;
or: and ((OR) and)*;
and: equality((AND) equality)*;
equality: relational ((EQ | NE) relational)*;
relational: expression((LT | LE | GT | GE) expression)*;

expression: term ((PLUS | MINUS) term)*;
term: factor ((STAR | SLASH) factor)*;
factor: LPAREN expression RPAREN | function_call | ID | NUMBER;
function_call: ID LPAREN (expression (COMMA expression)*)? RPAREN;

placeholder: 'placeholder';
type: ID;

// Lexer rules
IF: 'if';
TYPE: 'type';
METHOD: 'method';
LCURLY: '{';
RCURLY: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
ASSIGN: '=';
AND: 'and';
OR: 'or';

LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
EQ: '==';
NE: '!=';

PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
