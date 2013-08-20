==========================
cookiecutter-djangopackage
==========================

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly. 

**Why?** Creating reusable Django packages has always been annoying. There are no defined/maintained
best practices (especially for ``setup.py``), so you end up cutting and pasting hacky, poorly understood, 
often legacy code from one project to the other. This template, inspired by `cookiecutter-pypackage`_,
is designed to allow Django developers the ability to break free from cargo-cult configuration and follow
a common pattern dictated by the experts and maintained here. 

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

Features
--------

* Travis-CI configuration
* Tox configuration
* Sphinx Documentation
* Sane setup.py for easy PyPI registration/distribution
* BSD licensed by default


Usage
------

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/pydanny/cookiecutter-dj-package.git

You'll be prompted for some questions, answer them, then it will create a cookiecutter-dj-package with
your new package.

Let's pretend you want to create a reusable Django app called "Blogging-for-Humans", with an app that can be placed
in INSTALLED_APPS as "blogging_humans". Rather than have to copy/paste from other people's projects and
then fight enthusiasm destroying app layout issues like `setup.py` configuration and creating test
harnesses, you get cookiecutter_ to do all the work.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-dj-package'...
    remote: Counting objects: 49, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 49 (delta 6), reused 48 (delta 5)
    Unpacking objects: 100% (49/49), done.
    full_name (default is "Your full name here")? Daniel Greenfeld
    email (default is "you@example.com")? pydanny@gmail.com
    github_username (default is "yourname")? pydanny
    project_name (default is "dj-package")? Blogging-for-Humans
    repo_name (default is "dj-package")? blogging-for-humans
    app_name (default is "djpackage")? blogging_humans        
    project_short_description (default is "Your project description goes here")? A blog that's easy for humans to use!
    release_date (default is "2013-08-15")? 2013-08-15
    year (default is "2013")? 2013
    version (default is "0.1.0")? 0.3.0

Enter the project and take a look around::

    $ cd blogging-for-humans/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:pydanny/blogging-for-humans.git
    $ git push -u origin master

Now take a look at your repo. Awesome, right?

It's time to write the code!!!

Register on PyPI
~~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI::

    python setup.py register


Releasing on PyPI
~~~~~~~~~~~~~~~~~~~~~~~~

Time to release a new version? Easy! Just run::

    $ python setup.py publish

It will answer with something like::

    You probably want to also tag the version now:
          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.

Add to Django Packages
~~~~~~~~~~~~~~~~~~~~~~~

Once you have a release, and assuming you have an account there, just go to https://www.djangopackages.com/packages/add/ and add it there. 

