import sys


config_identifier = {{ "%r" % cookiecutter.config_identifier }}

try:
    int(config_identifier)
except ValueError:
    print("ERROR: Config identifier needs to be an integer.")
    sys.exit(1)
