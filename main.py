# Required before running:
#   'pip install psycopg'
#   'pip install "psycopg[binary,pool]"'

import psycopg


# Variables
db_name = "A3"
db_username = "postgres"
db_password = "tomasteixeira"
db_host = "localhost"
db_port = "5432"


def get_all_students(cur):
    """
    Fetches all student records from the database and prints them.

    Parameters:
    cur (psycopg.cursor): The cursor object for executing SQL queries.

    Returns:
    None
    """
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    for point in data:
        print(point)


def add_student(cur, first_name, last_name, email, enrollment_date):
    """
    Adds a new student record to the database.

    Parameters:
    cur (psycopg.cursor): The cursor object for executing SQL queries.
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    email (str): The email address of the student.
    enrollment_date (str): The enrollment date of the student in 'YYYY-MM-DD' format.

    Returns:
    None
    """
    cur.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date)"
                f"VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")


def update_student_email(cur, student_id, new_email):
    """
    Updates the email of a student record in the database.

    Parameters:
    cur (psycopg.cursor): The cursor object for executing SQL queries.
    student_id (int): The ID of the student whose email is to be updated.
    new_email (str): The new email address for the student.

    Returns:
    None
    """
    cur.execute(f"UPDATE students SET email='{new_email}' WHERE student_id={student_id}")


def delete_student(cur, student_id):
    """
    Deletes a student record from the database.

    Parameters:
    cur (psycopg.cursor): The cursor object for executing SQL queries.
    student_id (int): The ID of the student to be deleted.

    Returns:
    None
    """
    cur.execute(f"DELETE FROM students WHERE student_id={student_id}")


def main():
    # Establish a connection to the database
    connection = psycopg.connect(
        dbname=db_name,
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port
    )

    # Create a cursor object to execute commands
    cursor = connection.cursor()

    while True:
        # Get user's decision
        val = input("Get Student (1), Add Student (2), Update Student Email (3), "
                    "Delete Student (4), Exit and Commit Changes (5) > ")

        # Print all students in the database to the screen
        if val == '1':
            get_all_students(cursor)

        # Get student info and add student to database
        elif val == '2':
            stu_first = input("Student's first name > ")
            stu_last = input("Student's last name > ")
            stu_email = input("Student's email > ")
            stu_date = input("Student's enrollment date (yyyy-mm-dd) > ")
            add_student(cursor, stu_first, stu_last, stu_email, stu_date)

        # Update student's email, if the id exists
        elif val == '3':
            stu_id = input("Student's id > ")
            stu_email = input("Student's new email > ")
            update_student_email(cursor, stu_id, stu_email)

        # Delete the student, if the id exists
        elif val == '4':
            stu_id = input("Student's id > ")
            delete_student(cursor, stu_id)

        # Commit all changes and exit the program
        elif val == '5':
            connection.commit()
            break

        # Invalid input
        else:
            print("Not a valid input.")

    # Closes the cursor
    cursor.close()


# Run on program start
if __name__ == '__main__':
    main()
