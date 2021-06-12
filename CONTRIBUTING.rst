.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/pydanny/cookiecutter-djangopackage/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

`cookiecutter-djangopackage`_ could always use more documentation, whether as part of the
official docs, in docstrings, or even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/pydanny/cookiecutter-djangopackage/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `cookiecutter-djangopackage`_ for local development. Please note this documentation assumes you have a `GitHub`_ account,
you already have `virtualenv`_ and `Git`_ installed and ready to go. If you are using Python 3.5, you already have virtualenv, as it comes with Python 3.5.

1. Fork the `cookiecutter-djangopackage`_ repo on GitHub.
2. Clone your fork locally::

    $ cd path_for_the_repo
    $ git clone git@github.com:YOUR_NAME/cookiecutter-djangopackage.git

3. Assuming you have virtualenv installed (If you have Python3.5 this should already be there), you can create a new environment for your local development by typing::

    $ virtualenv cookiecutter-djangopackage-env
    $ source cookiecutter-djangopackage-env/bin/activate

   This should change the shell to look something like::

    (cookiecutter-djangopackage-env) $

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. The next step would be to run the test cases. `cookiecutter-djangopackage`_ uses py.test, you can run PyTest. Before you run pytest you should ensure all dependancies are installed::

    $ pip install -r requirements_dev.txt
    $ py.test

   If you get any errors while installing cryptography package (something like #include <openssl/aes.h>).
   Please update your pip version and try again::

    # Update pip
    $ pip install -U pip

7. Before raising a pull request you should also run tox. This will run the tests across different versions of Python::

    $ tox

   .. note:: If you are missing flake8, pytest and/or tox, just pip install them into your virtualenv.

8. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

9. Submit a pull request through the GitHub website. See Guidelines below.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7, 3.8 and 3.9, and for PyPy3. Check
   https://travis-ci.org/pydanny/cookiecutter-djangopackage/pull_requests
   and make sure that the tests pass for all supported Python versions.


.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`virtualenv`: https://virtualenv.pypa.io/en/stable/installation
.. _`Git`: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _`GitHub`: https://github.com/
