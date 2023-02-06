<h1 align="center">Homework №4</h1>

## Goal:
- Learn how to test API services based on their documentation.

## Description:
Testing of each api should be done in a separate test module.

1. Testing the REST service https://dog.ceo/dog-api/
2. Testing the REST service https://www.openbrewerydb.org/
3. Testing the REST service https://jsonplaceholder.typicode.com/

#### Benchmark
- Write at least 5 tests for each REST service.
- At least 2 out of 5 should use parameterization.
- The tests should be successful.

Implement a test function in a separate module that will take 2 parameters:
- ```url``` - there should be a default value https://ya.ru
- ```status_code``` - default value 200

#### Benchmark
- The parameters must be implemented via ```pytest.addoption```.
- You can put a fixture and a test function in one file.
The main task is for your test to check the status of the response from the transmitted url, the one that was transmitted,
i.e. at the address ```https://ya.ru/sfhfhfhfhfhfhfhfh``` the 404 response must be valid
example of running ```pytest test_module.py --url=https://mail.ru --status_code=200```

#### Launch:
1. Moving to the working directory.
```shell script
qa_automation_course>cd homework_04
```

3. Running tests.
```shell script
qa_automation_course/homework_04>pytest [OPTIONS]
```

**Parameters:**

| Parameter  | Description                                                         | Default value |
| ------------- |---------------------------------------------------------------------| ------------- |
| `Dog_api` | Running tests for the service https://dog.ceo/dog-api/              | Optional |
| `Jsonplaceholder` | Running tests for the service https://jsonplaceholder.typicode.com/ | Optional |
| `Open_brewery_db` | Running tests for the service https://www.openbrewerydb.org/        | Optional |
| `test_validation_status_code.py` | Running a validation status_code test                               | Optional |
