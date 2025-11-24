import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
print("------------------------------------\n")


# empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW")
    print("A- Add Information\nB- Print All Record\nC- Search Student Record\nD- Delete a Student Record\nE- Edit Student Record\nF- Export Data\nG- Exit")
    choice = input("Your choice     --> ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("------------------------------------ ")
        student_id = input("Key search for this student use this pattern(course-IDNO) --> ")

        first_name = input("Input Student First Name --> ").upper()
        last_name = input("Input Student Last Name --> ").upper()
        course = input ("Input Student Course --> ").upper()
        email = input("Input Student email address --> ")
        issingle = input("Are you single (True or False ) --> ")

        student_records(student_id, [first_name, last_name, course, email, issingle])
        print("DATA SAVED")   