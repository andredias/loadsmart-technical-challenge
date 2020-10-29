LoadSmart Technical Challenge
=============================

This project is the implementation of the technical challenge proposed as part of Loadsmart's admission process.
The complete specification is described by the file `be_challenge.pdf`.


System Requirements
===================

1. The project uses Poetry_ for dependency and package management
2. Python 3.6+


Installation
============

1. You must `install poetry <https://python-poetry.org/docs/#installation>`_ first in order to run the project
2. Create a virtual environment for the project::

    poetry install


Running
=======

You must execute all commands from within a shell.
To spawn a shell use::

    poetry shell

And then, you can execute the command using::

    python main.py cargo.csv trucks.csv

Alternatively, you can use skip the shell spawning and run the project directly using `poetry run`::

    poetry run python main.py cargo.csv trucks.csv


Running Tests
-------------

You can execute:

1. poetry shell
2. make test

or you can run the tests directly using::

    poetry run make test



.. _Poetry: https://python-poetry.org/docs
