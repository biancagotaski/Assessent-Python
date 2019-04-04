# Escreva um programa que obtenha um nome de um arquivo texto 
# do usuário e crie um processo para executar o programa do
# sistema Windows bloco de notas (notepad) para abrir o arquivo.

import subprocess, os, re

inputUser = input('Qual o nome do arquivo txt a ser criado?\n')

def generate_file_txt():
    name_file = str(inputUser + ".txt")
    new_file = open(name_file, "w+")
    os.startfile(name_file)

generate_file_txt()