<h1 align="center">Homework №0</h1>


## Goal:
- Prepare local environment

## Description:
- Install & settings Poetry
- Install library's for work

### Install Poetry.

#### use Pip
```shell script
pip install poetry
```

#### or use Terminal
```shell script
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```


### Settings Poetry
#### Create .venv folder in project 
```shell script
poetry config virtualenvs.in-project true
```

### Init Poetry
```shell script
poetry init
```
#### Input some information about you project (or skip settings by ```Enter```)


### Activate env with poetry
```shell script
poetry shell
```

### Install library's for work
```shell script
poetry add pytest==7.1.2
poetry add requests==2.27.1
poetry add pydantic==1.9.0
poetry add selenium==4.1.3
poetry add allure-pytest==2.9.45
poetry add pytest-xdist==2.5.0
```

### For pre-commit hooks or manual check style you may add some linters
```shell script
poetry add flake8 --dev
poetry add flake8-import-order --dev
poetry add flake8-builtins --dev
poetry add flake8-quotes --dev
poetry add flake8-bugbear --dev
poetry add flake8-commas --dev
poetry add pep8-naming= --dev
```
