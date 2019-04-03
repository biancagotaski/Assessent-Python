import psutil, math

def get_current_processes():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid
            print(process_name, ' ::: ', process_id)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("Nao foi possivel encontrar nenhum processo ativo")

def get_percent_cpu_and_memory():
    count = 0
    ##Estou dando um count de 20 pois senão o processo vai ficar correndo eternamente
    while count != 20:
        proc = psutil.Process()
        print('Percentual do uso da CPU:', proc.cpu_percent(interval=1))
        count += 1
    per_memory = psutil.virtual_memory()
    print('\nPercentual de memoria:', per_memory.percent, "%")
    print('Memoria disponivel:', convert_unit_measurement(per_memory.available))
    print('Quantidade de memoria usada:', convert_unit_measurement(per_memory.used))


def convert_unit_measurement(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

get_current_processes()
get_percent_cpu_and_memory()