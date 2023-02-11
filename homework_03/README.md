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
    Homework №3
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Description</a> •
  <a href="#launch">Launch</a>
</p>


## Goal
- Learn how to work with different types of files.


## Description
- Write a script that will read data from two data files and create a result based on them.json file 
- The idea is that you need to distribute all the books from the csv file to users from the list.
  - Books are put together in the form of dictionaries in an array of books for each user
  - There are initially more books than users, so you need to distribute them according to the principle of 'as evenly as possible', i.e. if there are 10 books, for example, and 3 users, then the distribution will be as follows - 4 3 3 (one will receive the remaining book).
- The final structure must comply with the json standard and be parsed by the appropriate library.


## Launch
1. Moving to the working directory
```shell script
cd homework_03/app
```

2. Running code
```shell script
python main.py  [OPTIONS]
```

**Parameters**

| Parameter | Type  | Description | Default value |
| --------- |-------|-----------| ------------- |
| `--users_file_path` | `str` | The path to the file users.json | Optional |
| `--books_file_path` | `str` | The path to the file books.csv | Optional |
| `--result_file_path` | `str` | The path to the file with json results | Optional |


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>