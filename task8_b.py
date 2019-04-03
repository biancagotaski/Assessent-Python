import time, threading, psutil

vector_a = []
vector_b = []

def main():
    input_value = int(input('Insira o tamanho do array desejado: '))
    for i in range(input_value):
        vector_a.append(20)

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def calcula_fatorial_do_vetor(vector_a):
    for i in vector_a:
        result = fatorial(i)
        vector_b.append(result)

def get_core_cpu():
  core_cpu = psutil.cpu_count()
  return core_cpu

if __name__ == "__main__":
    main()
    qtd_threads = 4
    tamanho = len(vector_a)
    threads = []
    resultado = []
    inicio_tempo = float(time.time())
    for i in range(qtd_threads):
        inicio = i*int(tamanho//qtd_threads)
        fim = (i+1)*int(tamanho//qtd_threads)
        ##passar a virgula junto com o primeiro argumento do parametro para o python reconhecer que é uma tupla
        t = threading.Thread(target=calcula_fatorial_do_vetor, args=(vector_a[inicio:fim], ))
        threads.append(t)
        t.start()
        resultado.append(t)
    for t in resultado:
        t.join()
    fim_tempo = float(time.time())
    tempo_total = fim_tempo - inicio_tempo
    print('O tempo total de execução foi:', tempo_total)
    print('\nO número de cores do meu processador é:', get_core_cpu())