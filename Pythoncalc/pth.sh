cp .pypirc /~
python setup.py sdist bdist_wheel
/usr/bin/python -m twine upload dist/* -r nexus
