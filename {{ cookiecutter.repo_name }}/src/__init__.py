"""{{ cookiecutter.description }}"""

__version__ = "0.1.0"
__author__ = "{{ cookiecutter.author_name }}"
__author_email__ = "{{ cookiecutter.author_email }}"
__license__ = "Proprietary software"
__copyright__ = " 2014-2022, %s." % __author__
__homepage__ = "http://sta.spacetimedocs.com/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/"
# this has to be simple string, see: https://github.com/pypa/twine/issues/522
__docs__ = "{{ cookiecutter.description }}"
__long_docs__ = """
{{ cookiecutter.description }}
"""

# for compatibility with namespace packages
__import__('pkg_resources').declare_namespace(__name__)
