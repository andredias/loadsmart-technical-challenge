lint:
	@echo
	isort --diff -c --skip-glob '**.venv' .
	@echo
	yapf -vv --diff --recursive --style yapf.ini --exclude '**.venv' .
	@echo
	mypy .
	@echo
	flake8 --config flake8.ini .
