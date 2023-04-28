grammar Expresso;

// Parser rules
program: (concept_declaration | type_declaration | method_declaration | variable_declaration | statement)*;

concept_declaration: CONCEPT ID LT type_name_list GT LCURLY (concept_body SEMI)* RCURLY;
concept_body: (concept_declaration | type_declaration | variable_declaration | statement)*;

type_declaration: TYPE ID (LCURLY type_body RCURLY | SEMI);
type_body: (concept_declaration | type_declaration | method_declaration | variable_declaration)*;

method_declaration: METHOD ID LPAREN params RPAREN (LCURLY method_body RCURLY | SEMI);
params: (type_name ID (COMMA type_name ID)*)?;
method_body: program;

variable_declaration: type_name ID (ASSIGN value)? SEMI;

statement: value_statement | throw_statement;
throw_statement: THROW value_statement;
value_statement: value SEMI;
value: expression | logic;

logic: or;
or: and ((OR) and)*;
and: equality((AND) equality)*;
equality: comparable ((EQ | NE) comparable)*;
relational: expression((LT | LE | GT | GE) expression)*;

comparable: relational | method_call | concept;
concept: type_name | method_signature;
method_signature: METHOD ID LPAREN params RPAREN;

expression: term ((PLUS | MINUS) term)*;
term: factor ((STAR | SLASH) factor)*;
factor: LPAREN expression RPAREN | method_call | ID | NUMBER;
method_call: ID LPAREN (value (COMMA value)*)? RPAREN;

placeholder: 'placeholder';
type_name: ID (LT type_name_list GT)?;
type_name_list: type_name (COMMA type_name)*;

// Lexer rules
TYPE: 'type';
METHOD: 'method';
CONCEPT: 'concept';
THROW: 'throw';
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
