<p align=center>
  <img height="400px" src="https://github.com/aurimas13/Tracker/blob/main/public/logo/time_tracker.png"/>
</p>

<p align="center" > <b> Time Tracker </b> </p>
<br>
<p align=center>
  <a href="https://github.com/aurimas13/Tracker/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/npm/l/express"></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

The app tracks the time of stories and tasks. Details of the usage are under [Usage](#usage).
Please refer to Requirements for importing required libraries before looking at the [Usage](#usage).

# Table of contents

[//]: # (- [Birthday Reminder App]&#40;#birthday-reminder-app&#41;)

- [Table of contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
- [Datasets](#datasets)
- [Tests](#tests)
- [Error](#errors)
- [Cron Job](#cron-job)
- [Public](#public)
- [Logo](#photo)
- [License](#license)

# Requirements


`IMPORTANT NOTE:` To run the services you might need to use the virtual environment:
```
virtualenv my_env
source my_env/bin/activate
```

**Python 3.10.6** is required to properly execute package's modules, imported libraries and defined functions. 
To install the necessary libraries run [requirements.txt](https://github.com/aurimas13/Tracker/blob/main/requirements.txt) file as shown:
`pip install -r requirements.txt`.

For proper usage of the program you might need to run **python3** rather than proposed **python** as shown in the [Usage](#usage).<sup>1</sup>

<br><sup>1</sup>**python** or **python3** depends on the way how you installed python of version 3.* on your machine. </br>
# Usage
After the requirements are met, the app package is set at your directory and terminal is run you have to run the flask app:
```
>>> conda create --name tracker 
>>> conda activate tracker 
>>> flask db upgrade 
>>> flask run
```

# Tests

An overview of functions found inside a module - [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py):
- *test_correct_parse_date_ymd()* tests if the correct date is parsed.
- *test_correct_parse_date_md()* tests if the correct date is parsed.
- *test_is_date_in_past_old()* tests if the old date is in the past.
- *test_is_date_in_past_future()* tests if the future date is in the past.
- *test_is_date_in_past_past_month_day()* tests if the old date is in the past.
- *test_is_valid_email_good()* tests if the email address is valid.
- *test_is_valid_email_bad()* tests if the email address is invalid.

By navigating to the program/app folder where it is extracted - [BirthdayReminderApp](https://github.com/aurimas13/BirthdayReminderApp#birthday-reminder-app) - one folder before where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held and one can run these test commands:

[//]: # ([comment]: <> &#40;For DocTest run this command in terminal:&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;``` python&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;> python -m doctest -v calculator.py&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;```&#41;)
1) To check source files for errors in the project folder:
```
>>> pyflakes .
```

2) To check source files for errors in test file: 
```
>>> pyflakes Tests/tests.py
```

3) To check typing for test file:
``` 
>>> python -m pytest Tests/tests.py
```
# Errors

There could arise a few errors like:

1) 1st argument error if the provided 1st argument is of different format to the csv format:
```
>>> python bdayreminder.py Datasets/data_20.json 1      
Traceback (most recent call last):
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 237, in <module>
    run(arg_path, cron_input)
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 215, in run
    raise Exception('ERROR: Wrong data format file')
Exception: ERROR: Wrong data format file
```
2) 1st argument error if the provided 1st argument of data file doesn't exist:
```
>>> python bdayreminder.py Datasets/data_13.csv 1 
Traceback (most recent call last):
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 237, in <module>
    run(arg_path, cron_input)
  File "/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/bdayreminder.py", line 199, in run
    raise Exception('ERROR: File doesn\'t exist')
Exception: ERROR: File doesn't exist
```
3) 2nd argument error if the provided 2nd argument is a string:
```
>>>  python bdayreminder.py Datasets/data_20.csv versada
Argument passed not an integer
```

There are more yet these would be the most common.

# Cron Job

To build cron job in mac terminal run:
``` 
>>> crontab -e
```

The syntax for cronjob when entering terminal could look like this:<sup>1,2,3</sup>
``` 
>>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2
[Optional] >>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2 >> Public/birthdays.txt
```
<br><sup>1</sup> **<directory_to_app>** - should be the directory where BirthdayReminderApp folder is like /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp </br>
<br><sup>2</sup> **<directory_to_python>** should be where you installed python on your machine like /Users/aurimasnausedas/opt/miniconda3/envs/symmetric/bin/python </br>
<br><sup>3</sup> **<data_file_path>** should be the dataset in the directory of app like in /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp by setting it to Datasets/data_20.csv </br>

Syntax customization for Cron Job can be checked [here](https://crontab.guru/).

# Public

Public folder contains three files: 
- [birthdays.txt](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/birthdays.txt) - the output of a Cron Job after implementing the [Optional] command as given at [Cron Job](#cron-job) field.
- [todolist](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/todolist) - the TO DO List.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the Birthday Reminder Application can be found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/Photo/birthdaylogo.png).

# License

The MIT [LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)
