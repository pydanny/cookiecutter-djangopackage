==========================
cookiecutter-djangopackage
==========================

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Usage
------

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/hogarthww/cookiecutter-djangopackage.git

You'll be prompted for some questions, answer them, then it will create a cookiecutter-djangopackage with
your new package.

Features
--------

* Tox configuration
* Sphinx Documentation
* Sane setup.py for easy PyPI registration/distribution
* Makefile for easy cli
* BSD licensed by default

