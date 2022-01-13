{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Organização do projeto
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── utils          <- Scripts to facilitate the manipulation of objects in the project
    │   │   └── utils.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Template de projeto baseado no <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science</a>. #cookiecutterdatascience</small></p>


Documentação do projeto
-----------------------

1. Edite as variáveis e links no arquivo de configuração `docs/source/conf.py`
    de acordo com o projeto
2. Escreva sua documentação em arquivos **markdown** (`.md`) ou 
    **reStructuredText** (`.rst`) em `docs/source/`
3. Para executar localmente, instale as dependências em seu ambiente virtual 
    rodando, por exemplo: `pip install -r docs/requirements_doc.txt`  
    3.1. Execute os scripts para geração da documentação utilizando os comandos
    do `Makefile` disponíveis dentro do diretório `docs`, como: `make html`
    3.2. O HTML gerado pode ser conferido em `docs/build/html/index.html`  
    3.3. Se tudo estiver ok, limpe o diretório *build* criado com `make clean`
4. Verifique se o arquivo `.gitlab-ci.yml` está na raiz do seu projeto e se ele
    possui os passos necessários para a geração da documentação no CI-CD do GitLab
5. Done! A cada **commit** realizado na *branch* configurada em `.gitlab-ci.yml`
    sua documentação será atualizada
6. Confira a documentação criada na página do projeto (`Settings -> Pages`).
    Ela provavelmente estará sob o domínio **http://sta.spacetimedocs.com/{{ cookiecutter.project_name.lower().replace(' ', '_') }}**.