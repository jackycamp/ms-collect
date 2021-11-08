Contribute
===========

**This section is a work in progress**

If you are interested in becoming a collaborator for this project, feel free
to reach out to one of the current collaborators. 

But absolutely feel free to clone the source code and play around with it!

    **IMPORTANT: These sections assume that you are using Python3**

    This guide aims to make the setup of your ms-collect development environment a little easier.
    But assumes that you have Python3 or pyenv setup on your machine.
    

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


Pre-requisites
---------------

    Install the linting and code formatting tools using pip

    - pycodestyle: linting/style checking in accordance with pep8
    - autopep8: code formatting in accordance with pep8

    .. code-block:: console

        $ pip install pycodestyle

        $ pip install autopep8
    
    Most of the contributors use vscode, if you do too, then we recommend installing
    the following extensions:

    - pylance

    - Python-autopep8

    - Change your Python Linter to: pycodestyle

