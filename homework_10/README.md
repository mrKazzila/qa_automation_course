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
    Homework №10
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Requirements</a> •
  <a href="#launch">Launch</a>
</p>


## Goal
- Practice using the socket module and network interaction over the HTTP protocol.


## Requirements
1. We implement our own echo server using the socket library.
2. Your server must accept the request from the client and send it to him:
   - headers received in the request
   - the method by which the request was made
   - set the status that the client passed in the GET status parameter
   - if the parameter is not passed or is not valid, then give 200
   - if the value is (optional), the server should not stop working after responding to the client, but continue to wait for the next connection
   - Headings should be displayed on the page as lines of text:
     - Request Method: GET
     - Request Source: ('127.0.0.1', 47296)
     - Response Status: 200 OK
     - header-name: header-value
     - header-name: header-value
     - ...


## Launch
1. Moving to the working directory
```shell script
cd homework_10/echo_server
```

2. Running code
```shell script
python server.py
```


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
