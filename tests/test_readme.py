def test_readme(cookies):
    result = cookies.bake()

    readme_file = result.project.join('README.rst')
    readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
    assert 'Then use it in a project::' in readme_lines
    assert '(myenv) $ pip install -r requirements-test.txt' in readme_lines
