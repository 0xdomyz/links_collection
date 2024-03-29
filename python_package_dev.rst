===============
contents
===============

* `Packaging`_
* `Vitual Environment`_
* `dependency management`_
* `Documentation`_
* `Lint`_
* `Testing`_

Packaging
=========

`Python org packaging tutorial <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_

`Setup tools <https://setuptools.pypa.io/en/latest/userguide/quickstart.html>`_

`Pip <https://packaging.python.org/en/latest/tutorials/installing-packages>`_

`Packaging tutorial <https://python-packaging.readthedocs.io/en/latest/index.html>`_

`pyproject.toml <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`_

`pypi <https://pypi.org/>`_

Quick package:

.. code-block:: console

    #structure
    mkdir src
    mkdir src/{package_name}
    cd src/{package_name}
    touch __init__.py
    touch a_script.py   
    cd ../..
    
.. code-block:: console

    #meta data
    code pyproject.toml

`pyproject.toml example <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`_
    
Build and Publishing:

.. code-block:: console

    #need pypi registration first
    
    python3.11 -m pip install --upgrade build
    python3.11 -m pip install --upgrade twine
    
    python3.11 -m build
    python3.11 -m twine upload dist/*
    
user name: __token__

password: token


Vitual Environment
==================

`Real python tute <https://realpython.com/python-virtual-environments-a-primer/>`_

linux:

.. code-block:: console

    sudo apt-get install python3-venv
    python3.9 -m venv venv_pymc3
    
    source venv_pymc3/bin/activate
    deactivate
    
    source ~/Projects/python_collection/venvs/venv_mach/bin/activate
    deactivate

dependency management
===========================

`strat <https://blog.inedo.com/python-package-dependency-managament-demystified>`_

Documentation
=============

`Sphinx tutorial <https://www.sphinx-doc.org/en/master/tutorial/index.html>`_

`Sphinx directive doco <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

`rst cheat sheet <https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html>`_

`Sphinx domains <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html>`_

`Read the Docs Sphinx cross referencing guide <https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html>`_

`Extension napolean <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_

`Docutils directive doco <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_

`Docutils rst quickref <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

`Read the Docs tutorial <https://docs.readthedocs.io/en/stable/tutorial/>`_

`pyment <https://github.com/dadadel/pyment>`_

`config example <https://github.com/0xdomyz/dwopt/blob/master/docs/source/conf.py>`_

Quick set-up:

.. code-block:: console

    pip install sphinx
    pip install sphinx_rtd_theme

.. code-block:: console

    mkdir docs
    sphinx-quickstart docs
    y
    {proj_name}
    {author_name}
    {version}
    en
    echo .. include:: ../../README.rst > docs/source/index.rst
    cd docs
    make html
    explorer.exe docs/build/html/index.html

Quick API:

* docstring:

  .. code-block:: console

      pyment -o numpydoc -w myfile.py

* Title: "= - ` : ' " ~ ^ _ * + # < >"

* numpy style::

    def func(arg1, arg2):
        """Summary line.
    
        Extended description of function.
    
        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value
        """
        return True

* In config:

  .. code-block:: python
  
      sys.path.insert(0, os.path.abspath("{path to module root e.g. ../../src}"))
      extensions = [
          "sphinx.ext.autodoc",
          "sphinx.ext.napoleon",
          "sphinx.ext.viewcode",
          "sphinx.ext.autosummary",
      ]
      html_theme = "sphinx_rtd_theme"
      #templates_path
      #exclude_patterns
      #html_static_path

* In README.rst:

  .. code-block:: text

      .. automodule:: mymodule
        :members:
        :undoc-members:
        :private-members:

sphinx make pdf::

    # install
    sudo apt-get install texlive-full
    sudo apt-get install latexmk
    # test
    pdflatex document.tex
    # actual
    make latexpdf

Lint
======

`black <https://black.readthedocs.io/en/stable/index.html>`_

`black compatibility with flake8 <https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html?highlight=fake8flake%208#flake8>`_

Testing
=======

`Pytest <https://docs.pytest.org/en/7.0.x/>`_

just a func or class or file::

    pytest tests/test_mod.py
    pytest tests/test_mod.py::test_func
    pytest tests/test_mod.py::test_class

`Pytest fixtures <https://docs.pytest.org/en/latest/how-to/fixtures.html>`_

`Tox <https://tox.wiki/en/latest/>`_

`Flake8 <https://flake8.pycqa.org/en/latest/index.html>`_

`Flake8 rules <https://www.flake8rules.com/>`_

`Github action <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py>`_

`Github action setup python <https://github.com/actions/setup-python>`_
