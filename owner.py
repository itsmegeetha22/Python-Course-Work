# ==========================================
# medical.py (Part 1)
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import database


class MedicalWindow:

    def __init__(self, root):

        self.root = tk.Toplevel(root)
        self.root.title("Medical Records")
        self.root.geometry("1200x650")
        self.root.configure(bg="white")

        database.connect_db()

        # ================= Variables =================

        self.record_id = tk.StringVar()
        self.pet_id = tk.StringVar()
        self.vaccination = tk.StringVar()
        self.disease = tk.StringVar()
        self.medicine = tk.StringVar()
        self.veterinarian = tk.StringVar()
        self.visit_date = tk.StringVar()
        self.notes = tk.StringVar()

        # ================= Title =================

        title = tk.Label(
            self.root,
            text="Medical Records",
            font=("Arial",22,"bold"),
            bg="#2196F3",
            fg="white",
            pady=10
        )

        title.pack(fill="x")

        # ================= Left Frame =================

        left = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="ridge"
        )

        left.place(x=10,y=60,width=360,height=560)

        labels = [

            ("Pet ID",self.pet_id),
            ("Vaccination",self.vaccination),
            ("Disease",self.disease),
            ("Medicine",self.medicine),
            ("Veterinarian",self.veterinarian),
            ("Visit Date",self.visit_date),
            ("Notes",self.notes)

        ]

        row = 0

        for text,var in labels:

            tk.Label(
                left,
                text=text,
                bg="white",
                font=("Arial",11,"bold")
            ).grid(row=row,column=0,padx=10,pady=10,sticky="w")

            tk.Entry(
                left,
                textvariable=var,
                width=25
            ).grid(row=row,column=1,padx=5)

            row += 1

        # ================= Buttons =================

        btn_frame = tk.Frame(left,bg="white")
        btn_frame.grid(row=8,columnspan=2,pady=20)

        tk.Button(
            btn_frame,
            text="Add",
            bg="green",
            fg="white",
            width=10,
            command=self.add_record
        ).grid(row=0,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Update",
            bg="blue",
            fg="white",
            width=10,
            command=self.update_record
        ).grid(row=0,column=1,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Delete",
            bg="red",
            fg="white",
            width=10,
            command=self.delete_record
        ).grid(row=1,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Search",
            bg="orange",
            fg="white",
            width=10,
            command=self.search_record
        ).grid(row=1,column=1,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="View All",
            bg="#009688",
            fg="white",
            width=10,
            command=self.fetch_data
        ).grid(row=2,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Clear",
            bg="gray",
            fg="white",
            width=10,
            command=self.clear
        ).grid(row=2,column=1,padx=5,pady=5)

        # ================= Right Frame =================

        right = tk.Frame(
            self.root,
            bd=2,
            relief="ridge",
            bg="white"
        )

        right.place(x=380,y=60,width=800,height=560)

        scroll_x = tk.Scrollbar(right,orient="horizontal")
        scroll_y = tk.Scrollbar(right,orient="vertical")

        self.table = ttk.Treeview(

            right,

            columns=(

                "id",
                "petid",
                "vaccination",
                "disease",
                "medicine",
                "vet",
                "date",
                "notes"

            ),

            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set

        )

        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        headings = [

            ("id","Record ID"),
            ("petid","Pet ID"),
            ("vaccination","Vaccination"),
            ("disease","Disease"),
            ("medicine","Medicine"),
            ("vet","Veterinarian"),
            ("date","Visit Date"),
            ("notes","Notes")

        ]

        for col,text in headings:

            self.table.heading(col,text=text)
            self.table.column(col,width=120)

        self.table["show"]="headings"

        self.table.pack(fill="both",expand=1)

        self.table.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

        self.fetch_data()

    # ===================================
    # Add Medical Record
    # ===================================

    def add_record(self):

        if self.pet_id.get()=="":

            messagebox.showerror(
                "Error",
                "Pet ID is required."
            )

            return

        database.add_medical(

            self.pet_id.get(),
            self.vaccination.get(),
            self.disease.get(),
            self.medicine.get(),
            self.veterinarian.get(),
            self.visit_date.get(),
            self.notes.get()

        )

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Medical Record Added Successfully."
        )

            # ===================================
    # Fetch Medical Records
    # ===================================
    def fetch_data(self):

        rows = database.get_medical_records()

        self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert("", tk.END, values=row)

    # ===================================
    # Select Row
    # ===================================
    def get_cursor(self, event=""):

        cursor_row = self.table.focus()

        contents = self.table.item(cursor_row)

        row = contents.get("values")

        if not row:
            return

        self.record_id.set(row[0])
        self.pet_id.set(row[1])
        self.vaccination.set(row[2])
        self.disease.set(row[3])
        self.medicine.set(row[4])
        self.veterinarian.set(row[5])
        self.visit_date.set(row[6])
        self.notes.set(row[7])

    # ===================================
    # Update Record
    # ===================================
    def update_record(self):

        if self.record_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please select a record."
            )
            return

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE medical
        SET
            pet_id=?,
            vaccination=?,
            disease=?,
            medicine=?,
            veterinarian=?,
            visit_date=?,
            notes=?
        WHERE record_id=?
        """,
        (
            self.pet_id.get(),
            self.vaccination.get(),
            self.disease.get(),
            self.medicine.get(),
            self.veterinarian.get(),
            self.visit_date.get(),
            self.notes.get(),
            self.record_id.get()
        ))

        conn.commit()
        conn.close()

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Medical Record Updated Successfully."
        )

    # ===================================
    # Delete Record
    # ===================================
    def delete_record(self):

        if self.record_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please select a record."
            )
            return

        answer = messagebox.askyesno(
            "Delete",
            "Are you sure you want to delete this record?"
        )

        if answer:

            conn = database.connect_db()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM medical WHERE record_id=?",
                (self.record_id.get(),)
            )

            conn.commit()
            conn.close()

            self.fetch_data()
            self.clear()

            messagebox.showinfo(
                "Deleted",
                "Medical Record Deleted Successfully."
            )

    # ===================================
    # Search Record
    # ===================================
    def search_record(self):

        keyword = self.pet_id.get().strip()

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM medical WHERE pet_id LIKE ?",
            ('%' + keyword + '%',)
        )

        rows = cursor.fetchall()

        conn.close()

        self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert("", tk.END, values=row)

    # ===================================
    # Clear Fields
    # ===================================
    def clear(self):

        self.record_id.set("")
        self.pet_id.set("")
        self.vaccination.set("")
        self.disease.set("")
        self.medicine.set("")
        self.veterinarian.set("")
        self.visit_date.set("")
        self.notes.set("")


# ===================================
# Open Medical Window
# ===================================

def open_medical_window(root):
    MedicalWindow(root)


# ===================================
# Run Independently
# ===================================

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    MedicalWindow(root)

    root.mainloop()