# Escreva um programa em Python que:
# - gere uma estrutura que armazena o nome dos arquivos em 
# um determinado diretório e a quantidade de bytes que 
# eles ocupam em disco. Obtenha o nome do diretório do usuário.
# - Ordene decrescentemente esta estrutura pelo valor
# da quantidade de bytes ocupada em disco 
# (pode usar as funções sort ou sorted);
# - gere um arquivo texto com os valores desta estrutura ordenados.

import os, re, shutil, collections

path = input("Informe o diretório (usando \) para saber o tamanho dos arquivos existentes nele:\n")
dirs = os.listdir(path)
name_of_files_in_dir = {}

def format_dir(inputUser):
    formatedInput = re.sub(r'(\\)', r'\\\\', inputUser)
    return formatedInput

def get_size_and_name_of_files():
    name_dir = format_dir(path)
    complete_path = os.path.abspath(name_dir)
    print(complete_path)
    if os.path.exists(complete_path):
        for file in dirs:
            # print('file:', file)
            if os.path.isfile(file):
                size_file = os.path.getsize(file)
                #informa o tamanho em byte de cada arquivo, de forma decrescente
                print("O tamanho do arquivo", file, "é", size_file, "bytes")
                ##Armazenando o nome dos arquivos que estão dentro desse diretório, passado pelo usuário
                if file not in name_of_files_in_dir and size_file not in name_of_files_in_dir:
                    if os.path.isfile(file):
                        name_of_files_in_dir[file] = size_file
            # else:
            #     print('Não encontrei arquivo para calcular o tamanho')
    else:
        print('Diretorio informado não existe')

def order_dict():
    dict_ord_desc = sorted(name_of_files_in_dir.items(), key=lambda kv: kv[1], reverse=True)
    ##array de tuplas sendo convertido em dictionary
    return dict(dict_ord_desc)

def generate_file_txt():
    order_files = order_dict()
    new_file = open("dados_ordenados.txt", "w+")
    for i in order_files:
        new_file.write(str(order_files[i])+" bytes\n")

def open_file_with_data():
    name_file = "dados_ordenados.txt"
    if os.path.isfile(name_file):
        os.startfile(name_file)
    else:
        print("Arquivo não foi criado corretamente e não existe")
    
def main():
    get_size_and_name_of_files()
    generate_file_txt()
    open_file_with_data()

if __name__ == "__main__":
    main()