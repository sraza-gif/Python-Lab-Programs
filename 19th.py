import sqlite3
import tkinter as tk
from tkinter import messagebox


def create_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    """)

    conn.commit()
    conn.close()


def add_book():
    book_id = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()

    if book_id == "" or title == "" or author == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO books(book_id, title, author)
            VALUES (?, ?, ?)
        """, (int(book_id), title, author))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Book added successfully.")

        clear_fields()

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Book ID already exists.")


def issue_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showwarning("Warning", "Enter Book ID.")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET status = 'Issued'
        WHERE book_id = ? AND status = 'Available'
    """, (int(book_id),))

    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Book issued successfully.")
    else:
        messagebox.showerror(
            "Error",
            "Book not found or already issued."
        )

    conn.close()


def return_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showwarning("Warning", "Enter Book ID.")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET status = 'Available'
        WHERE book_id = ? AND status = 'Issued'
    """, (int(book_id),))

    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Book returned successfully.")
    else:
        messagebox.showerror(
            "Error",
            "Book not found or it was not issued."
        )

    conn.close()


def search_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showwarning("Warning", "Enter Book ID.")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT book_id, title, author, status
        FROM books
        WHERE book_id = ?
    """, (int(book_id),))

    book = cursor.fetchone()

    conn.close()

    if book:
        messagebox.showinfo(
            "Book Details",
            f"Book ID: {book[0]}\n"
            f"Title: {book[1]}\n"
            f"Author: {book[2]}\n"
            f"Status: {book[3]}"
        )
    else:
        messagebox.showerror("Error", "Book not found.")


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)


def main():
    global entry_id, entry_title, entry_author

    create_database()

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x350")

    tk.Label(
        root,
        text="Library Management System",
        font=("Arial", 16)
    ).pack(pady=15)

    tk.Label(root, text="Book ID").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Label(root, text="Book Title").pack()
    entry_title = tk.Entry(root)
    entry_title.pack()

    tk.Label(root, text="Author").pack()
    entry_author = tk.Entry(root)
    entry_author.pack()

    tk.Button(
        root,
        text="Add Book",
        command=add_book
    ).pack(pady=5)

    tk.Button(
        root,
        text="Issue Book",
        command=issue_book
    ).pack(pady=5)

    tk.Button(
        root,
        text="Return Book",
        command=return_book
    ).pack(pady=5)

    tk.Button(
        root,
        text="Search Book",
        command=search_book
    ).pack(pady=5)

    tk.Button(
        root,
        text="Clear",
        command=clear_fields
    ).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()