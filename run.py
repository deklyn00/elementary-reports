import gspread
from google.oauth2.service_account import Credentials

# Define constants for credentials and scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('elementaryreports')

# Calculating the total grade
def calculate_total_grade(student, worksheet):
    headers = worksheet.row_values(1)
    try:
        student_column = headers.index(student) + 1
    except ValueError:
        return None

    grades = worksheet.col_values(student_column)[1:5]
    total_grade = sum(map(float, grades))
    return total_grade

#Getting the report card of the learner
def display_student_report(student, worksheets):
    print(student)

    for sheet_name, worksheet in worksheets.items():
        total_grade = calculate_total_grade(student, worksheet)
        if total_grade is not None:


            print(f"{sheet_name.capitalize()}: {total_grade}%")
        else:

            print(f"{sheet_name.capitalize()}: Student not found")
    main()


# Function to validate student name
def is_valid_student_name(student):
    # Check if the input is a non-empty string
    return isinstance(student, str) and student.strip() != "" and not any(char.isdigit() for char in student)

# Creating starting function to initialize application
def main():
    validData = False

    while not validData:
        student = input("Enter student's full name: ")

        if not is_valid_student_name(student):
            print("Invalid name. Please enter a valid name")
        else:
            validData = True

    # Create a dictionary to set the sheets
    worksheets = {
        'mathematics': SHEET.worksheet('mathematics'),
        'english': SHEET.worksheet('english'),
        'economics': SHEET.worksheet('economics'),
        'social_studies': SHEET.worksheet('socialstudies'),
        'science': SHEET.worksheet('science'),
        'geography': SHEET.worksheet('geography'),
        'history': SHEET.worksheet('history')
    }

    display_student_report(student, worksheets)

if __name__ == "__main__":
    main()