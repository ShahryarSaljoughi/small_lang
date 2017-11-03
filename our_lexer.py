import ply.lex as lexer
import re


# literals are single characters. 
# Their class(type) is the same as their lexeme.
# They are the last thing to be checked. 
# So if a rule starts with a literal, it will take precedence .
literals = ['+', '-', '/', '*', '=', ',', '(', ')']


keywords = {
    
}


tokens = [
    # KEYWORDS:
    'const',  
    'var',
    'begin',
    'end',
    'integer',
    'procedure',
    'in',
    'out',
    'in_out',
    'for',
    'print',
    'read',
    'if',
    'then',
    'else',
    'to',
    'do',
    'return',
    'call',
    'not',
    'or',
    'and', 
    # IDENTIFIER
    'identifier', 
    # WHITESPACE
    'whitespace',
    # SPECIAL CHARACTERS:
    'assign_op',            # :=          
    'semicolon',            # ;
    'comma',                # ,
    'l_parenthese',         # (
    'r_parenthese',         # )
    'minus_sign',           # -
    'plus_sign',            # + 
    'mul_sign',             # *
    'divide_sign',          # /
    'equal_sign'            # =
    'less_equal_sing'       # <=
    'greater_equal_sign',   # >=
    'greater_sign',         # >
    'less_sign',            # <
    'not_equal_sign',       # <>
]

lexer.lex(reflags=re.IGNORECASE)
