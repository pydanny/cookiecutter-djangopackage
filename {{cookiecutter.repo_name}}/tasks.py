import os
import webbrowser

from invoke import task


def open_browser(path):
    try:
        from urllib import pathname2url
    except:
        from urllib.request import pathname2url
    webbrowser.open("file://" + pathname2url(os.path.abspath(path)))


@task
def clean_build(c):
    """
    Remove build artifacts
    """
    c.run("rm -fr build/")
    c.run("rm -fr dist/")
    c.run("rm -fr *.egg-info")


@task
def clean_pyc(c):
    """
    Remove python file artifacts
    """
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")


@task
def coverage(c):
    """
    check code coverage quickly with the default Python
    """
    c.run("coverage run --source {{ cookiecutter.repo_name }} runtests.py tests")
    c.run("coverage report -m")
    c.run("coverage html")
    c.run("open htmlcov/index.html")


@task
def docs(c):
    """
    Build the documentation and open it in the browser
    """
    c.run("rm -f docs/{{ cookiecutter.repo_name }}.rst")
    c.run("rm -f docs/modules.rst")
    c.run("sphinx-apidoc -o docs/ {{ cookiecutter.app_name }}")

    c.run("sphinx-build -E -b html docs docs/_build")
    open_browser(path='docs/_build/html/index.html')


@task
def test_all(c):
    """
    Run tests on every python version with tox
    """
    c.run("tox")


@task
def clean(c):
    """
    Remove python file and build artifacts
    """
    clean_build(c)
    clean_pyc(c)


@task
def unittest(c):
    """
    Run unittests
    """
    c.run("python manage.py test")


@task
def lint(c):
    """
    Check style with flake8
    """
    c.run("flake8 {{ cookiecutter.repo_name }} tests")


@task(help={'bumpsize': 'Bump either for a "feature" or "breaking" change'})
def release(c, bumpsize=''):
    """
    Package and upload a release
    """
    clean(c)
    if bumpsize:
        bumpsize = '--' + bumpsize

    c.run("bumpversion {bump} --no-input".format(bump=bumpsize))

    import {{ cookiecutter.repo_name|replace('-', '_') }}
    c.run("python setup.py sdist bdist_wheel")
    c.run("twine upload dist/*")

    c.run('git tag -a {version} -m "New version: {version}"'.format(version={{ cookiecutter.repo_name|replace('-', '_') }}.__version__))
    c.run("git push --tags")
    c.run("git push origin master")
