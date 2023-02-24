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
    Homework №5
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Description</a> •
  <a href="#launch">Launch</a>
</p>


## Goal
- Learn how to set up an environment for Selenium tests, write tests, set up expectations for the project. Learn how to write simple selenium scripts.


## Description
#### Part 1
1. Write a fixture to run different browsers (firefox, chrome, opera).
2. The choice of browser should be made by passing the command line argument pytest.
3. Upon completion of the tests, the browser should be closed.
4. Add a command line option that specifies the base URL of opencart.

#### Part 2
1. Write tests that check the elementary presence of elements on different pages of the opencart application
2. Implement at least five tests (one test = one application page)
3. Use methods of explicit expectation of elements

You need to cover:
- The main
- Catalog
- Product card
- Login page in the admin/admin
- User registration page (/index.php?route=account/register)


## Launch
1. Moving to the working directory
```shell script
qa_automation_course>cd homework_05
```

2. Running tests
```shell script
qa_automation_course/homework_05>pytest
```


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
