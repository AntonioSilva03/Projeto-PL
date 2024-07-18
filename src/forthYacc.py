import ply.yacc as yacc
from forthLexer import tokens
import re
import sys

stack = []
vm_code = ""

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:
        p[0] = p[1]
        
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

def p_statement(p):
    '''statement : function_declaration
                 | expressiontypes
                 | function_dot
                 | arithmetic_expression
                 | comparison_expression
                 | function_string
                 | function_char
                 | function_emit
                 | space
                 | cr
                 | 2dup
                 | condicinal1
                 | condicinal2'''
    p[0] = ('statement', p[1])


def p_function_declaration(p):
    '''
    function_declaration : FUNCTION
    '''
    global vm_code
    num = 0
    function_def, lineno = p[1]
    function_name, parameters, return_type, function_body, number1, number2, name = re.match(r':\s+([a-zA-Z]+)\s+\(\s*(.*?)\s*--\s*(.*?)\s*\)\s+(.*?)\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)', function_def).groups()
    # Process function declaration here, for example:
    if function_name != name:
        print("Function name doesn't match the name of the function")
        return
    vm_code += f"PUSHN 0\n"
    vm_code += f"START\n"
    try:
        # Tenta converter a string para um número inteiro
        inteiro = int(number1)
        inteiro2 = int(number2)
        vm_code += f"PUSHI {inteiro}\n"
        stack.append(inteiro)
        vm_code += f"PUSHI {inteiro2}\n"
        stack.append(inteiro2)
    except ValueError:
        try:
            # Tenta converter a string para um número de ponto flutuante
            flutuante = float(number1)
            flutuante2 = float(number2)
            num = 1
            vm_code += f"PUSHF {flutuante}\n"
            stack.append(flutuante)
            vm_code += f"PUSHF {flutuante2}\n"
            stack.append(flutuante2)
        except ValueError:
            pass

    expressao(function_body, num)


def p_cr(p):
    '''cr : CR'''
    global vm_code
    vm_code += f"WRITELN\n"

def p_function_char(p):
    '''function_char : CHAR'''
    global vm_code
    function_def, lineno = p[1]
    char_value, name = re.match(r'(\'[a-zA-Z0-9]\')\s+(CHAR)', function_def).groups()
    vm_code += f"pushs {char_value}\n"
    vm_code += f"CHRCODE\n"


def p_space(p):
    '''space : SPACE'''
    global vm_code
    vm_code += f"PUSHS ' '\n"

def p_function_string(p):
    '''function_string : FUNCTION_STRING'''
    global vm_code
    function_def, lineno = p[1]
    string_name, string_value, name = re.match(r':\s+([a-zA-Z]+)\s+\."(.*?)"\s+;[\n]([a-zA-Z]+)', function_def).groups()
    if string_name != name:
        print("String doens't match the name of the function")
        return
    vm_code += f"PUSHN 0\n"
    vm_code += f"START\n"
    vm_code += f"PUSHS \"{string_value}\"\n"
    vm_code += f"WRITES\n"

def p_function_emit(p):
    '''function_emit : EMIT'''
    global vm_code
    function_def, lineno = p[1]
    emit_value, name = re.match(r'("[a-zA-Z0-9]"|\'[a-zA-Z0-9]\')\s+(EMIT)', function_def).groups()
    vm_code += f"PUSHS {emit_value}\n"
    vm_code += f"WRITES\n"


def p_expressiontypes(p):
    '''expressiontypes : NUMBER '''
                  # | STRING
                  # | VARIABLE
                  # | CHAR
                  # | EMIT
    global vm_code
    p[0] = p[1]
    if isinstance(p[1], int):
        stack.append(p[1])
        vm_code += f"PUSHI {p[1]}\n"
    elif isinstance(p[1], float):
        stack.append(p[1])
        vm_code += f"PUSHF {p[1]}\n"

