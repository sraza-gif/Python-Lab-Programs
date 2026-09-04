import tkinter as tk
from tkinter import messagebox

from database import create_table
from operations import (
    add_book,
    issue_book,
    return_book,
    search_book,
    get_all_books
)


def add_book_gui():
    try:
        book_id = int(id_entry.get())
        title = title_entry.get()
        author = author_entry.get()

        if title == "" or author == "":
            messagebox.showwarning(
                "Warning",
                "Please enter all details."
            )
            return

        success, message = add_book(book_id, title, author)

        if success:
            messagebox.showinfo("Success", message)

            id_entry.delete(0, tk.END)
            title_entry.delete(0, tk.END)
            author_entry.delete(0, tk.END)

        else:
            messagebox.showerror("Error", message)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Book ID must be a number."
        )


def issue_book_gui():
    try:
        book_id = int(id_entry.get())

        success, message = issue_book(book_id)

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid Book ID."
        )


def return_book_gui():
    try:
        book_id = int(id_entry.get())

        success, message = return_book(book_id)

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid Book ID."
        )


def search_book_gui():
    try:
        book_id = int(id_entry.get())

        book = search_book(book_id)

        if book:
            messagebox.showinfo(
                "Book Details",
                "Book ID: " + str(book[0]) +
                "\nTitle: " + book[1] +
                "\nAuthor: " + book[2] +
                "\nStatus: " + book[3]
            )
        else:
            messagebox.showerror(
                "Error",
                "Book not found."
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid Book ID."
        )


def display_books_gui():
    books = get_all_books()

    if not books:
        messagebox.showinfo(
            "Library",
            "No books available."
        )
        return

    result = ""

    for book in books:
        result += (
            "Book ID: " + str(book[0]) +
            "\nTitle: " + book[1] +
            "\nAuthor: " + book[2] +
            "\nStatus: " + book[3] +
            "\n--------------------------\n"
        )

    messagebox.showinfo("All Books", result)


def main():

    # Create database table
    create_table()

    global id_entry
    global title_entry
    global author_entry

    root = tk.Tk()

    root.title("Library Management System")
    root.geometry("500x550")

    # Heading
    heading = tk.Label(
        root,
        text="Library Management System",
        font=("Arial", 20, "bold")
    )

    heading.pack(pady=20)

    # Book ID
    tk.Label(
        root,
        text="Book ID",
        font=("Arial", 12)
    ).pack()

    id_entry = tk.Entry(
        root,
        width=35
    )

    id_entry.pack(pady=5)

    # Book Title
    tk.Label(
        root,
        text="Book Title",
        font=("Arial", 12)
    ).pack()

    title_entry = tk.Entry(
        root,
        width=35
    )

    title_entry.pack(pady=5)

    # Author
    tk.Label(
        root,
        text="Author",
        font=("Arial", 12)
    ).pack()

    author_entry = tk.Entry(
        root,
        width=35
    )

    author_entry.pack(pady=5)

    # Buttons

    tk.Button(
        root,
        text="Add Book",
        width=25,
        command=add_book_gui
    ).pack(pady=8)

    tk.Button(
        root,
        text="Issue Book",
        width=25,
        command=issue_book_gui
    ).pack(pady=8)

    tk.Button(
        root,
        text="Return Book",
        width=25,
        command=return_book_gui
    ).pack(pady=8)

    tk.Button(
        root,
        text="Search Book",
        width=25,
        command=search_book_gui
    ).pack(pady=8)

    tk.Button(
        root,
        text="Display All Books",
        width=25,
        command=display_books_gui
    ).pack(pady=8)

    # Start GUI
    root.mainloop()


if __name__ == "__main__":
    main()