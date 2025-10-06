import tkinter as tk
from tkinter import messagebox
import sqlite3
import re # Will be used for validation

# --- COMMIT 1: Initial Setup and Database Creation ---
# Reason: This is the foundational step. At this point, you have a script that
# can successfully create the database and the necessary table. It's a stable,
# testable base for the rest of the application. The program runs without error,
# even though it doesn't do much visually yet.

def setup_database():
    """Connects to the SQLite database and creates the customers table if it doesn't exist."""
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- End of COMMIT 1 ---


class CustomerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Information Management")
        self.root.geometry("450x400") # Set a default size

        # --- COMMIT 2: GUI Layout and Widget Creation ---
        # Reason: The entire user interface is now visually laid out. All labels,
        # entry fields, the dropdown menu, and the submit button are present.
        # Although they don't have functionality yet, this commit captures the
        # complete static design of the GUI. It separates the "look" from the "feel".

        # Main frame with padding
        main_frame = tk.Frame(root, padx=15, pady=15)
        main_frame.pack(fill="both", expand=True)

        # Configure grid layout
        main_frame.columnconfigure(1, weight=1)

        # --- Labels and Entry Fields ---
        # Name
        tk.Label(main_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(main_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew")

        # Birthday
        tk.Label(main_frame, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", pady=5)
        self.birthday_entry = tk.Entry(main_frame)
        self.birthday_entry.grid(row=1, column=1, sticky="ew")

        # Email
        tk.Label(main_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(main_frame)
        self.email_entry.grid(row=2, column=1, sticky="ew")

        # Phone
        tk.Label(main_frame, text="Phone Number:").grid(row=3, column=0, sticky="w", pady=5)
        self.phone_entry = tk.Entry(main_frame)
        self.phone_entry.grid(row=3, column=1, sticky="ew")

        # Address
        tk.Label(main_frame, text="Address:").grid(row=4, column=0, sticky="w", pady=5)
        self.address_entry = tk.Entry(main_frame)
        self.address_entry.grid(row=4, column=1, sticky="ew")

        # Preferred Contact Method
        tk.Label(main_frame, text="Contact Method:").grid(row=5, column=0, sticky="w", pady=5)
        self.contact_method = tk.StringVar(value="Email") # Default value
        contact_options = ["Email", "Phone", "Mail"]
        self.contact_menu = tk.OptionMenu(main_frame, self.contact_method, *contact_options)
        self.contact_menu.grid(row=5, column=1, sticky="ew")

        # Submit Button
        self.submit_button = tk.Button(main_frame, text="Submit", command=self.submit_data, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
        self.submit_button.grid(row=6, columnspan=2, pady=20, sticky="ew")

        # --- End of COMMIT 2 ---


    # --- COMMIT 3: Implement Core Submit Functionality ---
    # Reason: This is the most significant functional part of the app. The submit button
    # now works as intended: it gathers data from the fields, connects to the database,
    # inserts a new record, and clears the form. The application is now fully functional
    # for its primary purpose.

    def submit_data(self):
        """Gathers data from the GUI, validates it, inserts it into the database, and clears the form."""
        if not self.validate_inputs():
            return # Stop submission if validation fails

        try:
            conn = sqlite3.connect('customer_data.db')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO customers (name, birthday, email, phone, address, contact_method)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                self.name_entry.get(),
                self.birthday_entry.get(),
                self.email_entry.get(),
                self.phone_entry.get(),
                self.address_entry.get(),
                self.contact_method.get()
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Customer information submitted successfully!")
            self.clear_form()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def clear_form(self):
        """Clears all the entry fields in the GUI."""
        self.name_entry.delete(0, tk.END)
        self.birthday_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_method.set("Email") # Reset to default

    # --- End of COMMIT 3 ---


    # --- COMMIT 4: Add Data Validation ---
    # Reason: This commit adds a layer of robustness. The application no longer
    # blindly accepts any input. It now checks for a required name and a valid
    # email format. This is a distinct feature enhancement that improves data
    # integrity and user experience without changing the core functionality.

    def validate_inputs(self):
        """Validates the user inputs before database submission."""
        name = self.name_entry.get()
        email = self.email_entry.get()

        if not name.strip():
            messagebox.showwarning("Validation Error", "Name is a required field.")
            return False

        # Simple regex for email validation
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Validation Error", "Please enter a valid email address.")
            return False
        
        # You could add more validation here (e.g., for phone or date format)

        return True

    # --- End of COMMIT 4 ---


if __name__ == '__main__':
    # --- COMMIT 5: Final Application Assembly and Refinements ---
    # Reason: This is the final step that brings everything together. It sets up
    # the main application loop, instantiates the class, and runs the database setup.
    # Minor tweaks, comments, and code cleanup would also fit well in this commit.
    # It finalizes the project into a complete, runnable state.

    setup_database()  # Ensure the database and table exist on startup
    root = tk.Tk()
    app = CustomerApp(root)
    root.mainloop()

    # --- End of COMMIT 5 ---
