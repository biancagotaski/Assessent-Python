import os

a = "a.txt"
b = "b.txt"

def create_new_file(filename_a, filename_b):
    file_a = open(filename_a, "w+")
    file_a.write("1 15 -42 33 -7 -2 39 8")

    file_b = open(filename_b, "w+")
    file_b.write("19 56 -43 23 -7 -11 33 21 61 9")

def sum_elements_from_file():
    if os.path.isfile(a) and os.path.isfile(b):
        read_file_a = open(a, "r")
        read_file_b = open(b, "r")
        ##colocar o conteúdo dentro de um array
        ##comparar item a item do array A com o array B e fazer o somatório
        data_a = read_file_a.read().split()
        data_b = read_file_b.read().split()
        # print(data_a, '\n', data_b)
        for i in range(len(data_a)):
            print(int(data_a[i]) + int(data_b[i]))
    else:
        print('O arquivo não existe')

if __name__ == "__main__":
    create_new_file(a, b)
    sum_elements_from_file()