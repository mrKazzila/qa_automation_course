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
    Homework №9
</h4>
<hr>

<p align="center">
  <a href="#goal">Goal</a> •
  <a href="#description">Requirements</a> •
  <a href="#launch">Launch</a> •
  <a href="#log-format">Log Format</a>
</p>


## Goal
- Practice writing parsers for logs.


### Requirements
1. It should be possible to specify directories where to look for logs or a specific file
2. It should be possible to process all logs inside one directory
3. The following information should be collected for access.log:
   - total number of completed requests
   - the number of requests by HTTP methods: GET - 20, POST - 10, etc.
   - top 3 IP addresses from which requests were made
   - top 3 longest requests, the method, url, ip, duration, date and time of the request should be visible
4. The collected statistics should be saved in a json file and output to the terminal in a free (but understandable!) format
5. Must be README.md a file that describes how the script works


## Launch
1. Moving to the working directory
```shell script
cd homework_09/app
```

2. Running code
```shell script
python main.py [OPTIONS]
```

**Parameters**

| Parameter  | Type | Description                              | Default value |
| ------------- | ------------- |------------------------------------------| ------------- |
| `--logs_path`  | `str` | The path to the log file or logs folderи | Required |
| `--output_file_path`  | `str` | The path to the result file              | Optional | 


## Log Format
#### JSON file format for a single log file
```json5
{
   "count": 0000,
   "methods": {
      "GET": 0000,
      ...,
   },
   "top_3_ipS": [
      [
         "193.106.31.130",
         000
      ],
      ...
   ],
   "top_10_duration": [
      [
         "POST",
         "62.93.172.245",
         "-",
         "23/Dec/2015:07:27:57",
         0000
      ],
      ...,
   ]
}
```
#### JSON file format for a directory with .log files
```json5
{
   "<log_file_name>.log": {
      "count": 000,
      "methods": {
         "GET": 000,
         ...
      },
      "top_3_ipS": [
         [
            "191.182.199.16",
            000
         ],
         ...,
         ]
         "top_10_duration": [
            [
               "POST",
               "189.13.146.143",
               "http://almhuette-raith.at/administrator/",
               "12/Dec/2015:20:06:43",
               0000
            ],
            ...,
         ]
         },
   "<second_log_file_name>.log": {
            ...,
         }
}
```


<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
