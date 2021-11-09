Contribute
===========

**This section is a work in progress**

If you are interested in becoming a collaborator for this project, feel free
to reach out to one of the current collaborators. 

But absolutely feel free to clone the source code and play around with it!

    **IMPORTANT: These sections assume that you are using Python3**

    This guide aims to make the setup of your ms-collect development environment a little easier,
    but assumes that you have Python3 or pyenv using a Python3 version setup on your machine.
    

Quick setup
-------------

    So you want to get your hands on the code huh? You want to know the quickest way to do that huh?

    Easy. Just follow this section :)

    1. First clone the repository and cd into ms-collect:

    .. code-block:: console

        $ git clone https://github.com/jakuzo/ms-collect.git

        $ cd ms-collect

    2. Next install the development dependencies:

    .. code-block:: console

        $ pip install -r requirements.txt

    3. Then install an editable instance of ms-collect. This allows you to make changes to all
    of the source code under ``src/`` and not have to build it every time.

    .. code-block:: console

        $ python -m pip install -e .

    4. There are some datasets in csv format under ``test/`` that you can play around with as well.


VS Code Setup
---------------

    Most of the contributors use vscode, if you do too, then we recommend installing
    the following extensions:

    - pylance

    - Python-autopep8

    - Change your Python Linter to: pycodestyle


Githooks
----------

    If you are a contributor i.e. are authorized to push code to ms-collect's repository,
    please ensure that you have the shared githooks configured properly.

    Assuming that you have cloned the repository, you will notice that there is a directory
    named ``.githooks/``

    In order for the hooks in this directory to run, please update the hooks config for your local copy of this repo:

    .. code-block:: console

        $ git config core.hooksPath .githooks
    
    All of the hook scripts in this directory need to be executable, so please ``chmod +x`` all files in the ``.githooks/`` directory.
    For example:

    .. code-block:: console

        $ chmod +x .githooks/pre-commit


Working on the Docs
--------------------
TODO



Building and Publishing ms-collect to PyPI
--------------------------------------------

TODO


Requirements
--------------

    This section outlines installing each requirement and some context for each dependency.
    If you just want to automatically install the dependencies and move on then:

    .. code-block:: console

        # At the same level as setup.cfg and pyproject.toml

        $ pip install -r requirements.txt


    But if you want some explanation behind each dependency and how to install them
    individually then keep following along :)

    - **pycodestyle**: Used for linting in accordance with pep8. (Also baked into our pre-commit hook)

    .. code-block:: console

        $ pip install pycodestyle

    - **autopep8**: Used for auto formatting your python code in accordance with pep8

    .. code-block:: console

        $ pip install autopep8
    
    - **sphinx** TODO

    .. code-block:: console

        $ pip install sphinx

    - **karma-sphinx-theme** TODO
    
    .. code-block:: console

        $ pip install karma-sphinx-theme

    - **build** TODO

    .. code-block:: console

        $ pip install build
    
    - **twine** TODO

    .. code-block:: console

        $ pip install twine

    - **matplotlib** TODO

    .. code-block:: console

        $ pip install matplotlib









