# Basing off of requests
# https://github.com/kennethreitz/requests/blob/master/Makefile

init:
	pip install -r requirements.txt

test:
	# This runs all of the tests. To run an individual test, run py.test with
	# the -k flag, like "py.test -k test_path_is_not_double_encoded"
	py.test tests

coverage:
	py.test --verbose --cov-report term --cov=consumer tests

freeze:
	pip freeze > requirements.txt

publish:
	python setup.py register
