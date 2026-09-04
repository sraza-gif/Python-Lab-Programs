from database import connect_database


def add_book(book_id, title, author):
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO books (book_id, title, author, status)
            VALUES (?, ?, ?, ?)
        """, (book_id, title, author, "Available"))

        connection.commit()
        return True, "Book added successfully."

    except Exception as e:
        return False, "Error: " + str(e)

    finally:
        connection.close()


def issue_book(book_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT status FROM books WHERE book_id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        connection.close()
        return False, "Book not found."

    if book[0] == "Issued":
        connection.close()
        return False, "Book is already issued."

    cursor.execute("""
        UPDATE books
        SET status = ?
        WHERE book_id = ?
    """, ("Issued", book_id))

    connection.commit()
    connection.close()

    return True, "Book issued successfully."


def return_book(book_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT status FROM books WHERE book_id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        connection.close()
        return False, "Book not found."

    if book[0] == "Available":
        connection.close()
        return False, "Book is already available."

    cursor.execute("""
        UPDATE books
        SET status = ?
        WHERE book_id = ?
    """, ("Available", book_id))

    connection.commit()
    connection.close()

    return True, "Book returned successfully."


def search_book(book_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM books
        WHERE book_id = ?
    """, (book_id,))

    book = cursor.fetchone()

    connection.close()

    return book


def get_all_books():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    connection.close()

    return books