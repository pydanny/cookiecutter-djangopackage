import re
import sys

APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

app_name = '{{cookiecutter.app_name}}'

if not re.match(APP_REGEX, app_name):
    sys.exit(1)
