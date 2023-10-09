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

# Create a dictionary to map worksheet names to their respective objects
worksheets = {
    'mathematics': SHEET.worksheet('mathematics'),
    'english': SHEET.worksheet('english'),
    'economics': SHEET.worksheet('economics'),
    'social_studies': SHEET.worksheet('socialstudies'),
    'science': SHEET.worksheet('science'),
    'geography': SHEET.worksheet('geography'),
    'history': SHEET.worksheet('history')
}

def calculate_total_grade(student, worksheet):
    # Find the column containing the student's name
    headers = worksheet.row_values(1)
    try:
        student_column = headers.index(student) + 1
    except ValueError:
        return None

    # Get the grades for the student and calculate the total
    grades = worksheet.col_values(student_column)[1:5]
    total_grade = sum(map(float, grades))
    return total_grade

def display_student_report(student):
    print(student)
    
    # Loop through worksheets and calculate total grades
    for sheet_name, worksheet in worksheets.items():
        total_grade = calculate_total_grade(student, worksheet)
        if total_grade is not None:
            print(f"{sheet_name.capitalize()}: {total_grade}%")
        else:
            print(f"{sheet_name.capitalize()}: Student not found")

def main():
    student = input("Enter student's full name: ")
    display_student_report(student)

if __name__ == "__main__":
    main()