# Dado um vetor A de tamanho N com apenas números inteiros positivos, 
# calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
# Desenvolva o programa sequencialmente (sem concorrência)

import time, psutil

vector_a = []

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def main():
  input_value = int(input('Insira o tamanho do array desejado: '))
  for i in range(input_value):
      vector_a.append(20)

def calcula_fatorial_do_vetor():
  vector_b = []
  for i in vector_a:
      result = fatorial(i)
      vector_b.append(result)

def get_core_cpu():
  core_cpu = psutil.cpu_count()
  return core_cpu

if __name__ == "__main__":
  main()
  tempo_inicial = float(time.time())
  calcula_fatorial_do_vetor()
  tempo_final = float(time.time())
  tempo_total = tempo_final - tempo_inicial
  print('O tempo total de execução foi:', tempo_total)
  print('\nO número de cores do meu processador é:', get_core_cpu())

  
