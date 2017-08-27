# Change Log
All enhancements and patches to cookiecutter-django will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).

## NOTE: August 26, 2017 -- ssteinerX

Please see ROADMAP.md for upcoming changes.
From this point forward, releases will be tagged and development will take place on the `develop` branch, merges back to master will be tagged and annotated here.

## [2017-08-25]
#### Tag: 1.0.0

### Added

- Create `develop` branch for WIP
- Add pyup configuration, direct updates to `develop` branch instead of master
- Add Python 3.6 in Tox, Travis configs

### Changed

- Remove Python 3.3 from test matrix
- Upgrade Travis host OS to Trusty
- Merged and/or closed all open pull requests (mostly pyup version updates)
- Updates
  - pytest 3.0.6 -> 3.2.1
  - tox 2.5.0 -> 2.7.0
  - pytest-cov 2.4.0 -> 2.5.1
  - sh 1.12.9 -> 1.12.14
  - flake8 3.3.0 -> 3.4.1

## [2016-12-06]
### Added
- Re-added `get_version()` function in setup.py (@pydanny)

## [2016-11-19]
### Added
- Config for flake8 in setup.cfg (@browniebroke)

### Changed
- Use Tox and fix Tox envlist (@browniebroke)
- Cleaned installations instructions (@browniebroke)
- Corrected domain for readthedocs: .org -> .io (@browniebroke)


## [2016-06-08]
### Changed
- tox.ini file made more compact (@kelseyq)

## [2016-06-04]
### Added
- Makefile watchme for template generation (@pydanny)
- `post_gen_project.py` for removing example project if needed (@pydanny)
- flake8 on generated Python code (@pydanny)
- Issue template (@purplediane)

### Changed
-

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
