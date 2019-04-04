# Escreva um programa em Python que 
# leia um arquivo texto e apresente na tela o seu conteúdo reverso. 

import os

def create_file():
    name_file = "task4.txt"
    new_file = open(name_file, "w+")
    new_file.write("Bom dia\nVocê pode falar agora?")
    return name_file

def read_file_and_revert(filename):
    data_from_file = []
    if os.path.isfile(filename):
        read_file = open(filename, "r")
        for x in range(1):
            content_file = read_file.read()
            data_from_file.append(content_file)
        for i in data_from_file:
            formated_data = i.splitlines()
            reverted_content = i[-1::-1]
        print(reverted_content)
    else:
        print('Arquivo não existe')

def main():
    filename = create_file()
    read_file_and_revert(filename)

if __name__ == "__main__":
    main()