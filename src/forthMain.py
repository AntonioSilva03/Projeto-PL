from forthLexer import lexer
from forthYacc import parse_input as parser
import sys
import os

def main(args):

    if len(args) != 2:
        print("Como correr: python script.py <ficheiro_de_teste>")
        return
    
    file_name = args[1]
    output_dir = '../out'

    with open(file_name, 'r') as file:
        data = file.read()

    dois_pontos = 0
    ponto_virgula = 0
    L_parenteses = 0
    linha = 1;
    R_parenteses = 0
    pontos_linha = 0
    parenteses_linha = 0

    for letter in data:
        if letter == ':':
            dois_pontos = dois_pontos + 1
        elif letter == ';':
            ponto_virgula = ponto_virgula + 1
            pontos_linha = linha
        elif letter == '(':
            L_parenteses = L_parenteses + 1
        elif letter == ')':
            R_parenteses = R_parenteses + 1
            parenteses_linha = linha
        elif letter == '\n':
            linha = linha + 1

    if dois_pontos != ponto_virgula:
        print("Erro: O número de ':' e ';' não é igual\nÚltima ocorrência de ';' na linha", pontos_linha)
        return
    if L_parenteses != R_parenteses:
        print("Erro: O número de '(' e ')' não é igual\nÚltima ocorrência de ')' na linha", parenteses_linha)
        return
            
    lexer.input(data)

    code = parser(data)
    code += 'STOP\n'

    # Use os.path.basename to get the file name without directory path
    output_file_path = os.path.join(output_dir, f'{os.path.splitext(os.path.basename(file_name))[0]}.txt')
    with open(output_file_path, 'w') as file:
        file.write(code)

if __name__ == '__main__':
    main(sys.argv)