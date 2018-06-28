clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	flake8
	openfisca-run-test --country-package openfisca_italy openfisca_italy/tests
