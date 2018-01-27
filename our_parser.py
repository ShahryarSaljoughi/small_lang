
import our_lexer
import ply.yacc as yacc

tokens = our_lexer.tokens



# by default start symbol is defined by the first rule function defined 
# but the below variable let's functions be moved :)
start = 'program'  

def p_program(p):
    ' program : A B C  BEGIN D END'


def p_A(p):
    '''A :  empty
            | CONST A_1'''
    



def p_A_1(p):
    '''A_1 :    const_decl
           |    const_decl A_1'''
    

def p_B(p):
    '''B : empty
         | VAR B_1'''
    

def p_B_1(p):
    '''B_1 : var_decl
           | var_decl B_1'''
    

def p_C(p):
    '''C : empty
         | proc_decl C'''
    

def p_D(p):
    '''D : statement
         | statement D'''
    

def p_const_decl(p):
    ''' const_decl : identifier E '=' integer_constant'''

def p_E(p):
    '''E :  empty 
         |  ',' identifier E'''
    

def p_var_decl(p):
    """ var_decl : identifier E ':' type """
    

def p_proc_decl(p):
    """proc_decl : PROCEDURE identifier '(' F ')' ';' block"""
    

def p_F(p):
    '''F : empty 
         | format F_1'''
    

def p_F_1(p):
    '''F_1 : empty
           | ';' format F_1'''
    

def p_format(p):
    '''format : identifier E ':' type
              | identifier E ':' mode type'''
    

def p_mode(p):
    '''mode : IN
            | OUT
            | IN_OUT'''
    

def p_type(p):
    'type : INTEGER'
    

def p_block(p):
    '''block : BEGIN A B D END
             | BEGIN A B END'''
    

def p_print(p):
    """ print : PRINT '(' string_constant G ')' """
    

def p_G(p):
    '''G : empty 
         | ',' expression G'''
    


def p_read(p):
    '''read : READ '(' string_constant H ')' '''
    

def p_H(p):
    ''' H : empty 
          | ',' var H'''
    

def p_cond(p):
    ''' cond : IF bool THEN statement
            | IF bool THEN statement ELSE statement'''
    

def p_call(p):
    """call : CALL identifier '(' ')'
            | CALL identifier '(' expression G ')' """
    

def p_var(p):
    """var : identifier
           | identifier '[' expression ']' """
    

def p_statement_assign(p):
    '''statement_assign : var assign_op expression 
    '''
    

def p_statement(p):
    '''statement : block  
                | print
                | read
                | statement_assign
                | cond
                | statement_for
                | return
                | call'''
    


def p_return(p):
    'return : RETURN'
    

def p_bool(p):
    """ bool : NOT bool
            | bool AND bool
            | bool OR bool
            | expression relop expression
            | '(' bool ')' """
    

def p_empty(p):
    'empty :'
    pass
    


def p_statement_for(p):
    ' statement_for : FOR identifier assign_op TO expression DO statement'
    

def p_relop(p):
    """  relop : '=' 
               | less_equal_sign
               | '>'
               | greater_equal_sign
               | '<'
               | not_equal_sign """

    

# expressions : **************
precedence = (
    ('left', 'AND', 'OR'),
    ('right','NOT'),
    ('left', '>', '<',
                    'greater_equal_sign', 
                    'less_equal_sign',     
                    'not_equal_sign'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS')
)

def p_expression(p):
    """expression : integer_constant
                  | expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | '-' expression %prec UMINUS
                  | '(' expression ')' 
                  | var """    

# ##################  Error Recovery  ##############

def p_error(p): # panic mode
    if not p:
        print("unexpected end of file")
        return

    # Read ahead looking for a closing '}'
    print("error here -->{}:{} near {}".format(p.lineno, p.lexpos, p.value))
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'END': 
            break
    parser.restart()

# ##################################################

parser = yacc.yacc(tabmodule='parsing_tables')
with open('input.txt') as f:
    s = f.read()
    yacc.parse(s)