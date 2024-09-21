import sqlite3

connection=sqlite3.connect('example.db')
cursor=connection.cursor()
cursor.execute('''
create table if not exists employees(
    id integer primary key autoincrement,
    name text not null,
    position text not null,
    department text not null,
    salary real
)
''')

cursor.execute('''
insert into employees(name, position, department, salary)
values(?,?,?,?)
''',('Rron Miftari','Software Engineer','IT',9000.00))

connection.commit()

cursor.execute('Select * from employees')

row=cursor.fetchall()
for row in row:
    print(row)

cursor.close()
connection.close()