def p_function_dot(p):
    '''function_dot : DOT'''
    global vm_code
    if len(stack) == 0:
        print("Stack is empty")
        return
    top_stack = stack.pop()
    if isinstance(top_stack, int):
        vm_code += f"WRITEI\nWRITELN\n"
    elif isinstance(top_stack, float):
        vm_code += f"WRITEF\nWRITELN\n"
    elif isinstance(top_stack, str):
        vm_code += f"WRITES\nWRITELN\n"
    p[0] = top_stack

def p_arithmetic_expression(p):
    '''arithmetic_expression : statement statement arithmetic_op'''
    global vm_code
    if len(stack) < 2:
        print("Stack is doesn't have enough elements")
        return
    b = stack.pop()
    a = stack.pop()
    op = p[3]
    if op == '+':
        result = a + b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"ADD\n"
        else:
            vm_code += f"FADD\n"
    elif op == '-':
        result = a - b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"SUB\n"
        else:
            vm_code += f"FSUB\n"
    elif op == '*':
        result = a * b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"MUL\n"
        else:
            vm_code += f"FMUL\n"
    elif op == '/':
        result = a / b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"DIV\n"
        else:
            vm_code += f"FDIV\n"
    elif op == '%':
        result = a % b
        stack.append(result)
        vm_code += f"MOD\n"

def p_arithmetic_op(p):
    '''arithmetic_op : ADD
                     | MINUS
                     | TIMES
                     | DIVIDE
                     | MOD'''
    p[0] = p[1]

def p_comparison_expression(p):
    '''comparison_expression : statement statement comparison_op'''
    global vm_code
    if len(stack) < 2:
        print("Stack is doesn't have enough elements")
        return
    b = stack.pop()
    a = stack.pop()
    op = p[3]
    if op == '<':
        result = a < b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"INF\n"
        else:
            vm_code += f"FINF\n"
    elif op == '<=':
        result = a <= b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"INFEQ\n"
        else:
            vm_code += f"FINFEQ\n"
    elif op == '>':
        result = a > b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"SUP\n"
        else:
            vm_code += f"FSUP\n"
    elif op == '>=':
        result = a >= b
        stack.append(result)
        if isinstance(result, int):
            vm_code += f"SUPEQ\n"
        else:
            vm_code += f"FSUPEQ\n"


def p_condicinal1(p):
    '''condicinal1 : CONDICIONAL1'''
    global vm_code
    num = 0
    function_def, lineno = p[1]
    function_name, condi, expressao1, expressao2, number1, number2, function_name = re.match(r':\s+(\w+)\s+([^)]+)\s+IF\s+([^)]+)\s+ELSE\s+([^)]+)\s+THEN\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)', function_def).groups()
    vm_code += f"PUSHN 0\n"
    vm_code += f"START\n"
    try:
        inteiro = int(number1)
        inteiro2 = int(number2)
        vm_code += f"PUSHI {inteiro}\n"
        stack.append(inteiro)
        vm_code += f"PUSHI {inteiro2}\n"
        stack.append(inteiro2)
    except ValueError:
        try:
            flutuante = float(number1)
            flutuante2 = float(number2)
            num = 1
            vm_code += f"PUSHF {flutuante}\n"
            stack.append(flutuante)
            vm_code += f"PUSHF {flutuante2}\n"
            stack.append(flutuante2)
        except ValueError:
            pass

    expressao(condi, num)
    vm_code += f"JZ else1\n"
    expressao(expressao1, num)
    vm_code += f"JUMP endif1\n"
    vm_code += f"else1:\n"
    expressao(expressao2, num)
    vm_code += f"JUMP endif1\n"
    vm_code += f"endif1:\n"
    

    

