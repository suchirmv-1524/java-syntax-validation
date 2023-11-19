import ply.lex as lex
import ply.yacc as yacc

# Disable unused token warnings
# pylint: disable=unused-token 

# Define the list of Java keywords and reserved words
reserved = {
    'abstract': 'ABSTRACT',
    'assert': 'ASSERT',
    'boolean': 'BOOLEAN',
    'break': 'BREAK',
    'byte': 'BYTE',
    'case': 'CASE',
    'catch': 'CATCH',
    'char': 'CHAR',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'do': 'DO',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'extends': 'EXTENDS',
    'false': 'FALSE',
    'final': 'FINAL',
    'finally': 'FINALLY',
    'float': 'FLOAT',
    'for': 'FOR',
    'if': 'IF',
    'implements': 'IMPLEMENTS',
    'import': 'IMPORT',
    'instanceof': 'INSTANCEOF',
    'int': 'INT',
    'interface': 'INTERFACE',
    'long': 'LONG',
    'native': 'NATIVE',
    'new': 'NEW',
    'null': 'NULL',
    'package': 'PACKAGE',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'return': 'RETURN',
    'short': 'SHORT',
    'static': 'STATIC',
    'strictfp': 'STRICTFP',
    'String': 'STRING',
    'super': 'SUPER',
    'switch': 'SWITCH',
    'synchronized': 'SYNCHRONIZED',
    'this': 'THIS',
    'throw': 'THROW',
    'throws': 'THROWS',
    'transient': 'TRANSIENT',
    'true': 'TRUE',
    'try': 'TRY',
    'void': 'VOID',
    'volatile': 'VOLATILE',
    'while': 'WHILE',
}

# Define tokens
tokens = (
    'ID', 'VECTOR', 'ADD', 'GET', 'REMOVE', 'SIZE',
    'INTEGER', 'SEMICOLON'
)

# Define a function for 'Vector'
def t_VECTOR(t):
    r'Vector\b'  # Matching 'Vector' as a whole word
    return t

# Define a function for 'add'
def t_ADD(t):
    r'add\b'  # Matching 'add' as a whole word
    return t

# Define a function for 'remove'
def t_REMOVE(t):
    r'remove\b'  # Matching 'remove' as a whole word
    return t

# Define a function for 'size'
def t_SIZE(t):
    r'size\b'  # Matching 'size' as a whole word
    return t

# Define a function for 'get' which is basically displaying vector item by item
def t_GET(t):
    r'get\b'  # Matching 'get' as a whole word
    return t

# Tokens
t_INTEGER = r'\d+'
t_SEMICOLON = r';'
t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'Vector':
        t.type = 'VECTOR'
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


# Updated parser rules
def p_statement(p):
    '''
    statement : VECTOR ID SEMICOLON
              | ID ADD INTEGER SEMICOLON
              | ID GET INTEGER SEMICOLON
              | ID REMOVE INTEGER SEMICOLON
              | ID SIZE SEMICOLON
              | ID SEMICOLON
    '''
    print(f"Valid Java Vector construct: {' '.join(p[1:])}")


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    input_string = input("Enter vector construct:\n")
    if input_string.lower() == 'exit':
        break
    parser.parse(input_string)

'''
Testing examples:

Creating a Vector:
Vector vec;

Adding elements to the Vector:
vec add 5;
vec add 10;
vec add 15;

Getting elements from the Vector:
vec get 0;
vec get 2;

Removing elements from the Vector:
vec remove 1;
vec remove 0;

Getting the size of the Vector:
vec size;

'''