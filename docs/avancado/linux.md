# Um pouquinho de super poder

## Operações com arquivos

### Criando arquivo com a listagem de um diretório:

    ls > file

### Ordenando a listagem
Ordem Alfabética (padrão):

    ls

Ordem Alfabética Reversa:

    ls -r

Por Data de Modificação (do mais antigo para o mais recente):

    ls -t

Por Data de Modificação (do mais recente para o mais antigo):

    ls -tr

Por Tamanho do Arquivo (do menor para o maior):

    ls -S

Por Tamanho do Arquivo (do maior para o menor):

    ls -rS

Por Ordem Cronológica (da data de criação):

Bah! Depende do sistema de arquivos e da configuração do sistema operacional. O Linux não tem uma opção padrão para isso no comando ls, mas podemos improvisar combinando comandos. Vou mostrar abaixo, mas vamos precisar fazer uma pequena tangente. Depois retomamos.

    stat --format '%Y :%y %n' * | sort -nr | cut -d: -f2- | less

Essa combinação de comandos lista todos os arquivos no diretório atual, ordena os arquivos por hora de modificação em ordem decrescente e exibe a saída em páginas usando o comando less. Isso permite visualizar os arquivos no diretório ordenados por data de criação. Caso prefira salvar a lista em um arquivo:

    stat --format '%Y :%y %n' * | sort -nr | cut -d: -f2- > file

Éh!... não é simples como um ls, mas vamos tentar entende o que e como a combinação acima funciona. Vamos por partes:

- stat --format '%Y :%y %n' *:
    - [[ stat ]] exibir informações detalhadas sobre arquivos e sistemas de arquivos.
    - [[ --format '%Y :%y %n' ]] especifica o formato de saída para o comando stat. 
        - [[ %Y ]] representa a hora de modificação (em segundos desde o Unix Epoch), 
        - [[ %y ]] representa a hora de modificação no formato padrão e 
        - [[ %n ]] representa o nome do arquivo. 
        
        Tá complexo: a ideia é que combinar as horas de modificação com o nome do arquivo, separados por : e processar depios. Só isso.

- [[ * ]] é um padrão de correspondência de shell para todos os arquivos no diretório atual. Ele é usado para garantir que o stat seja aplicado a todos os arquivos no diretório atual.

- [[ | sort -nr ]]
    - [[ | ]] o pipe encaminha a saída do comando anterior para a entrada do próximo comando.
    - [[ sort ]] classifica linhas de texto em ordem alfabética ou numérica.
        - [[-nr ]] 
            - [[ -n ]] indica classificação numérica e 
            - [[-r ]] indica classificação reversa, ou seja, do maior para o menor.
- [[ | cut -d: -f2- ]]
    - [[ | ]] pipe novamente, para empurra a saída dos comandos aciama para o cut.
    - [[ cut ]] é usado para dividir cada linha de entrada em campos e selecionar apenas os campos desejados.
        - [[ -d: ]] especifica o delimitador a ser usado, que é  [[ : ]].
        - [[ -f2- ]] indica que queremos selecionar todos os campos a partir do segundo campo até o final da linha. Isso remove o campo de tempo de modificação em segundos, deixando apenas a hora de modificação padrão e o nome do arquivo.
- [[ | less ]]
    - [[ | ]] Mais um pip, mas agora você já sabe para quê.
    - [[ less ]] usado para mostrar a saída em páginas, permitindo rolar para cima e para baixo na saída, facilitando a visualização de grandes conjuntos de dados.

E o [[ > file ]] do comando anterior?

- [[ > ]] é um direcionador. É bem isso que você pensou. Direciona tudo o que vem antes dele para algum lugar. No caso:
- [[ file ]] o arquivo desejado. Caso o arquivo não exista ele cria. Se existir, a opção [[ > ]] sobrescreve seu conteúdo. Caso queiramos adiconar, o correto é utilizar assim: [[ >> ]].

Bah...Entendi, mas não tem outro jeito, tipo um clique e pronto? Até tem, mas somente se você utiliza GUI, o que não é o nosso caso. Mas não tem fórmula pronta não. Existem outras formas de fazer o fizemos acima, por exemplo:

    find . -type f -print0 | xargs -0 stat --format '%y %n' | sort -nr | cut -d: -f2- | less

Ainda está complicado? Dê uma examinada nos manuais de Linux que você vai encontrar outras forma de fazer isso, com certeza. Daí é só eleger uma preferida e pronto. Para mim, por exemplo, a primeira é mais interessante, ainda mais porque utilizo um álias, lst, o que facilita muito a minha vida.

    alias lst="stat --format '%Y :%y %n' * | sort -nr | cut -d: -f2- | less"

Logo, quando quero litar arquvios por data de criação eu só digito `lst`. Show, mas vamos voltar para o assunto principal: a ordenação a listagem.

Por Ordem Alfabética, Ignorando Caixa Alta/Baixa:

    ls -f

Mostrar Detalhes (incluindo permissões, proprietário, tamanho, etc.):

    ls -l

Mostrar Detalhes e Ordenar por Data de Modificação (do mais recente para o mais antigo):

    ls -lt

Mostrar Detalhes e Ordenar por Data de Modificação (do mais antigo para o mais recente):

    ls -ltr



