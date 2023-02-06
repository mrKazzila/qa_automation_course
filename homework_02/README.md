<h1 align="center">Homework №2</h1>


## Goal:
- Learn how to write code in the OOP style and cover it with tests.

## Description:
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

## Launch:

1. Moving to the working directory.
```shell script
qa_automation_course>cd homework_02
```

2. Running tests.
```shell script
pytest
```

**Parameters:**

| Parameter  |  Description |
| ------------ | ------------- |
| `- m smoke` | Running only smoke tests |
