# Instituto Infnet - Apoio Acadêmico
## 2024.T1

Bem-vindo ao repositório de apoio para os alunos dos cursos de Ciência da Computação, Banco de Dados, Ciência de Dados e afins do Instituto Infnet.

Este repositório foi criado para fornecer recursos adicionais, exemplos de código, tutoriais e materiais de estudo para auxiliar no aprendizado e no desenvolvimento acadêmico dos alunos.

## Conteúdo

- **Recursos**: Links úteis para sites, artigos, vídeos e outras fontes de informação relevantes para os cursos.
  
- **Exemplos de Código**: Exemplos de código em várias linguagens de programação, frameworks e bibliotecas frequentemente utilizadas nos cursos.

- **Tutoriais**: Tutoriais passo a passo para ajudar os alunos a entenderem conceitos complexos e a resolverem problemas comuns.

- **Materiais de Estudo**: Slides de aula, notas de aula, listas de exercícios e outros materiais de estudo fornecidos pelos professores.

- [**Subindo o nível**](docs/avancado/indice.md) : ... 

## Contribuição

Os alunos são incentivados a contribuir para este repositório adicionando recursos, exemplos de código, tutoriais e outros materiais úteis que encontrarem durante seus estudos.

Para contribuir, basta fazer um fork deste repositório, adicionar seus próprios recursos ou materiais e enviar um pull request. Todas as contribuições são bem-vindas!

## 

## Licença

Este repositório é disponibilizado sob a [ Licença GNU ](LICENSE). Sinta-se à vontade para usar, modificar e distribuir os materiais deste repositório conforme desejar.

Professor Fábio Linhares

E-mail:
fabio.slinhares@prof.infnet.edu.br

------------------------------------

# Como começar um projeto Pyton?

## Estrutura Genérica

### Diretórios:
  * Documentacao
  * sources (ou nome do projeto)
  * testes

## Quando utilizar o Ipython?
Pesquisar...

	python -i file.py
    
## Ferramentas

## Pyenv (Gerenciador de versões do Python)

### Instalação

    curl https://pyenv.run | bash

#
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
#
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
#
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc

Mas como uso o bash também, preciso exportar as variáveis para ele:

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#   
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

Reinicie o shell:

    exec "$SHELL"

Atualize-o:

    pyenv update

## Modo de usar

    pyenv install 3.10.4

#
    pyenv shell <version> -- 
select just for current shell session
#

    pyenv local <version> 
-- automatically select whenever you are in the current directory (or its subdirectories)

#
    pyenv global <version> -- select globally for your user account

## Unistall version

    $(pyenv root)/versions

#

    rm -rf pyenv prefixpyenv prefix 2.6.8

# Unistall Pyenv
    rm -rf $(pyenv root)

# Ecossistema Python
Gerenciador de pscotes e ambientes virtuais. (Pacote == módulo). Nada mais é que uma pasta com arquivos dentro. É algo que podemos instalar no python.

## Virtualenv
Um lugar onde instalamos pacotes sem misturá-los com outras. Faz um link simbólico do Python em outra pasta.

### Criação:
    python -m venv nome_do_ambiente

### Ativando o ambiente
    source /path/nome_do_ambiente/bin/activate

### Desativando o ambiente
    deactivate

## Pypi
Índice público de pacotes do Python

## Pip
Ferramenta que pega os pacotes do Pypi e instala-os na máquina. (Virtualenv é opcional, porém recomendado). Desta forma,quando configurado adequadamente, o pip pega o pacote no pypi e utiliza o virtualenv para instála-lo em um ambiente virtual.

### Modo Pythônico ... (antigamente)

    pip -m install nome_do_pacote

ou

    pip install nome_do_módulo
#

Obs.:
-- Para dar um 'build' e criar pacotes precisamos de um arquivo setup.py e do setuptools. A Pypa é a mantenedora desse pacote.

### Exemplo 

*   Diretório: meu_pacote
    *   arquivo: minha_lib.py
        
            def minha_lib():
                print("Pacote Zerocopia")

*   arquivo: setup.py
  
        from setuptools import setup

        setup(
        name='Zero Pacote',
        packages=['meu_pacote']
        )


Exemplo de um arquivo completo:

