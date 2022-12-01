check_dirs := aoc tests

test:
	poetry run pytest tests -s -v

# This target runs checks on all files and potentially modifies some of them
style:
	poetry run black $(check_dirs)
	poetry run isort $(check_dirs)
	poetry run flake8 $(check_dirs)
