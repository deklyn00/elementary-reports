# Elementary Reports

![Elementary Reports]()

## Introduction

Elementary Reports is a terminal-based Python application designed to manage and display student report cards for various subjects. It utilizes the Google Sheets API to store and retrieve student grades.

### Goals

1. **Student Reports:** Generate report cards for students with grades in multiple subjects.
2. **Data Validation:** Ensure data input is valid and within the specified range.
3. **Add New Students:** Allow the addition of new students with their grades.

## Features

### Add Student Grades

The application allows you to add a new student's name and their grades for each subject. You can input four integer values between 0 and 25 for each subject, representing the grades for four assignments.

### Get Existing Grades

You can search for existing students by name and retrieve their report cards, displaying grades for each subject.

### Data Validation

The application performs data validation to ensure that student names are valid strings and that grades are integers between 0 and 25.

### Type of Pass

The application also calculates and displays the type of pass (Fail, Pass, Merit, or Distinction) based on the total grade.

## Usage

1. Run the application by executing `python run.py` in your terminal.
2. Choose to add new student grades or get existing grades.

## Dependencies

- Python
- gspread
- google.oauth2
- Google Sheets API
- Other libraries as specified in your project

## Credits
The link provided leads to a page that helped explain different use cases for Google sheets with python.
![The Comprehensive Guide To Google Sheets With Python](https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/)

### Google Sheets API

This project utilizes the Google Sheets API for storing and retrieving student data.

## Bugs
No known bugs when running the terminal through Codeanywhere.

## Improvements
Further features could be added such as deleting students or creating login algorithms to control access and allow students to look up their own grades without being able to do more.
