lint:
	@echo
	isort --diff -c --skip-glob '**.venv' .
	@echo
	yapf -vv --diff --recursive --style yapf.ini --exclude '**.venv' .
	@echo
	mypy .
	@echo
	flake8 --config flake8.ini .


_test:
	pytest -x -v --cov-report term-missing --cov-report html --cov-branch --cov app/


test: lint _test