def p_condicinal2(p):
    '''condicinal2 : CONDICIONAL2'''
    global vm_code
    num = 0
    function_def, lineno = p[1]
    function_name, condi, expressao1, number1, number2, function_name = re.match(r':\s+(\w+)\s+([^)]+)\s+IF\s+([^)]+)\s+THEN\s*;\n(.*?)\s+(.*?)\s+([a-zA-Z]+)', function_def).groups()
    print(function_name)
    vm_code += f"PUSHN 0\n"
    vm_code += f"START\n"
    try:
        inteiro = int(number1)
        inteiro2 = int(number2)
        vm_code += f"PUSHI {inteiro}\n"
        stack.append(inteiro)
        vm_code += f"PUSHI {inteiro2}\n"
        stack.append(inteiro2)
    except ValueError:
        try:
            flutuante = float(number1)
            flutuante2 = float(number2)
            num = 1
            vm_code += f"PUSHF {flutuante}\n"
            stack.append(flutuante)
            vm_code += f"PUSHF {flutuante2}\n"
            stack.append(flutuante2)
        except ValueError:
            pass
    expressao(condi, num)
    vm_code += f"JZ else1\n"
    expressao(expressao1, num)
    vm_code += f"JUMP endif1\n"
    vm_code += f"else1:\n"
    vm_code += f"endif1:\n"

def p_2dup(p):
    '''2dup : 2DUP'''
    global vm_code
    if len(stack) < 2:
        print("Stack is doesn't have enough elements")
        return
    a = stack[-2]
    b = stack[-1]
    stack.append(a)
    stack.append(b)
    if isinstance(a, int):
        vm_code += f"PUSHI {a}\n"
    else:
        vm_code += f"PUSHF {a}\n"
    if isinstance(b, int):
        vm_code += f"PUSHI {b}\n"
    else:
        vm_code += f"PUSHF {b}\n"

def p_comparison_op(p):
    '''comparison_op : INF
                     | INFEQ
                     | SUP
                     | SUPEQ'''
    p[0] = p[1]
  
def p_error(p):
    if(p):
        print("Invalid syntax at '%s'" % p.value)
        parser.errok()
        sys.exit()

parser = yacc.yacc()

def parse_input(data):
    global vm_code
    parser.parse(data)
    return vm_code

def expressao(expressao, num):
    global vm_code
    split_condi = expressao.split()

    for parte in split_condi:
        if parte == '+':
            if num == 1:
                vm_code += f"FADD\n"
            else: vm_code += f"ADD\n"
        elif parte == '-':
            if num == 1:
                vm_code += f"FSUB\n"
            else: vm_code += f"SUB\n"
        elif parte == '*':
            if num == 1:
                vm_code += f"FMUL\n"
            else: vm_code += f"MUL\n"
        elif parte == '/':
            if num == 1:
                vm_code += f"FDIV\n"
            else: vm_code += f"DIV\n"
        elif parte == '%':
                vm_code += f"MOD\n"
        elif parte == '<':
            vm_code += f"INF\n"
        elif parte == '<=':
            vm_code += f"INFEQ\n"
        elif parte == '>':
            vm_code += f"SUP\n"
        elif parte == '>=':
            vm_code += f"SUPEQ\n"
        elif parte == '2DUP':
            a = stack[-2]
            b = stack[-1]
            stack.append(a)
            stack.append(b)
            if isinstance(a, int):
                vm_code += f"PUSHI {a}\n"
            else:
                vm_code += f"PUSHF {a}\n"
            if isinstance(b, int):
                vm_code += f"PUSHI {b}\n"
            else:
                vm_code += f"PUSHF {b}\n"
        elif parte == '.':
            top_stack = stack.pop()
            if isinstance(top_stack, int):
                vm_code += f"WRITEI\nWRITELN\n"
            elif isinstance(top_stack, float):
                vm_code += f"WRITEF\nWRITELN\n"
            elif isinstance(top_stack, str):
                vm_code += f"WRITES\nWRITELN\n"
        elif re.match(r'\.".+?"', parte):
            parte_sem_ponto = parte.replace('.', '')
            vm_code += f"PUSHS {parte_sem_ponto}\n"
            vm_code += f"WRITES\n"
        elif parte == 'SWAP':
            vm_code += f"SWAP\n"
        else:
            try:
                inteiro = int(parte)
                stack.append(inteiro)
                vm_code += f"PUSHI {inteiro}\n"
            except ValueError:
                try:
                    flutuante = float(parte)
                    stack.append(flutuante)
                    vm_code += f"PUSHF {flutuante}\n"
                except ValueError:
                    print(f'Invalid input {parte}')
                    sys.exit(0)