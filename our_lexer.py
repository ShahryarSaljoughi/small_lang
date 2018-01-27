import ply.lex as lexer
import re


# literals are single characters. 
# Their class(type) is the same as their lexeme.
# They are the last thing to be checked. 
# So if a rule starts with a literal, it will take precedence .
literals = ['+', '-', '/', '*', '=', ',', '(', ')', ';', '[', ']', ':', '<', '>']


keywords = {                      # keys are lexeme names
    'const': 'CONST',             # values are class names (type names)
    'var': 'VAR',
    'begin': 'BEGIN' ,
    'end': 'END',
    'integer': 'INTEGER',
    'string': 'STRING',
    'procedure': 'PROCEDURE',
    'in': 'IN',
    'out': 'OUT',
    # 'in out': 'IN_OUT',
    'for': 'FOR',
    'print': 'PRINT',
    'read': 'READ',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'to': 'TO',
    'do': 'DO',
    'return': 'RETURN',
    'call': 'CALL',
    'not': 'NOT',
    'or': 'OR',
    'and': 'AND',   
}


tokens = [
    'IN_OUT',
    'comment',
    'identifier',
    'integer_constant',
    'string_constant', 
    'assign_op',            # :=          
    'less_equal_sign',      # <=
    'greater_equal_sign',   # >=
    'not_equal_sign',       # <>
] + list(keywords.values())

t_ignore_comment = r'/\*.*\*/'

# t_integer_constant = r'[1-9][0-9]*'

t_string_constant = r'".*"'

t_assign_op = r':='

t_less_equal_sign = r'<='

t_greater_equal_sign = r'>='

t_not_equal_sign = r'<>'

def t_IN_OUT(t):
    r'in out'
    t.type = 'IN_OUT'
    return t


def t_identifier(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value,'identifier')    # Check for reserved words
    return t

def t_integer_constant(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    t.type = 'integer_constant'
    return t  

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) 
    # there is no return ! so newlines are skipped!

# The characters given in t_ignore are not ignored when
# such characters are part of other regular expression patterns
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

my_lexer = lexer.lex(reflags=re.IGNORECASE)

data = '''

var bb: integer
const a=10
const b=3
const c=5
var result: integer
var e: string

procedure max(max: in out integer, a in integer)
begin
    var max: integer
    max := a
    if b>max then max := b 
    if c>max then max := c
    return;
end

begin 
    
    call max(a, b, c, result)
    print("max is :", result)
end
'''
# my_lexer.input(data)
# while True:
#     tok = my_lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)