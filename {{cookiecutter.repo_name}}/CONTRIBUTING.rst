============
Contributing
============

Bugs
~~~~

Please report bugs on our bug tracker: https://hogarthww.atlassian.net/

If you are reporting a bug, please include:

* OS name and version.
* Details about your test setup/settings.
* Steps to reproduce the issue.

Documentation
~~~~~~~~~~~~~

{{ cookiecutter.project_name }} documentation is built via docstrings.


Get Started!
------------

1. Clone the repo locally::

    $ git clone git@github.hogarth.prv:hogarthww/{{ cookiecutter.repo_name }}.git

2. Create a virtualenv and install dev dependencies::

    $ mkvirtualenv {{ cookiecutter.repo_name }}
    $ cd {{ cookiecutter.repo_name }}/
    $ python setup.py develop

4. Create a branch for your new feature::

    $ git checkout -b feature/my-cool-feature

Now you can make your changes locally.

5. Run tests and linting to make sure they pass::

    $ flake8 {{ cookiecutter.app_name }} tests
    $ python setup.py test
    $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin feature/my-cool-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Your pull requests must contain adequate tests and documentation.

Also, please use the PR template located here: https://github.hogarthww.prv/mikejarrett/pull-request-template

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_{{ cookiecutter.app_name }}
