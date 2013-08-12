======================
cookiecutter-dj-package
======================

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly:

.. _cookiecutter: https://github.com/audreyr/cookiecutter.


Usage
------

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/pydanny/cookiecutter-dj-package.git

You'll be promoted for some questions, answer them, then it will create a cookiecutter-dj-package with your new package. Change the name of that directory to your own project's name, then send that to GitHub.

Example
-------

You want to create a reusable Django app called "Blogging-for-Humans", with an app that can be placed in INSTALLED_APPS as "blogging_humans". Rather than have to copy/paste from other people's projects and then fight enthusiasm destroying app layout issues like `setup.py` configuration and creating test harnesses, you get cookiecutter_ to do all the work.

First, get cookiecutter. I'm telling you, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/pydanny/cookiecutter-dj-package.git

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

It prompts you for questions. Answer them:

    Cloning into 'cookiecutter-dj-package'...
    remote: Counting objects: 49, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 49 (delta 6), reused 48 (delta 5)
    Unpacking objects: 100% (49/49), done.
    full_name (default is "Your full name here")? Daniel Greenfeld
    email (default is "Your email address here")? pydanny@gmail.com
    github_username (default is "Your GitHub name here")? pydanny
    project_name (default is "The human friendly project name goes here.")? Blogging-for-Humans
    repo_name (default is "The GitHub repo name goes here")? blogging-for-humans
    app_name (default is "The name that is added to INSTALLED_APPS goes here.")? blogging_humans        
    project_short_description (default is "Your project description goes here")? A blog that's easy for humans to use!
    release_date (default is "2013-08-15")? 2013-08-15
    year (default is "2013")? 2013
    version (default is "0.1.0")? 0.3.0

Now rename the repo:

    $ mv cookiecutter-dj-package Blogging-for-Humans

Create a GitHub repo and push it there:

    $ cd Blogging-for-Humans/
    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:pydanny/Blogging-for-Humans.git
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

