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
- [Tests](#tests)
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

# Public

Public folder contains [todolist text file](https://github.com/aurimas13/Tracker/blob/main/public/todolist.txt) and a Logo folder.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the Birthday Reminder Application can be found [here](https://github.com/aurimas13/Tracker/blob/main/public/logo/time_tracker.png).

# License

The MIT [LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)
