#!/usr/bin/sh
python setup.py sdist bdist_wheel
python -m  twine upload --repository-url http://localhost:8081/repository/pypi-internal/ dist/*
admin
admin123
