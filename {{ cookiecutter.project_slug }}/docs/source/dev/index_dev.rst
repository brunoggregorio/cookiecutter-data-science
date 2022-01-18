=================
Manual do projeto
=================

.. contents::
   :depth: 1
   :local:
   :backlinks: none

.. highlight:: console

Visão geral
-----------

A ideia aqui é criar um README detalhado do projeto.
Exemplos/sugestões do que documentar podem ser vistos nas seções abaixo.
Nos casos em que uma seção fique muito extensa é possível criar um 
documento à parte (``.rst`` ou ``.md``), acrescentá-lo à pasta ``docs/source/dev`` 
e referenciá-lo aqui.

----

Organização das pastas
----------------------

Descrever a organização do projeto em termos de arquivos e pastas.
Uma forma simples de obter essa informação no Linux é rodar o 
comando `tree`.

::

   $ sudo apt-get install tree
   $ tree

Exemplo de saída com breve descrição:

::

   ├── docs                      <- Pasta com a documentação
   │   ├── Makefile              <- Makefile para criação da documentação
   │   ├── requirements-doc.txt  <- Arquivo com os requisitos da documentação
   │   ├── build                 <- Destino dos arquivos criados na documentação
   │   └── source                <- Arquivos de origem para documentação
   │       ├── api               <- Documentação da API (automático)
   │       ├── dev               <- Documentação do projeto
   │       ├── tutorials         <- Tutoriais do projeto
   │       ├── _images           <- Imagens utilizadas na documentação
   │       ├── _static           <- Arquivos estáticos para documentação
   │       ├── conf.py           <- Arquivo de configuração da documentação
   │       └── index.rst         <- Arquivo inicial da documentação
   ├── notebooks                 <- Pasta com notebooks
   │   └── example.ipynb         <- Exemplo de um notebook jupyter
   ├── README.md                 <- Readme do projeto (enxuto)
   ├── requirements.txt          <- Arquivos com requisitos do projeto
   └── src                       <- Diretório com código source do projeto
      ├── model                  <- Exemplo de diretório
      ├── utils                  <- Exemplo de diretório
      └── example.py             <- Exemplo de arquivo de código


Dados
-----

Descrever onde e como os dados podem ser obtidos, se necessário.
Por exemplo, se os dados para o desenvolvimento estão armazenados 
em buckets no S3:

Os dados podem ser encontrados no `S3 <link>`_ e podem ser baixados da seguinte forma:

::

   $ aws s3 sync https://...

Metodologia
-----------

Se o projeto possuir uma metodologia bem definida que valha a pena
ser detalhada, você pode descrevê-la aqui.

Exemplos:

- Diagramas de fluxo
- Técnicas computacionais
- Métodos matemáticos
- Papers e/ou livros importantes
- Outras tecnologias empregadas no projeto

Pré-requisitos
--------------

Descrever todos os pré-requisitos para o desenvolvimento do projeto.

::

   $ pip install -r requirements.txt

Instalação
----------

Descrever como deve ser feita a instalação, se necessário.
Exemplos a seguir.

Instalação a partir do source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Você pode instalar o pacote diretamente clonando o repositório `Git repository`__.
Isso pode ser feito clonando o repositório e instalando a partir do clone local, ou
simplesmente instalando diretamente via :command:`git`.

::

   $ git clone https://github.com/package-doc/package
   $ cd package
   $ pip install .

::

   $ pip install git+https://github.com/package-doc/package

Você pode também baixar um snapshot do repositório Git nos formatos `tar.gz`__ ou
`zip`__. Uma vez baixados e extraídos, eles podem ser instalados com o comando
:command:`pip` como citado acima.

.. highlight:: default

__ https://github.com/package-doc/package
__ https://github.com/package-doc/package/archive/master.tar.gz
__ https://github.com/package-doc/package/archive/master.zip

Debian/Ubuntu
~~~~~~~~~~~~~

Instalar ``python3-package`` usando :command:`apt-get`:

::

   $ apt-get install python3-package

Se o Python não estiver instalado, isso o instalará para você.

RHEL, CentOS
~~~~~~~~~~~~

Instalar ``python3-package`` usando :command:`yum`:

::

   $ yum install python-package

Se o Python não estiver instalado, isso o instalará para você.

Outras distribuições
~~~~~~~~~~~~~~~~~~~~

Descrição do passo a passo.

Configurações
-------------

Descrever possíveis configurações de uso/desenvolvimento.
Como exemplo, temos a configuração de diversos parâmetros de entrada,
processamento e/ou saída de um modelo.

Primeiros passos
----------------

Descrever os primeiros passos para o início do desenvolvimento, se necessário.

Casos de uso
------------

Descrever casos de uso, se necessário.