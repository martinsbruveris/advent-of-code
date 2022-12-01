check_dirs := 2021/code 2022/code

test:
	cd 2022 && poetry run pytest tests

# This target runs checks on all files and potentially modifies some of them
style:
	poetry run black $(check_dirs)
	poetry run isort $(check_dirs)
	poetry run flake8 $(check_dirs)
