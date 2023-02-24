<h1 align="center">
  <a href="https://otus.ru/lessons/avtomatizaciya-web-testirovaniya/">
    <img style="background-color: #ffffff" src="../readme/otus.svg"
    alt="Otus" width="200">
  </a>
  <br>
   Python QA Engineer
  <br>
</h1>

<h4 align="center">
    Homework №0
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Description</a>
</p>


## Goal
- Prepare local environment.


## Description
1. Install & settings Poetry
2. Install library's for work


- Install Poetry
  - use Pip
    - ```pip install poetry ```
  - or use Terminal
    - ```(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -```

- Settings Poetry
  - Create .venv folder in project 
    - ```poetry config virtualenvs.in-project true```

- Init Poetry
  - ```poetry init```

- Input some information about you project (or skip settings by ```Enter```)

- Activate env with poetry
  - ```poetry shell```


- Install library's for work
```shell script
poetry add pytest==7.1.2
poetry add requests==2.27.1
poetry add pydantic==1.9.0
poetry add selenium==4.1.3
poetry add allure-pytest==2.9.45
poetry add pytest-xdist==2.5.0
```

- For pre-commit hooks or manual check style you may add some linters
```shell script
poetry add flake8 --dev
poetry add flake8-import-order --dev
poetry add flake8-builtins --dev
poetry add flake8-quotes --dev
poetry add flake8-bugbear --dev
poetry add flake8-commas --dev
poetry add pep8-naming= --dev
```


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
