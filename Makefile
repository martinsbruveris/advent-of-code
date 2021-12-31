check_dirs := code

# This target runs checks on all files and potentially modifies some of them
style:
	poetry run black $(check_dirs)
	poetry run isort $(check_dirs)
	poetry run flake8 $(check_dirs)
