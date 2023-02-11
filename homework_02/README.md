<h1 align="center">
  <a href="https://otus.ru/lessons/avtomatizaciya-web-testirovaniya/">
    <img src="../readme/otus.png"
    alt="Otus" width="200">
  </a>
  <br>
   Python QA Engineer
  <br>
</h1>

<h4 align="center">
    Homework №2
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Description</a> •
  <a href="#launch">Launch</a>
</p>


## Goal
- Learn how to write code in the OOP style and cover it with tests.


## Description
Create a base class of a geometric shape (Figure).
Implement classes of geometric shapes:
- Triangle
- Rectangle
- Square
- Circle

Each class should be located in a separate file with the appropriate name.
All files with classes should be located in the ```src/``` folder in the root of the repository.

Each shape must have attributes:
- ```name``` - name of the shape
- ```area``` (calculated!) - area
- ```perimeter``` (calculated!) - perimeter (the sum of the lengths of the sides or the length of the circle)
- Each shape should implement the add_area(figure) method, which should take another geometric shape and return the sum of the areas of these shapes.

Write tests using pytest on these classes.
All tests should be located in the ```tests/``` folder in the root of the repository.


## Launch
1. Moving to the working directory
```shell script
cd homework_02
```

2. Running tests
```shell script
pytest
```

**Parameters**

| Parameter  |  Description |
| ------------ | ------------- |
| `- m smoke` | Running only smoke tests |


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>