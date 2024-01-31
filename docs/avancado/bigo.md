# Notação Big O

A notação Big O, também conhecida como "O grande O", é uma notação utilizada em Ciência da Computação para descrever o desempenho ou complexidade de algoritmos. Ela fornece uma forma de classificar o crescimento do tempo de execução ou uso de recursos (como memória) de um algoritmo à medida que o tamanho da entrada aumenta.

Em termos simples, a notação Big O descreve (ou tenta determinar) o limite superior (máximo) do tempo de execução de um algoritmo em relação ao tamanho de sua entrada, em uma escala assintótica. Isso significa que o Big O não descreve o tempo exato de execução de um algoritmo para uma entrada específica, mas sim como o tempo de execução cresce à medida que a entrada aumenta em tamanho.

Sugestão: pense assim, o Big O é mais ou menos como uma regra de três. Se para uma entrada de dados de tamanho [2] o tempo máximo é [X], para uma entrada de tamanho [M] o tempo máximo será [Y]. Sacou? Não é isso, ou só isso. Tem o lance das notaçõees... bem interessantes, mas a parada da regra de trÊs ajuda a começar a entender. Continue a leitura que você vai perceber.

De modo mais técnico, a notação [Big O´] é frequentemente usada para comparar a eficiência de diferentes algoritmos e para prever como o desempenho de um algoritmo será afetado ao lidar com entradas de tamanhos variados. Além disso, ela fornece uma maneira de analisar a escalabilidade de um algoritmo, ou seja, como o desempenho do algoritmo se comporta quando o tamanho da entrada aumenta para tamanhos muito grandes.

Existem várias classes comuns de complexidade representadas pela notação Big O, como:

- O(1): Tempo de execução constante, independente do tamanho da entrada.

- O(log n): Tempo de execução cresce logaritmicamente com o tamanho da entrada.

- O(n): Tempo de execução cresce linearmente com o tamanho da entrada.

- O(n^2): Tempo de execução cresce quadráticamente com o tamanho da entrada.

- O(2^n): Tempo de execução cresce exponencialmente com o tamanho da entrada.

Esses são apenas alguns exemplos, e existem muitas outras classes de complexidade que podem ser expressas usando a notação Big O. Esta notação é uma ferramenta essencial para análise e projeto de algoritmos, ajudando os desenvolvedores a entender e comparar o desempenho relativo de diferentes abordagens algorítmicas.

a lógica é mais ou menos esta: um algoritmo com uma notação Big O de O(n) sugere que seu tempo de execução cresce linearmente, conforme o tamanho da entrada (n). Se o tamanho da entrada dobrar, o tempo de execução do algoritmo também dobrará. Sacou?

Tudo facinho até aqui, não é? Contudo, se você não é muito fã de matemática pode não lembrar ou não entender alguams paradas. WTF é "crescimento logarítmico? Pois é. Vamos lá!

Um crescimento logarítmico significa que o tempo de execução do algoritmo aumenta de forma proporcional ao logaritmo do tamanho da entrada. Isso implica que, à medida que o tamanho da entrada aumenta, o tempo de execução do algoritmo aumenta, mas em uma taxa muito mais lenta do que o tamanho da entrada em si. Sacou?

Um dos melhores exemplos disso é a busca binária. Como assim, busca binária? Aquela em que vamos dividindo por dois, dopois por dois de novo, e assim por diante. Olhe só: na busca binária a lista de elementos é dividida ao meio repetidamente até encontrar o elemento desejado. Não é? Então, esse processo de divisão pela metade reduz drasticamente o número de elementos a serem considerados a cada iteração. Logo, a quantidade máxima de iterações é definida pela função log₂[qtd_elementos] = X.

Saca só:

- Para 16 elementos: o número máximo de iterações necessárias para encontrar um elemento na busca binária é aproximadamente log₂16, ou seja = 4.

        2 x 2 x 2 x 2 -------> 4 passos

- Para 32 elementos: o número máximo de iterações necessárias seria aproximadamente log₂32, ou seja, 5.

        2 x 2 x 2 x 2 x 2 ---> 5 passos

Isso ocorre porque a lista sempre é dividida ao meio sucessivamente até restar apenas um elemento. Não por outra razão esse tipo de busca, ou no caso, do algorítimos, essa "complexidade": [O(log n)] é considerado muito eficiente e é frequentemente encontrado em algoritmos como a busca binária, árvores de busca binária balanceadas e em certas operações em estruturas de dados como heaps e árvores B.
