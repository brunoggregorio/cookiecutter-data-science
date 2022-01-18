# Cookiecutter Data Science - Template

_Estrutura de projeto template para Data Science - Python. Baseado no [template cookiecutter](http://drivendata.github.io/cookiecutter-data-science/)_.

---

## Dependências

 - Python 2.7 ou 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: Pode ser instalado via ``pip`` ou ``conda``, dependendo de como você administra seus pacotes Python:

``` bash
$ pip install cookiecutter
```

ou

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

---

## Utilização

Para iniciar um projeto de **Data Science - Python** utilizando o template, basta executar o seguinte comando e seguir preenchendo os dados no prompt:

```bash
$ cookiecutter -c master https://gitlab.spacetimeanalytics.com/sta/cookiecutter-data-science
```

### Estrutura de diretórios

A estrutura de diretórios criada no novo projeto terá o seguinte formato:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Sphinx project template; see http://sta.spacetimedocs.com/doc-template-sphinx for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1_bg_initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in the project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   ├── utils          <- Scripts to facilitate the manipulation of objects in the project
│   │   └── utils.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- Tox file with settings for running tox; see tox.readthedocs.io
```

### Documentação

O template de documentação sugerido para projetos de data science da STL também já é carregado e configurado automaticamente. Para mais detalhes de como editar tais documentos, veja o [Template Sphinx](http://sta.spacetimedocs.com/doc-template-sphinx/).

Para fazer o build local da documentação em html basta executar o comando:

```bash
$ make docs
```

A estruturação do diretório **docs** é a seguinte:

```
└── docs                      <- Pasta com a documentação
    ├── Makefile              <- Makefile para criação da documentação
    ├── make.bat              <- Makefile para criação da documentação em Windows
    ├── requirements-doc.txt  <- Arquivo com os requisitos da documentação
    ├── _build                <- Destino dos arquivos criados na documentação
    └── source                <- Arquivos de origem para documentação
        ├── api               <- Documentação da API (automático)
        ├── dev               <- Documentação do projeto
        ├── tutorials         <- Tutoriais do projeto
        ├── _images           <- Imagens utilizadas na documentação
        ├── _static           <- Arquivos estáticos para documentação
        ├── conf.py           <- Arquivo de configuração da documentação
        ├── index.rst         <- Arquivo inicial da documentação
        └── .build_docs.sh    <- Script bash para geração da documentação
```

### Notebooks são para exploração e comunicação

Pacotes de Notebook como [Jupyter notebook](http://jupyter.org/), [Beaker notebook](http://beakernotebook.com/), [Zeppelin](http://zeppelin-project.org/) e outros são efetivos na análise
exploratória de dados. Entretanto, essas ferramentas podem ser menos efetivas na reprodução de
uma análise. Quando usamos notebooks em nossos projetos, geralmente subdividimos o diretório
`notebooks`. Por exemplo, `notebooks/exploratory` contém as análises exploratórias iniciais,
enquanto `notebooks/reports` é para trabalhos mais refinados que podem ser exportados como
html para o diretório `reports`.

Uma vez que notebooks são objetos desafiadores para softwares de controle de versão (ex: `diffs`
de `json` são frequentemente ilegíveis e realizar o merge torna-se um trabalho complicado), 
recomendamos não utilizá-los em colaboração direta com outros membros. Sugerimos seguir alguns
passos na utilização de notebooks:

1. Siga uma convenção de nomenclatura que mostre o autor e a ordem em que a análise foi realizada.
   Ex: `<step>_<user>_<description>.ipynb` (e.g., `3_user_visualize-distributions.ipynb`).

2. Refatore as partes boas. Não escreva código para a mesma tarefa em múltiplos notebooks. Se é
uma tarefa de pré-processamento dos dados, coloque-o em um pipeline em `src/data/make_dataset.py`
e leia os dados a partir do `data/interim`, por exemplo. Ou seja, se é um código útil, refatore-o
para o diretório source do projeto.

3. Você pode também tornar seu projeto um pacote Python (veja o arquivo `setup.py`) e importá-lo
em seus notebooks:

```
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```

### Salve informações sensíveis e variáveis de configuração em um arquivo especial

O arquivo `.env` criado no diretório raiz do template pode ser usado para salvar informações sensíveis
ou variáveis de configuração local. Graças ao `.gitignore`, esse arquivo nunca será commitado no repositório
do GitLab. Exemplo:

```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```

#### Use um pacote para carregar essas variáveis automaticamente

Se você olhar o script em `src/data/make_dataset.py`, verá que ele utiliza um pacote chamado
[python-dotenv](https://github.com/theskumar/python-dotenv) para carregar todas as entradas do arquivo
`.env` como variáveis de ambiente, podendo assim acessá-las através do `os.environ.get`. Aqui está o
trecho de um exemplo adaptado da documentação do `python-dotenv`:

```python
# src/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")
```

### Configuração AWS CLI

Quando buckets S3 são usados no armazenamento dos dados, um método simples para o gerenciamento de acessos
AWS é setar suas chaves de acesso em variáveis ambiente. Entretanto, para gerenciar múltiplas chaves em uma
única máquina (quando trabalhando em vários projetos, por exemplo), o melhor a se fazer é criar um 
[arquivo de credenciais](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html), tipicamente
localizado em `~/.aws/credentials`. Tal arquivo pode ter a seguinte aparência:

```
[default]
aws_access_key_id=myaccesskey
aws_secret_access_key=mysecretkey

[another_project]
aws_access_key_id=myprojectaccesskey
aws_secret_access_key=myprojectsecretkey
```

Você pode definir o nome do perfil a ser utilizado ao inicializar o projeto com o comando `cookiecutter`.
Assumindo que nenhuma variável ambiente foi definida, as credenciais de perfil utilizadas serão as _default_.

### Atualização de versões

Este template já vem configurado com o pacote [bump2version](https://github.com/c4urself/bump2version)
para realizar a atualização de versões do seu projeto em apenas um comando.

Ao executar o comando `make release`, o pacote é acionado e realizará os seguintes passos:

- Atualização de todas as tags de versão do projeto (definidas no arquivo de configuração)
- Faz o commit das alterações
- Cria um tag da versão alterada

A definição das tags de versão, assim como outras configurações do pacote podem ser editadas no arquivo
`.bumpversion.cfg` criado pelo template. Para mais detalhes e opções de configuração avançadas, veja
a [documentação](https://github.com/c4urself/bump2version) do projeto.

---

## Contribuições

Toda contribuição é bem-vinda! Veja a [documentação](http://drivendata.github.io/cookiecutter-data-science/) para instruções mais detalhadas.

### Dependências para desenvolvimento

```bash
$ pip install -r requirements.txt
```

### Executando os testes

```bash
$ py.test tests
```