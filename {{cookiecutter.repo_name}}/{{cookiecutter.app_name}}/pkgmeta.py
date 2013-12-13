pkgmeta = dict(
    __title__='{{ cookiecutter.project_name }}',
    __author__='{{ cookiecutter.full_name }}',
    __version__='{{ cookiecutter.version }}',
)

globals().update(pkgmeta)
__all__ = pkgmeta.keys()
