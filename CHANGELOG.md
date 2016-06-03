# Change Log
All enhancements and patches to cookiecutter-django will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [2016-06-03]
### Added
- Views and urls based on specified model names (@leportella)
- Tests for urls and views and correcting model.strip() in some places (@leportella)

### Changed
- Updated usage and fix requirements (@purplediane)
- Expanded tests (@purplediane)

## [2016-06-02]
### Added
- pytest-cookies (@pydanny)
- tox config (@pydanny)

## [2016-06-01]
### Added
- ability to specify django versions to run tox against rendered project (@kelseyq)

## [2016-05-16]
### Changed
- Corrected datetime generation in `cookiecutter.json` (@kelseyq)

## [2016-05-13]
### Changed
- Name to Cookiecutter Django Package (@pydanny)

## [2016-05-12]
### Added
- Basic model generation (@pydanny)

## [2016-05-06]
### Changed
- Made MakeFile self documenting (@aaronbassett)

## [2016-05-06]
### Changed
- Fix Makefile to use Python to open the docs in the default webbrowser (@JoseTomasTocino)

## [2016-02-29]
### Changed
- Fix indents following code blocks (@acdha)

## [2016-02-11]
### Added
- Added Pycharm project configuration folder to .gitignore (@luzfcb)

## [2016-02-04]
### Added
- Corrected pip command (@davidastephens)
- Fixed filepath argument in setup.py (@jangeador)

## [2015-11-23]
### Added
- Validation of app_name (@hackebrot)

## [2015-11-22]
### Changed
- Formal Python 3.5 support (@luzfcb)

## [2015-11-20]
### Changed
- Fixed typo in README (@grokcode)

## [2015-11-14]
### Changed
- Fixed installation description (@jondelmil)

## 2015/11/12
### Added
- Insistence that wheel be used during package creation (@pydanny)
- Editor config (@pydanny)
- Bumpversion in project and requirements_dev.txt (@guilhermemaba)
- Travis for light testing (@pydanny)
- Two Scoops Academy sponsor mention (@pydanny)
- Testing instructions (@pydanny)

## 2015/09/28
### Changed
* Coverage results no longer are stored in version control, thanks to @grantmcconnaughey
