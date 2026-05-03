from library import Library

library = Library()

while True:
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("1. Add Book")
    print("2. Student Registration")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Show Books")
    print("7. Show Students")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.register_student()

    elif choice == 3:
        library.search_book()

    elif choice == 4:
        library.issue_book()

    elif choice == 5:
        library.return_book()

    elif choice == 6:
        library.show_books()

    elif choice == 7:
        library.show_students()

    elif choice == 8:
        print("Thank you for using Library Management System")
        break

    else:
        print("Invalid choice")