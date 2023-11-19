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
    'ID', 'INT', 'STRING',
    'ARRAY_LIST', 'HASH_SET', 'HASH_MAP', 'LINKED_LIST', 'PRIORITY_QUEUE', 'STACK',
    'ADD', 'REMOVE', 'DISPLAY',
)

# Define a function for 'ArrayList'
def t_ARRAY_LIST(t):
    r'ArrayList\b'  # Matching 'ArrayList' as a whole word
    return t

# Define a function for 'HashSet'
def t_HASH_SET(t):
    r'HashSet\b'  # Matching 'HashSet' as a whole word
    return t

# Define a function for 'HashMap'
def t_HASH_MAP(t):
    r'HashMap\b'  # Matching 'HashMap' as a whole word
    return t

# Define a function for 'LinkedList'
def t_LINKED_LIST(t):
    r'LinkedList\b'  # Matching 'LinkedList' as a whole word
    return t

# Define a function for 'PriorityQueue'
def t_PRIORITY_QUEUE(t):
    r'PriorityQueue\b'  # Matching 'PriorityQueue' as a whole word
    return t

# Define a function for 'Stack'
def t_STACK(t):
    r'Stack\b'  # Matching 'Stack' as a whole word
    return t

# Define a function for 'add'
def t_ADD(t):
    r'add\b'  # Matching 'add' as a whole word
    return t

# Define a function for 'remove'
def t_REMOVE(t):
    r'remove\b'  # Matching 'remove' as a whole word
    return t

# Define a function for 'display'
def t_DISPLAY(t):
    r'display\b'  # Matching 'display' as a whole word
    return t

# Tokens
t_STRING = r'\"[^\"]*\"'  # Matches double-quoted strings
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Matches identifiers
t_INT = r'\d+'  # Matches integers
t_ignore = ' \t\n'  # Ignore spaces, tabs, and newlines


# Error handling rule for other characters
def t_error(t):
    r'[^\s]'  # Match any non-whitespace character
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Handle empty lines gracefully
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Collection data
collections = {}

# Parser rules
def p_command(p):
    '''
    command : create_collection
            | add_element
            | remove_element
            | display_content
    '''
    print(p[1])

def p_create_collection(p):
    '''
    create_collection : ARRAY_LIST ID
                      | HASH_SET ID
                      | HASH_MAP ID
                      | LINKED_LIST ID
                      | PRIORITY_QUEUE ID
                      | STACK ID
    '''
    p[0] = f"Creating {p[1]} named '{p[2]}'"
    collections[p[2]] = []

def p_add_element(p):
    '''
    add_element : ADD ID STRING
    '''
    if p[2] in collections:
        collections[p[2]].append(p[3])
        p[0] = f"Adding '{p[3]}' to {p[2]}"
    else:
        p[0] = f"{p[2]} doesn't exist!"

def p_remove_element(p):
    '''
    remove_element : REMOVE ID STRING
    '''
    if p[2] in collections:
        if p[3] in collections[p[2]]:
            collections[p[2]].remove(p[3])
            p[0] = f"Removing '{p[3]}' from {p[2]}"
        else:
            p[0] = f"'{p[3]}' not found in {p[2]}"
    else:
        p[0] = f"{p[2]} doesn't exist!"

def p_display_content(p):
    '''
    display_content : DISPLAY ID
    '''
    if p[2] in collections:
        p[0] = f"Displaying contents of {p[2]}: {collections[p[2]]}"
    else:
        p[0] = f"{p[2]} doesn't exist!"

def p_error(p):
    print(f"Syntax error at '{p.value}'")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    input_string = input("Enter collection construct:\n")
    if input_string.lower() == 'exit':
        break
    parser.parse(input_string)


'''
Testing examples:

Creating Collections:

Create an ArrayList: ArrayList myList
Create a HashSet: HashSet mySet
Create a HashMap: HashMap myMap
Create a LinkedList: LinkedList myList
Create a PriorityQueue: PriorityQueue myQueue
Create a Stack: Stack myStack

Adding Elements:
Add to ArrayList: add myList "Java"
Add to HashSet: add mySet "Apple"
Add to HashMap: add myMap "Key1" "Value1"
Add to LinkedList: add myList "Python"
Add to PriorityQueue: add myQueue "5"
Add to Stack: add myStack "First"

Removing Elements:
Remove from ArrayList: remove myList "Java"
Remove from HashSet: remove mySet "Apple"
Remove from HashMap: remove myMap "Key1"
Remove from LinkedList: remove myList "Python"
Remove from PriorityQueue: remove myQueue "5"
Remove from Stack: remove myStack "First"

Displaying Contents:
Display ArrayList: display myList
Display HashSet: display mySet
Display HashMap: display myMap
Display LinkedList: display myList
Display PriorityQueue: display myQueue
Display Stack: display myStack
'''