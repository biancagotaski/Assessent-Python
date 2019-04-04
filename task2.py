import subprocess, os, re

inputUser = input('Qual o nome do arquivo txt a ser criado?\n')

def generate_file_txt():
    name_file = str(inputUser + ".txt")
    new_file = open(name_file, "w+")
    os.startfile(name_file)

generate_file_txt()
    