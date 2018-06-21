clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

uninstall:
	pip freeze | grep -v "^-e" | xargs pip uninstall -y

install: clean
	pip install --upgrade pip
	pip install -e .
	pip install -e ".[test]"

test: clean
	flake8
	openfisca-run-test --country-package openfisca_italy tests
