# Elementary Reports

[Elementary Reports](https://elementary-reports-fc8c248a84d7.herokuapp.com/)

## Introduction

![image](https://github.com/deklyn00/elementary-reports/assets/134307267/30d3e799-de0b-4d60-92ed-14b24ed929dc)

Elementary Reports is a terminal-based Python application designed to manage and display student report cards for various subjects. It utilizes the Google Sheets API to store and retrieve student grades.

### Goals

1. **Student Reports:** Generate report cards for students with grades in multiple subjects.
2. **Data Validation:** Ensure data input is valid and within the specified range.
3. **Add New Students:** Allow the addition of new students with their grades.

## Features

### Add Student Grades

The application allows you to add a new student's name and their grades for each subject. You can input four integer values between 0 and 25 for each subject, representing the grades for four assignments.
![image](https://github.com/deklyn00/elementary-reports/assets/134307267/3106ca15-4d38-4611-9c34-6a8f9242c426)

![image](https://github.com/deklyn00/elementary-reports/assets/134307267/446cdc02-11e5-428d-abbf-fe3a33055227)

Please wait for the successfully added message as through Heroku it may take a moment once all of the values are entered.

### Get Existing Grades

You can search for existing students by name and retrieve their report cards, displaying grades for each subject.
![image](https://github.com/deklyn00/elementary-reports/assets/134307267/ff1b82d5-aabd-42ff-ae20-16461c898ec4)

### Data Validation

The application performs data validation to ensure that student names are valid strings and that grades are integers between 0 and 25.

### Type of Pass

The application also calculates and displays the type of pass (Fail, Pass, Merit, or Distinction) based on the total grade.

## Usage

1. Run the application through the heroku deployed application at [Elementary Reports](https://elementary-reports-fc8c248a84d7.herokuapp.com/).
2. To ensure you use the application correctly initially you wil be asked to type "A" or "G" for the specific task, please use uppercase responses for the entry you make.
3. Choose to add new student grades or get existing grades.
4. To see existing names on the workseet see [Elementary Reports Google Sheet](https://docs.google.com/spreadsheets/d/1bV6n9P81VqisEU9JyWo7MfvoCAtqtmqyXcs8maf3exI/edit?usp=sharing).
5. When adding a new student you will need to add 4 grades per subjects as the prompts will guide you, no values over 25 are permitted.
6. View added students on the sheet in the following link [Elementary Reports Google Sheet](https://docs.google.com/spreadsheets/d/1bV6n9P81VqisEU9JyWo7MfvoCAtqtmqyXcs8maf3exI/edit?usp=sharing).
## Dependencies
- [Elementary Reports Google Sheet](https://docs.google.com/spreadsheets/d/1bV6n9P81VqisEU9JyWo7MfvoCAtqtmqyXcs8maf3exI/edit?usp=sharing)
- Python
- gspread
- google.oauth2
- Google Sheets API

## Credits
The link provided leads to a page that helped explain different use cases for Google sheets with python.
[The Comprehensive Guide To Google Sheets With Python](https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/)

### Google Sheets API

This project utilizes the Google Sheets API for storing and retrieving student data.

## Bugs
No known bugs when running the terminal.

## Improvements
Further features could be added such as deleting students or creating login algorithms to control access and allow students to look up their own grades without being able to do more.

[Elementary Reports](https://elementary-reports-fc8c248a84d7.herokuapp.com/)