<p align="center">
  <img src="image.png" alt="Parâmetros do setup" style="max-width: 100%;">
</p>

### Para 'buildar'
    python setup.py build


Gerando um pacote .tar.gz

    python setup.py build sdist

Para instalar basta utilizar o pip

    pip install pacote.tar.gz

#
Poderíamos utiliar o comando
    
    python setup.py install 

para instalar o pacote recém criado no nosso Python global.

Gerando um pacote whell (python3). Primeiro instale o wheel.

    pip -m install whell

Depois gere o pacote

    python setup.py sdist bdist_wheel


## Twine
Publicando o pacote no Pypa. Instale o pacote twine

    pip install twine


Para 'subir' todos os pacotes (*) utilize o comando abaixo e resposta às perguntas... Ao final do processo o pacote estará disponível no Pypa.

    twine upload dist/*


Caso seja preciso 'rebuildar' utilize o comando

    rm -rf dist/

para remover o diretório dist e repita o processo de 'buildar'



## Jeito moderno

## Poetry
Poetry é uma ferramenta para gerenciamento de dependências e empacotamento em Python. Ele permite que você declare as bibliotecas das quais seu projeto depende e irá gerenciá-las (instalar/atualizar) para você. Poetry oferece um arquivo de bloqueio para garantir instalações repetíveis, e pode construir seu projeto para distribuição.

## Instalação
O Poetry deve ser sempre instalado em um ambiente virtual dedicado para isolá-lo do resto do seu sistema. Em hipótese alguma, ele deve ser instalado no ambiente do projeto que será gerenciado. Isso garante que as próprias dependências do Poetry não serão acidentalmente atualizadas ou desinstaladas. 

Linux, macOS, Windows (WSL)

    curl -sSL https://install.python-poetry.org | python3 -


Windows (Powershell)

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -


## Modo de usar

    poetry new nome_do_projeto*

  --> * Nome do projeto, pacote, ambiente..
  O comando acima cria os diretórios do "ambiente" de desenvolvimento. O comando abaixo instala as bibliotecas (de que o projeto depende) em um ambiente virtual (poetry-core, pytest...) e cria o arquivo poetry.lock


Ou podemos fazer com assistência (cria o pyproject.toml e ignora o resto)

    poetry init ou poetry init -n**

#
        poetry install 
#
    poetry show

Exibe as bibioltecas instaladas

## Instalando dependencias com poetry

    poetry add pacote

Baixa, instala e atualiza o arquivo pyproject.toml

## Instalando dependências de desenvolvimento
Pacotes que não devem ser instalados em produção. Não integrarão o 'build'.

    poetry add --dev pacote

## Removendo pacote instalado

    poetry remove pacote

Caso o pacote esteja instalado no ambiente de desenvolvimento:

    poetry remove --dev pacote

## Executando mmódulo

    poetry run module

Outro modo de executar é por meio do shell, que já carrega todo o ambiente.

    poetry shell

## "Buildando" o pacote

    poetry build

## Publicando o pacote
Fazendo upload do pacote para o Pypa.

    poetry publish

## E o requeriments.txt?
Caso seja necessário gerar ou exportar o arquivo de requerimentos basta utilziar

    poetry export > arquivo

Apenas os pacotes e dependeências de produção seráo exportadas. Ou seja, os pacotes dev são desconsiderados.


# Git

    git clone git@github.com:zerodevsystem/infnet.git
#
Crie o arquivo .gitignore e adicione nele os arquivos, diretórios ou extensões que serão ignorados pelo github. Ex.:
* .venv
* .lock
* .etc...
* __pycache__
 
Uma dica útil para saber que diretórios, arquivos ou extensões ignorar acess:
    
    http://www.gitignore.io

#
    git add .
#
    git status
#
    git commit -m "Estrutura inicial do projeto"
#
    git push

# Github
Depois de criar seu repositório você vai começar a desenvolver e, em algum momento, vai querer subir (enviar) seus arquivos para o github. Para fazer 'push' você - desde 2024 - precisará utiliazar autenticação ssh. 

Para saber se suas configurações de acesso estão corretas tente se conectar por meio deste comando:

    $ ssh -T git@github.com

Caso sua chave SSH estaja cadastrada no github, a senha definida no momento da geração da chave será solicitada. Caso você visualize a mensagem abaixo, certamente tudo estará pronto.

    Attempt to SSH in to github
    Hi USERNAME! You've successfully authenticated, but GitHub does not provide
    shell access.

Caso não visualize, teremos que configurar. Vamos lá:

Abra Terminal e insira o comando abaixo para ver se as chaves SSH existentes estão presentes.

    $ ls -al ~/.ssh

Verifique se algum arquivo destes existe:

* id_rsa.pub
* id_ecdsa.pub
* id_ed25519.pub
  
Caso existam você já tem chave SSH. Basta configurá-la. Caso não existam, cole o texto abaixo, substituindo o email usado no exemplo pelo seu endereço de email GitHub.

    ssh-keygen -t ed25519 -C "your_email@example.com"

Observação: caso esteja usando um sistema herdado que não dá suporte ao algoritmo Ed25519, use:
    
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

Pressione enter quando esta mensagem aparecer:
    
    Enter a file in which to save the key (/home/YOU/.ssh/id_ALGORITHM):[Press enter]

Defina uma senha e depois repita-a quando solicitado. Depois disso, basta adicionar sua chave ao github. Para tanto, copie-a por meio deste comando:

    cat ~/.ssh/id_ed25519.pub

Agora acesse sua conta do github, clique em configurações e na seção "Acesso" da barra lateral, clique em  Chaves SSH e GPG. Clique em Nova chave SSH ou Adicionar chave SSH. No campo "Title" (Título), adicione uma etiqueta descritiva para a nova chave. Por exemplo, se estiver usando um laptop pessoal, você poderá chamar essa chave de "Laptop pessoal". Selecione o tipo de chave: autenticação ou assinatura. Recomendo a opção GNU e no campo "Chave", cole sua chave pública. Aquela que acabamos de copiar. Clique em Adicionar chave SSH e, se solicitado, confirme acesso à sua conta em GitHub.

Pronto. Sua chave SSH foi criada, configurada e adicionada ao github. Podes começar a 'codar'. Mas lembre-se. Ao utilizar o comando git push será solicitado uma senha. A senha em questão é a que você definiu ao criar a chave SSH.

# Dicas

## Pipx
Pipx é uma ferramenta para ajudá-lo a instalar e executar aplicativos de usuário final escritos em Python em ambientes isolados. Está intimamente relacionado com o pip. Na verdade, ele usa pip, mas é focado em instalar e gerenciar pacotes Python que podem ser executados a partir da linha de comando diretamente como aplicativos.

## Instalação

    sudo pacman -S python-pipx
    pipx ensurepath

## Modo de usar

    pipx install PACKAGE

## Desinstalar bibliotecas
Método tradicional:
    
    pip unistall biblioteca 
#
Método recomendado:

    pip-autoremove biblioteca

## Listar dependências de pacotes
    pipdeptree

## Criar arquivo de requerimentos (requirements.txt)
    pip freeze > requiriments.txt

### Formatação do arquivo:

    pacote==versão
    pacote>=versão
    pacote!=versão (diferente)
    pacote~=versão (só atualiza dentro da versão maior, ex.: 1.0.1, 1.2, 1.9... ----> inferior a 2.x

## Instalar as bibliotecas necessárias
    pip install -r requirements.txt

## Instalar blibliotecas de desenvolvimento (requirements_dev.txt)
Obs: o arquivo tem a mesma formatação do requirements.txt
    -r requirements.txt

## Constraints
Trava uma biblioteca específica. Tem a mesma formatação do requirements.txt

    pacote==versão

Atenção para o uso do '=='


### Modo de usar
    
    pip install -r requirements.txt -c constraints.txt



# Referências:

[1] https://github.com/pyenv/pyenv?tab=readme-ov-file#installation

[2] https://github.com/pyenv/pyenv-installer?tab=readme-ov-file

[3] https://python-poetry.org/docs/

[4] https://python-poetry.org/docs/cli/

[5] https://github.com/pypa/pipx

[6] https://pipx.pypa.io/stable/installation/

[7] https://docs.github.com/pt/authentication/connecting-to-github-with-ssh

<p align="center">
  <img src="image-1.png" alt="Parâmetros do setup" style="max-width: 100%;">
</p>
