<h1 align="center">Homework №5</h1>


## Goal:
- Learn how to set up an environment for Selenium tests, write tests, set up expectations for the project. Learn how to write simple selenium scripts.

## Description:

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


#### Launch:

1. Moving to the working directory.
```shell script
qa_automation_course>cd homework_05
```

2. Running tests
```shell script
qa_automation_course/homework_05>pytest
```
