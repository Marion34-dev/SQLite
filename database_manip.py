import sqlite3

# Creating database and cursor
db = sqlite3.connect('students_database')
cursor = db.cursor()

# Creating table
cursor.execute('''CREATE TABLE if not exists python_programming(
ID int PRIMARY KEY not null,
Name varchar not null,
Grade int)
;''')
db.commit()

# Inserting rows into the table
student1 = f'''insert into python_programming
values(55, "Carl Davis", 61);'''

student2 = f'''insert into python_programming
values(66, "Dennis Fredrickson", 88);'''

student3 = f'''insert into python_programming
values(77, "Jane Richards", 78);'''

student4 = f'''insert into python_programming
values(12, "Peyton Sawyer", 45);'''

student5 = f'''insert into python_programming
values(2, "Lucas Brooke", 99);'''

cursor.execute(student1)
cursor.execute(student2)
cursor.execute(student3)
cursor.execute(student4)
cursor.execute(student5)
print(f"All students have been successfully inserted")

# Select (and print) all records with a grade between 60 and 80
records = cursor.execute('SELECT * FROM python_programming WHERE grade >= 60 and grade <= 80;')
print(f"The records with a grade between 60 and 80 are as follows: {records.fetchall()}")

# Change Carl's grade to 65 (and print his updated record)
cursor.execute('''UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis";''')
print("Carl's grade was successfully updated")
rec_updated = cursor.execute('SELECT * FROM python_programming WHERE name = "Carl Davis"')
print(rec_updated.fetchall())

# Delete Dennis's row (and print updated table)
cursor.execute('''DELETE FROM python_programming WHERE name = "Dennis Fredrickson"''')
print("Row successfully deleted")
new_table = cursor.execute('SELECT * FROM python_programming')
print(new_table.fetchall())

# Add 1 to the grade of people with an ID < 55 and print their records
cursor.execute('''UPDATE python_programming SET grade = grade + 1 WHERE ID < 55''')
print("The grade from students with an ID below 55 have been updated")
new_grades = cursor.execute('SELECT * FROM python_programming WHERE ID <55')
print(f"They are now as follows: {new_grades.fetchall()}")

db.commit()
db.close()