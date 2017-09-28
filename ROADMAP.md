# cookiecutter-djangopackage Roadmap

This document outlines the roadmap for [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage).

#### August 27, 2017 -- sssteinerX

Version 1.0.0 will be the first tagged release.  Cleanup only, see below for
details.

From this point forward, development will be done on a branch other than
master with merges back to master for new tagged releasess.

Each proposed release will have a checklist.  When it's done, the release will
be merged back to master and tagged.

The first release (1.0.0) will be to update all tools used in building the
project and handle all the outstanding pull requests.

#### 1.0.1 : August 27, 2017 -- ssteinerX

Additional cleanup of 1.0.0 release.  No code changes.

Checklist:
    [ ] Remove Django 1.9.x from generation options
    [ ] Remove Python 3.3 from generated project etc.
    [ ] Add Python 3.6 to generated project tests etc.
    [ ] Add generated project to its own Github repo with Tox/Travis so it
        can be tested before releases too!
    [ ] Automate generation & test of generated project as part of new release
    [ ] Document new release/tag workflow

#### 1.0.0 : August 26, 2017 -- ssteinerX

First tagged release with no code changes, really just a clean up release.

Checklist:
    [x] Remove Python 3.3
    [x] Add Python 3.6
    [x] Upgrade Travis Ubuntu to Trusty
    [x] All requirements up to date
    [x] Add ROADMAP.md
    [x] All pull requests handled (closed if possible)
    [x] Update CHANGELOG.md
    [x] Tag 1.0.0

#### 1.1.0 : ????

The 1.1 series will be mostly to bring the testing matrix up to date to ensure
compatibility with all current Django releases as per [Django Supported
Versions](https://www.djangoproject.com/download/#supported-versions).

Each outstanding issue will be revisited to remove those that are no longer
relevant, request duplicatable cases for those without them, and to generally
make it possible to take action on any remaining issues.

#### 1.2.0 : ????

We'll see!  This will be fleshed out after going through all of the outstanding
issues and feature requests.

If you have a feature request, please file an issue!
