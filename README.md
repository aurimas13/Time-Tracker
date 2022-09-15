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

By navigating to the program/app folder where it is extracted - [Tracker](https://github.com/aurimas13/Tracker) - one folder before where test folder is held one can run these test commands:

1) To run unit tests in the project folder run:
```
>>> python -m pytest test/unit/test.py

```

2) To run functional tests in the project folder run:
```
>>> python -m pytest test/functional/test.py

```

# Public

Public folder contains [todolist text file](https://github.com/aurimas13/Tracker/blob/main/public/todolist.txt) and a Logo folder.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the Birthday Reminder Application can be found [here](https://github.com/aurimas13/Tracker/blob/main/public/logo/time_tracker.png).

# License

The MIT [LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)
