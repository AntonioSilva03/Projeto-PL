from ply import lex
import sys

# Lista de tokens
tokens = (
    'ID',
    'DASHDASH',
    'NUMBER',
    'ADD',
    'MINUS',
    'MINUS_MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'NOT',
    'INF',
    'INFEQ',
    'SUP',
    'SUPEQ',
    'DOT',
    'NEWLINE',
    'FUNCTION',
    'FUNCTION_STRING',
    'STRING',
    'EMIT',
    'CHAR',
    'SPACE',
    'CR',
    '2DUP',
    'CONDICIONAL1',
    'CONDICIONAL2',
)

# Expressão regulares para cada token
t_ID = r'[a-zA-Z]+'
t_DASHDASH = r'--'
t_ADD = r'\+'
t_MINUS = r'-'
t_MINUS_MINUS = r'--'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_NOT = r'!'
t_INF = r'<'
t_INFEQ = r'<='
t_SUP = r'>'
t_SUPEQ = r'>='
t_DOT = r'\.'
t_STRING = r'\.".*"'
t_SPACE = r'SPACE'
t_CR = r'CR'


# Ignorar espaços em branco
t_ignore = ' \t\n'

def t_2DUP(t):
    r'2DUP'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_FUNCTION(t):
    r':\s+([a-zA-Z]+)\s+\(\s*(.*?)\s*--\s*(.*?)\s*\)\s+(.*?)\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_CONDICIONAL1(t):
    r':\s+(\w+)\s+([^)]+)\s+IF\s+([^)]+)\s+ELSE\s+([^)]+)\s+THEN\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_CONDICIONAL2(t):
    r':\s+(\w+)\s+([^)]+)\s+IF\s+([^)]+)\s+THEN\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)'
    t.value = (t.value, t.lexer.lineno)
    return t


def t_CHAR(t):
    r'(\'[a-zA-Z0-9]\'\s+CHAR)'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_EMIT(t):
    r'("[a-zA-Z0-9]"|\'[a-zA-Z0-9]\')\s+EMIT'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_FUNCTION_STRING(t):
    r':\s+([a-zA-Z]+)\s+\."(.*?)"\s+;[\n]([a-zA-Z]+)'
    t.value = (t.value, t.lexer.lineno)
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print("Caractere ilegal: '%s' encontrado na linha; '%d'" % (t.value[0], t.lexer.lineno))
    sys.exit(0)
    

# Construção do lexer
lexer = lex.lex()