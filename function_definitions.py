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
]

# Regular expressions for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
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


# Regular expression for identifiers (variable names and function names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Regular expression for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling rule for other characters
def t_error(t):
    r'[^\s]'  # Match any non-whitespace character
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Handle empty lines gracefully
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define the production rules for function definitions
def p_function_definition(p):
    '''
    function_definition : modifiers type ID LPAREN parameters RPAREN LBRACE function_body RBRACE
    '''
    print(f"Valid Function Definition:\n{p[1]} {p[2]} {p[3]}({p[5]}) {{\n{p[8]}\n}}")

def p_function_body(p):
    '''
    function_body : statements
                  | empty
    '''
    p[0] = p[1]

def p_modifiers(p):
    '''
    modifiers : PUBLIC
              | STATIC
              | PUBLIC STATIC
              | empty
              | PROTECTED
              | PRIVATE
    '''
    if len(p) == 1:
        p[0] = ""
    else:
        p[0] = " ".join(p[1:])

def p_type(p):
    '''
    type : INT
         | VOID
         | DOUBLE
         | STRING
    '''
    p[0] = p[1]

def p_parameters(p):
    '''
    parameters : parameter_list
               | empty
    '''
    if len(p) == 2:
        p[0] = p[1]

def p_parameter_list(p):
    '''
    parameter_list : type ID
                   | parameter_list COMMA type ID
    '''
    if len(p) == 3:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = f"{p[1]}, {p[3]} {p[4]}"

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = p[1]

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}\n{p[2]}"

def p_statement(p):
    '''
    statement : ID ASSIGN expression SEMICOLON
              | if_statement
              | empty
              | expression SEMICOLON
              | RETURN expression SEMICOLON
    '''
    if len(p) == 5:
        p[0] = f"{p[1]} {p[2]} {p[3]};"
    else:
        p[0] = p[1]

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN statement
                | IF LPAREN expression RPAREN statement ELSE statement
    '''
    if len(p) == 6:
        p[0] = f"if ({p[3]}) {p[5]}"
    else:
        p[0] = f"if ({p[3]}) {p[5]} else {p[7]}"

def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_term(p):
    '''
    term : factor
         | term TIMES factor
         | term DIVIDE factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_factor(p):
    '''
    factor : ID
           | NUMBER
           | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"({p[2]})"

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")

# Define an empty production for optional grammar elements
def p_empty(p):
    'empty :'
    pass

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Define the entry point for the parser
def parse_input():
    lexer = lex.lex()
    parser = yacc.yacc()

    print("Enter function declaration (enter an empty line to finish):")
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

#Parsing
parse_input()

'''
Some testing examples(only 1,2,3 are correct, 4 and 5 are illegal due to unavailable grammars)

1)
public int add(int a, int b) {
    return a + b;
}

2)
private double calculateAverage(int numbers) {
    return result;
}

3)
public static String concatenateStrings(String str1, String str2) {
    return str1 + str2;
}

4)
public void printMessage() {
    System.out.println("Hello, World!");
}

5)
public String checkNumber(int number) {
    if (number > 0) {
        return "Positive";
    } else if (number < 0) {
        return "Negative";
    } else {
        return "Zero";
    }
}

'''
