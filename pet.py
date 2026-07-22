# ==========================================
# nutrition.py (Part 1)
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import database


class NutritionWindow:

    def __init__(self, root):

        self.root = tk.Toplevel(root)
        self.root.title("Nutrition Management")
        self.root.geometry("1200x650")
        self.root.configure(bg="white")

        database.connect_db()

        # ================= Variables =================

        self.nutrition_id = tk.StringVar()
        self.pet_id = tk.StringVar()
        self.food = tk.StringVar()
        self.quantity = tk.StringVar()
        self.calories = tk.StringVar()
        self.water = tk.StringVar()
        self.feeding_time = tk.StringVar()

        # ================= Title =================

        title = tk.Label(
            self.root,
            text="Nutrition Management",
            font=("Arial", 22, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10
        )
        title.pack(fill="x")

        # ================= Left Frame =================

        left = tk.Frame(self.root, bg="white", bd=2, relief="ridge")
        left.place(x=10, y=60, width=350, height=560)

        fields = [
            ("Pet ID", self.pet_id),
            ("Food", self.food),
            ("Quantity", self.quantity),
            ("Calories", self.calories),
            ("Water Intake", self.water),
            ("Feeding Time", self.feeding_time)
        ]

        row = 0

        for text, var in fields:

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

        btn = tk.Frame(left,bg="white")
        btn.grid(row=7,columnspan=2,pady=20)

        tk.Button(
            btn,
            text="Add",
            bg="green",
            fg="white",
            width=10,
            command=self.add_record
        ).grid(row=0,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Update",
            bg="blue",
            fg="white",
            width=10,
            command=self.update_record
        ).grid(row=0,column=1,padx=5,pady=5)

        tk.Button(
            btn,
            text="Delete",
            bg="red",
            fg="white",
            width=10,
            command=self.delete_record
        ).grid(row=1,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Search",
            bg="orange",
            fg="white",
            width=10,
            command=self.search_record
        ).grid(row=1,column=1,padx=5,pady=5)

        tk.Button(
            btn,
            text="View All",
            bg="#009688",
            fg="white",
            width=10,
            command=self.fetch_data
        ).grid(row=2,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Clear",
            bg="gray",
            fg="white",
            width=10,
            command=self.clear
        ).grid(row=2,column=1,padx=5,pady=5)

        # ================= Right Frame =================

        right = tk.Frame(self.root, bg="white", bd=2, relief="ridge")
        right.place(x=370,y=60,width=810,height=560)

        sx = tk.Scrollbar(right, orient="horizontal")
        sy = tk.Scrollbar(right, orient="vertical")

        self.table = ttk.Treeview(
            right,
            columns=(
                "id",
                "petid",
                "food",
                "quantity",
                "calories",
                "water",
                "time"
            ),
            xscrollcommand=sx.set,
            yscrollcommand=sy.set
        )

        sx.pack(side="bottom",fill="x")
        sy.pack(side="right",fill="y")

        sx.config(command=self.table.xview)
        sy.config(command=self.table.yview)

        headings = [
            ("id","Nutrition ID"),
            ("petid","Pet ID"),
            ("food","Food"),
            ("quantity","Quantity"),
            ("calories","Calories"),
            ("water","Water"),
            ("time","Feeding Time")
        ]

        for col,text in headings:
            self.table.heading(col,text=text)
            self.table.column(col,width=120)

        self.table["show"]="headings"
        self.table.pack(fill="both",expand=True)

        self.table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ==========================
    # Add Nutrition Record
    # ==========================

    def add_record(self):

        if self.pet_id.get()=="":

            messagebox.showerror(
                "Error",
                "Pet ID is Required"
            )
            return

        database.add_nutrition(
            self.pet_id.get(),
            self.food.get(),
            self.quantity.get(),
            self.calories.get(),
            self.water.get(),
            self.feeding_time.get()
        )

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Nutrition Record Added Successfully"
        )
    # ===================================
    # Fetch Data
    # ===================================

    def fetch_data(self):

        rows = database.get_nutrition()

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

        self.nutrition_id.set(row[0])
        self.pet_id.set(row[1])
        self.food.set(row[2])
        self.quantity.set(row[3])
        self.calories.set(row[4])
        self.water.set(row[5])
        self.feeding_time.set(row[6])

    # ===================================
    # Update Nutrition Record
    # ===================================

    def update_record(self):

        if self.nutrition_id.get() == "":

            messagebox.showerror(
                "Error",
                "Please select a record."
            )
            return

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE nutrition
        SET
            pet_id=?,
            food=?,
            quantity=?,
            calories=?,
            water=?,
            feeding_time=?
        WHERE nutrition_id=?
        """,
        (
            self.pet_id.get(),
            self.food.get(),
            self.quantity.get(),
            self.calories.get(),
            self.water.get(),
            self.feeding_time.get(),
            self.nutrition_id.get()
        ))

        conn.commit()
        conn.close()

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Nutrition Record Updated Successfully."
        )

    # ===================================
    # Delete Nutrition Record
    # ===================================

    def delete_record(self):

        if self.nutrition_id.get() == "":

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
                "DELETE FROM nutrition WHERE nutrition_id=?",
                (self.nutrition_id.get(),)
            )

            conn.commit()
            conn.close()

            self.fetch_data()
            self.clear()

            messagebox.showinfo(
                "Deleted",
                "Nutrition Record Deleted Successfully."
            )

    # ===================================
    # Search Nutrition Record
    # ===================================

    def search_record(self):

        keyword = self.pet_id.get().strip()

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM nutrition WHERE pet_id LIKE ?",
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

        self.nutrition_id.set("")
        self.pet_id.set("")
        self.food.set("")
        self.quantity.set("")
        self.calories.set("")
        self.water.set("")
        self.feeding_time.set("")

# ===================================
# Open Nutrition Window
# ===================================

def open_nutrition_window(root):

    NutritionWindow(root)


# ===================================
# Run this file directly
# ===================================

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    NutritionWindow(root)

    root.mainloop()