test:
	python3 -m unittest

cover_test:
	py.test test_rpn.py --doctest-modules --pep8 coveralls -v --cov coveralls --cov-report term-missing

.PHONY: test
