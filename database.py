# ==========================================
# activity.py (Part 1)
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import database


class ActivityWindow:

    def __init__(self, root):

        self.root = tk.Toplevel(root)
        self.root.title("Activity Tracker")
        self.root.geometry("1200x650")
        self.root.configure(bg="white")

        database.connect_db()

        # ================= Variables =================

        self.activity_id = tk.StringVar()
        self.pet_id = tk.StringVar()
        self.activity = tk.StringVar()
        self.duration = tk.StringVar()
        self.calories = tk.StringVar()
        self.date = tk.StringVar()

        # ================= Title =================

        title = tk.Label(
            self.root,
            text="Activity Tracker",
            font=("Arial",22,"bold"),
            bg="#009688",
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

        left.place(x=10,y=60,width=350,height=560)

        fields = [

            ("Pet ID",self.pet_id),
            ("Activity",self.activity),
            ("Duration",self.duration),
            ("Calories Burned",self.calories),
            ("Activity Date",self.date)

        ]

        row = 0

        for text,var in fields:

            tk.Label(
                left,
                text=text,
                bg="white",
                font=("Arial",11,"bold")
            ).grid(row=row,column=0,padx=10,pady=10,sticky="w")

            if text=="Activity":

                ttk.Combobox(

                    left,

                    textvariable=var,

                    values=[
                        "Walking",
                        "Running",
                        "Playing",
                        "Swimming",
                        "Sleeping",
                        "Training"
                    ],

                    state="readonly",
                    width=22

                ).grid(row=row,column=1,padx=5)

            else:

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
            width=10,
            bg="green",
            fg="white",
            command=self.add_activity
        ).grid(row=0,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Update",
            width=10,
            bg="blue",
            fg="white",
            command=self.update_activity
        ).grid(row=0,column=1,padx=5,pady=5)

        tk.Button(
            btn,
            text="Delete",
            width=10,
            bg="red",
            fg="white",
            command=self.delete_activity
        ).grid(row=1,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Search",
            width=10,
            bg="orange",
            fg="white",
            command=self.search_activity
        ).grid(row=1,column=1,padx=5,pady=5)

        tk.Button(
            btn,
            text="View All",
            width=10,
            bg="#009688",
            fg="white",
            command=self.fetch_data
        ).grid(row=2,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="Clear",
            width=10,
            bg="gray",
            fg="white",
            command=self.clear
        ).grid(row=2,column=1,padx=5,pady=5)

        # ================= Right Frame =================

        right = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="ridge"
        )

        right.place(x=370,y=60,width=810,height=560)

        sx = tk.Scrollbar(right,orient="horizontal")
        sy = tk.Scrollbar(right,orient="vertical")

        self.table = ttk.Treeview(

            right,

            columns=(

                "id",
                "petid",
                "activity",
                "duration",
                "calories",
                "date"

            ),

            xscrollcommand=sx.set,
            yscrollcommand=sy.set

        )

        sx.pack(side="bottom",fill="x")
        sy.pack(side="right",fill="y")

        sx.config(command=self.table.xview)
        sy.config(command=self.table.yview)

        headings = [

            ("id","Activity ID"),
            ("petid","Pet ID"),
            ("activity","Activity"),
            ("duration","Duration"),
            ("calories","Calories"),
            ("date","Date")

        ]

        for col,text in headings:

            self.table.heading(col,text=text)
            self.table.column(col,width=120)

        self.table["show"]="headings"

        self.table.pack(fill="both",expand=True)

        self.table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ===================================
    # Add Activity
    # ===================================

    def add_activity(self):

        if self.pet_id.get()=="":

            messagebox.showerror(
                "Error",
                "Pet ID is Required."
            )
            return

        database.add_activity(

            self.pet_id.get(),
            self.activity.get(),
            self.duration.get(),
            self.calories.get(),
            self.date.get()

        )

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Activity Added Successfully."
        )

            # ===================================
    # View All Activities
    # ===================================

    def fetch_data(self):

        rows = database.get_activities()

        self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert("", tk.END, values=row)

    # ===================================
    # Select Record
    # ===================================

    def get_cursor(self, event=""):

        cursor_row = self.table.focus()

        contents = self.table.item(cursor_row)

        row = contents.get("values")

        if not row:
            return

        self.activity_id.set(row[0])
        self.pet_id.set(row[1])
        self.activity.set(row[2])
        self.duration.set(row[3])
        self.calories.set(row[4])
        self.date.set(row[5])

    # ===================================
    # Update Activity
    # ===================================

    def update_activity(self):

        if self.activity_id.get() == "":

            messagebox.showerror(
                "Error",
                "Please select a record."
            )
            return

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE activity
            SET
                pet_id=?,
                activity=?,
                duration=?,
                calories_burned=?,
                activity_date=?
            WHERE activity_id=?
        """,
        (
            self.pet_id.get(),
            self.activity.get(),
            self.duration.get(),
            self.calories.get(),
            self.date.get(),
            self.activity_id.get()
        ))

        conn.commit()
        conn.close()

        self.fetch_data()
        self.clear()

        messagebox.showinfo(
            "Success",
            "Activity Updated Successfully."
        )

    # ===================================
    # Delete Activity
    # ===================================

    def delete_activity(self):

        if self.activity_id.get() == "":

            messagebox.showerror(
                "Error",
                "Please select a record."
            )
            return

        answer = messagebox.askyesno(
            "Delete",
            "Are you sure you want to delete this activity?"
        )

        if answer:

            conn = database.connect_db()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM activity WHERE activity_id=?",
                (self.activity_id.get(),)
            )

            conn.commit()
            conn.close()

            self.fetch_data()
            self.clear()

            messagebox.showinfo(
                "Deleted",
                "Activity Deleted Successfully."
            )

    # ===================================
    # Search Activity
    # ===================================

    def search_activity(self):

        keyword = self.pet_id.get().strip()

        conn = database.connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM activity WHERE pet_id LIKE ?",
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

        self.activity_id.set("")
        self.pet_id.set("")
        self.activity.set("")
        self.duration.set("")
        self.calories.set("")
        self.date.set("")


        # ===================================
# Open Activity Window
# ===================================

def open_activity_window(root):

    ActivityWindow(root)


# ===================================
# Run File Independently
# ===================================

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    ActivityWindow(root)

    root.mainloop()