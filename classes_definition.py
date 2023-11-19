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

# Define the list of token names
tokens = list(reserved.values()) + [
    'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON', 'ASSIGN',
    'EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'AND', 'OR', 'NOT', 'INCREMENT', 'DECREMENT', 'DOT', 'ARROW', 'NUMBER', 
    'LEFT_BRACE', 'RIGHT_BRACE',
]

# Define a function for 'class'
def t_CLASS(t):
    r'class\b'  # Matching 'class' as a whole word
    return t

# Tokens

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_DOT = r'\.'
t_ARROW = r'->'
t_RETURN = r'return'
t_LEFT_BRACE = r'{'
t_RIGHT_BRACE = r'}'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Parser rules
def p_class(p):
    '''
    class : CLASS ID LEFT_BRACE class_body RIGHT_BRACE
    '''
    print(f"Valid Java class: {p[2]}")

def p_class_body(p):
    '''
    class_body : attribute class_body
               | empty
    '''
    pass

def p_attribute(p):
    '''
    attribute : type ID SEMICOLON
              | type ID LEFT_BRACE RIGHT_BRACE
              | type ID LEFT_BRACE class_body RIGHT_BRACE
    '''
    pass

def p_type(p):
    '''
    type : ID
    '''
    pass


def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

lexer = lex.lex()
parser = yacc.yacc()

# Define the entry point for the parser
def parse_input():
    lexer = lex.lex()
    parser = yacc.yacc()

    print("Enter class definition (enter an empty line to finish):")
    input_lines = []
    
    try:
        while True:
            line = input()
            if not line.strip():
                break
            input_lines.append(line)
    except EOFError:
        pass

    input_string = '\n'.join(input_lines)
    parser.parse(input_string)

# Parsing
parse_input()

'''
Testing examples(only simple class-object examples):

1) 
class Car{
String make;
int year;
}

2)
class BankAccount {
    String accountNumber;
    double balance;
    int x=0;
}

3)
class Student {
    String name;
    float marks;
}
'''