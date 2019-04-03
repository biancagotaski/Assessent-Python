import subprocess, os, re

inputUser = input('Informe o nome do arquivo txt que deseja abrir:\n')

formatedInput = re.sub(r'(\\)', r'\\\\', inputUser)
get_complete_path = os.path.abspath(formatedInput)
get_formated_complete_path = re.sub(r'(\\)', r'\\\\', get_complete_path)
if os.path.exists(get_formated_complete_path):
    # print(get_formated_complete_path)
    subprocess.call(['cmd.exe', '/c', get_formated_complete_path])
else:
    print('Arquivo informado não encontrado.')