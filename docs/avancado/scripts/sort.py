def ordenacao(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Adicionando o conteúdo do arquivo em uma lista
file_lista = []
with open('zero_lista', 'r') as file:
    for line in file:
        file_lista.append(line.strip())

# Ordenando a lista
ordenacao(file_lista)

# Imprimindo a lista de arquivos ordenada
for file in file_lista:
    print(file)
