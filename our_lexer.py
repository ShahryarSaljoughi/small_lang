import ply.lex as lexer
import re

tokens = [
    'const',
    'var',
    'integer',
    'identifier',
    'whitespace',
]

t_keyword = r"""[c|C][o|O][n|N][s|S][t|T]|var|begin|end|integer|procedure|in
                |out|in out| print|
            """
t_integer = r''   
t_identifier = r''
t_whitespace = r''


int a = 345

lex.lex()