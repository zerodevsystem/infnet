# Ordenando uma lista oriunda de uma arquivo.
Se você caiu aqui de paraquedas, no item [**Linuxando**](linux.md) vimos algumas formas de ordenar arquivos no terminal do GNU-Linux. Em praticamente todas elas podemos utilizar um [[ > ]] direcionador para colocar o conteúdo da ordenação em um arquivo. É este o lançe: você já ordenou (ou não) os arquivos de um diretório e criou um arquivo de texto com o conteúdo.

Vamos imaginar o seguinte conteúdo no arquivo chamado zero_lista:

```bash
$ cat zero_lista
```
    01:46.933145110 -0300 ./zero_lista\
    17:29.021949510 -0300 ./Untitled.ipynb\
    21:06.353993715 -0300 ./Aula Numpy 02 - Verificando propriedades dos arrays.ipynb\
    19:11.704032451 -0300 ./Aula Numpy 01 - Criação arrays NumPy.ipynb\
    01:00.624023820 -0300 ./Aula Conjuntos.ipynb\
    00:58.374023883 -0300 ./Aula Dicionários.ipynb\
    00:57.854023897 -0300 ./Aula for.ipynb\
    00:57.274023914 -0300 ./Aula for_.ipynb\
    00:56.794023927 -0300 ./Aula funções.ipynb\
    00:56.284023941 -0300 ./Aula funções-1.ipynb\
    00:55.734023956 -0300 ./Aula lambda.ipynb\
    00:55.154023972 -0300 ./Aula lambda-1.ipynb\
    00:54.494023991 -0300 ./Aula Listas.ipynb\
    00:53.584024013 -0300 ./Aula map(), reduce(), filter(), zip().ipynb\
    00:52.384024043 -0300 ./Aula map(), reduce(), filter(), zip()-1.ipynb\
    00:43.394024352 -0300 ./Aula Tuplas.ipynb\
    00:42.504024401 -0300 ./Cálculo IMC 2.ipynb\
    00:41.544024454 -0300 ./Aula while.ipynb\
    00:40.204024528 -0300 ./Cálculo IMC.ipynb\
    00:39.574024562 -0300 ./Estrutura condicional - if.ipynb\
    00:38.964024596 -0300 ./Introd Python.pdf\
    00:37.314024715 -0300 ./Operadores.ipynb\
    00:34.874024921 -0300 ./Strings.ipynb\
    00:33.314025052 -0300 ./Tabelas verdade.ipynb\
    00:30.454025292 -0300 ./Tipos de dados no Python.ipynb\
    00:29.124025376 -0300 ./Triângulos.ipynb\
    00:28.284025426 -0300 ./UNIDADE 1.pdf\

Suponha que seja necessário ordenar esses nomes de arquivos. Como fazer isso com Python? Qeue tal assim: vamos criar uma aquivo chamado sort.py e colocar o contúdo abaixo nele.

```python

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
        file_list.append(line.strip())

# Ordenando a lista
ordenacao(file_lista)

# Imprimindo a lista de arquivos ordenada
for file in file_lista:
    print(file)


```

Ao executarmos o código acima:

```shell
    python -i sort.py
```

    00:28.284025426 -0300 ./UNIDADE 1.pdf
    00:29.124025376 -0300 ./Triângulos.ipynb
    00:30.454025292 -0300 ./Tipos de dados no Python.ipynb
    00:33.314025052 -0300 ./Tabelas verdade.ipynb
    00:34.874024921 -0300 ./Strings.ipynb
    00:37.314024715 -0300 ./Operadores.ipynb
    00:38.964024596 -0300 ./Introd Python.pdf
    00:39.574024562 -0300 ./Estrutura condicional - if.ipynb
    00:40.204024528 -0300 ./Cálculo IMC.ipynb
    00:41.544024454 -0300 ./Aula while.ipynb
    00:42.504024401 -0300 ./Cálculo IMC 2.ipynb
    00:43.394024352 -0300 ./Aula Tuplas.ipynb
    00:52.384024043 -0300 ./Aula map(), reduce(), filter(), zip()-1.ipynb
    00:53.584024013 -0300 ./Aula map(), reduce(), filter(), zip().ipynb
    00:54.494023991 -0300 ./Aula Listas.ipynb
    00:55.154023972 -0300 ./Aula lambda-1.ipynb
    00:55.734023956 -0300 ./Aula lambda.ipynb
    00:56.284023941 -0300 ./Aula funções-1.ipynb
    00:56.794023927 -0300 ./Aula funções.ipynb
    00:57.274023914 -0300 ./Aula for_.ipynb
    00:57.854023897 -0300 ./Aula for.ipynb
    00:58.374023883 -0300 ./Aula Dicionários.ipynb
    01:00.624023820 -0300 ./Aula Conjuntos.ipynb
    01:46.933145110 -0300 ./zero_lista
    17:29.021949510 -0300 ./Untitled.ipynb
    19:11.704032451 -0300 ./Aula Numpy 01 - Criação arrays NumPy.ipynb
    21:06.353993715 -0300 ./Aula Numpy 02 - Verificando propriedades dos arrays.ipynb
>>>
