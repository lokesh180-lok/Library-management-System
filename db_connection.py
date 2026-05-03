import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lokesh1234",
    database="library"
)

cur = conn.cursor()

cur.execute("""
create table if not exists books(
    book_id int primary key auto_increment,
    title varchar(100) not null,
    author VARCHAR(100) not null,
    quantity int not null
)
""")

cur.execute("""
create table if not exists students(
    student_id int primary key auto_increment,
    name varchar(100) not null,
    email varchar(100) unique not null
)
""")

cur.execute("""
create table if not exists issued_books(
    issue_id int primary key auto_increment,
    book_id int not null,
    student_id int not null,
    issue_date date,
    return_date date,
    status varchar(20)
)
""")

conn.commit()

print("Database connected successfully")