=========
Tutoriais
=========

.. contents::
   :depth: 1
   :local:
   :backlinks: none

.. highlight:: console

Visão geral
-----------

Exemplos de tutoriais tanto para nível de usuário final 
quanto para o desenvolvimento.

Exemplos
--------

Alguns exemplos de tutoriais que podem ser criados para o projeto:

- Obtenção dos dados
- Instalação
- Pré-processamento
- Processamento
- Casos de uso
- Pós-processamento
- Visualização
- Geração de relatórios
- Sintaxes para documentação

Abaixo estão alguns tutoriais de como documentar seu projeto:

- Criando arquivos :doc:`Markdown <markdown-cheat-sheet>`
- Criando arquivos `reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
- Documentando algoritmos em Python com **docstring**
- Importando esta documentação no seu projeto

Obtenção dos dados
^^^^^^^^^^^^^^^^^^

* ``make sync_data_to_s3`` usará ``aws s3 sync`` para, recursivamente, sincronizar os arquivos de ``data/`` para ``s3://sta/data/``.
* ``make sync_data_from_s3`` usará ``aws s3 sync`` para, recursivamente, sincronizar os arquivos de ``s3://sta/data/`` para ``data/``.