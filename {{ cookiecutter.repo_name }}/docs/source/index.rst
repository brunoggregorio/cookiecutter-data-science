.. Doc-Tutorial documentation master file, created by
   sphinx-quickstart on Fri Jul 10 14:04:49 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ cookiecutter.project_name }}
==============================

.. image:: _images/banner.png
   :align: center
   :width: 100%
   :alt: alternate text

{{ cookiecutter.project_description }}

Link para o código: `{{ cookiecutter.project_name }} <https://gitlab.spacetimeanalytics.com/sta/{{ cookiecutter.project_name.lower().replace(' ', '_') }}>`_.

.. note::
   Este documento é apenas um template. Os conteúdos aqui sugeridos não
   precisam ser necessariamente usados, eles são apenas sugestões.
   Crie a documentação de acordo com seu projeto e suas necessidades.

----

Apresentação do projeto
^^^^^^^^^^^^^^^^^^^^^^^

Uma descrição um pouco mais detalhada do projeto.

Exemplos de input e output
^^^^^^^^^^^^^^^^^^^^^^^^^^

Possíveis exemplos (imagens/dados) de input/output do projeto.

Exemplos de interface
^^^^^^^^^^^^^^^^^^^^^

Possíveis exemplos de interface do projeto.

Para informações mais detalhadas sobre o **{{ cookiecutter.project_name }}** veja os links a seguir:


.. toctree::
   :maxdepth: 1
   :name: tutorials
   :caption: Tutoriais

   tutorials/index_tutorials
   tutorials/markdown-cheat-sheet


.. toctree::
   :maxdepth: 1
   :name: dev
   :caption: Desenvolvimento

   dev/index_dev
   dev/api_documentation


Índices e tabelas
-----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
