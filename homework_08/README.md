<h1 align="center">Homework №8</h1>

## Goal:
- Practice working with Linux OS processes.

## Description:
Write a system process parser of the 'ps aux' command in Python using the standard library and the subprocess module.

#### Example:

```txt
System Status Report:
System Users: 'root', 'user1', ...
Processes started: 833
User processes:
root: 533
user1: 231
...
Total memory used: 553.3 mb
Total CPU used: 33.2%
Most memory uses: (%process name, first 20 characters if it is longer)
Most CPU uses: (%process name, first 20 characters if it is longer)
```

- Also, this report should be saved in a separate txt file with the name of the current date and time of verification.

#### Launch:

1. Moving to the working directory.
```shell script
qa_automation_course>cd homework_08/app
```

2. Running code
```shell script
qa_automation_course/homework_08/app>python main.py
```
