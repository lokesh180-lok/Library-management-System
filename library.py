from db_connection import conn, cur
from datetime import date

class Library:

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter quantity: "))

        query = "insert into books(title, author, quantity) VALUES(%s, %s, %s)"
        values = (title, author, quantity)

        cur.execute(query, values)
        conn.commit()

        print("Book added successfully")

    def register_student(self):
        name = input("Enter student name: ")
        email = input("Enter student email: ")

        cur.execute("SELECT * FROM students WHERE email=%s", (email,))
        result = cur.fetchone()

        if result:
            print("Student already registered")
        else:
            cur.execute(
                "insert into students(name, email) VALUES(%s, %s)",
                (name, email)
            )
            conn.commit()
            print("Student registered successfully")

    def search_book(self):
        title = input("Enter book title to search: ")

        cur.execute("select * from books where title like %s", ("%" + title + "%",))
        books = cur.fetchall()

        if books:
            print("Available Books:")
            for book in books:
                print(book)
        else:
            print("Book not found")

    def issue_book(self):
        book_id = int(input("Enter book ID: "))
        student_id = int(input("Enter student ID: "))

        cur.execute("select quantity from books where book_id=%s", (book_id,))
        book = cur.fetchone()

        if book:
            if book[0] > 0:
                today = date.today()

                cur.execute("""
                insert into issued_books(book_id, student_id, issue_date, status)
                values(%s, %s, %s, %s)""", (book_id, student_id, today, "Issued"))

                cur.execute(
                    "update books set quantity = quantity - 1 where book_id=%s",
                    (book_id,)
                )

                conn.commit()
                print("Book issued successfully")
            else:
                print("Book is not available")
        else:
            print("Invalid book ID")

    def return_book(self):
        issue_id = int(input("Enter issue ID: "))

        cur.execute("""
        select book_id, issue_date, status 
        from issued_books 
        Where issue_id=%s
        """, (issue_id,))

        issued = cur.fetchone()

        if issued:
            book_id = issued[0]
            issue_date = issued[1]
            status = issued[2]

            if status == "Returned":
                print("Book already returned")
            else:
                today = date.today()
                days = (today - issue_date).days

                fine = 0
                if days > 7:
                    fine = (days - 7) * 5

                cur.execute("""
                update issued_books 
                set return_date=%s, status=%s 
                where issue_id=%s""", (today, "Returned", issue_id))

                cur.execute(
                    "update books set quantity = quantity + 1 where book_id=%s",
                    (book_id,)
                )

                conn.commit()

                print("Book returned successfully")
                print("Total days:", days)
                print("Fine amount: ", fine)
        else:
            print("Invalid issue ID")

    def show_books(self):
        cur.execute("select * from books")
        books = cur.fetchall()

        print("Books Table:")
        for book in books:
            print(book)

    def show_students(self):
        cur.execute("select * from students")
        students = cur.fetchall()

        print("Students Table:")
        for student in students:
            print(student)