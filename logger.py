# ==========================================
# health_analyzer.py
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class HealthAnalyzer:

    def __init__(self, root):

        self.window = tk.Toplevel(root)
        self.window.title("Pet Health Analyzer")
        self.window.geometry("700x550")
        self.window.configure(bg="white")

        title = tk.Label(
            self.window,
            text="Pet Health Analyzer",
            font=("Arial",22,"bold"),
            bg="#4CAF50",
            fg="white",
            pady=10
        )

        title.pack(fill="x")

        form = tk.Frame(self.window,bg="white")
        form.pack(pady=20)

        self.pet_id = tk.StringVar()

        tk.Label(
            form,
            text="Pet ID",
            font=("Arial",12,"bold"),
            bg="white"
        ).grid(row=0,column=0,padx=10,pady=10)

        tk.Entry(
            form,
            textvariable=self.pet_id,
            width=20
        ).grid(row=0,column=1)

        tk.Button(

            form,

            text="Analyze",

            bg="green",

            fg="white",

            width=15,

            command=self.analyze_health

        ).grid(row=0,column=2,padx=20)

        self.result = tk.Text(
            self.window,
            width=80,
            height=20,
            font=("Arial",11)
        )

        self.result.pack(pady=20)

    # =====================================
    # Analyze Health
    # =====================================

    def analyze_health(self):

        if self.pet_id.get()=="":

            messagebox.showerror(
                "Error",
                "Enter Pet ID"
            )

            return

        conn = sqlite3.connect("petcare.db")

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT age,weight
            FROM pets
            WHERE pet_id=?
            """,

            (self.pet_id.get(),)

        )

        pet = cursor.fetchone()

        if pet is None:

            messagebox.showerror(
                "Error",
                "Pet Not Found"
            )

            conn.close()

            return

        age = pet[0]
        weight = pet[1]

        score = 100

        remarks = []

        # Age Analysis

        if age >= 10:

            score -= 20
            remarks.append("Senior Pet")

        elif age >= 7:

            score -= 10
            remarks.append("Adult Pet")

        else:

            remarks.append("Young Pet")

        # Weight Analysis

        if weight < 3:

            score -= 15
            remarks.append("Under Weight")

        elif weight > 35:

            score -= 15
            remarks.append("Over Weight")

        else:

            remarks.append("Normal Weight")

        # Medical Records

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM medical
            WHERE pet_id=?
            """,
            (self.pet_id.get(),)
        )

        medical_count = cursor.fetchone()[0]

        if medical_count > 0:

            score -= medical_count * 2

            remarks.append(
                f"{medical_count} Medical Records"
            )

        # Activity Records

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM activity
            WHERE pet_id=?
            """,
            (self.pet_id.get(),)
        )

        activity = cursor.fetchone()[0]

        if activity >= 5:

            score += 5
            remarks.append("Active Lifestyle")

        else:

            remarks.append("Needs More Exercise")

        # Nutrition Records

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM nutrition
            WHERE pet_id=?
            """,
            (self.pet_id.get(),)
        )

        nutrition = cursor.fetchone()[0]

        if nutrition >= 5:

            score += 5
            remarks.append("Healthy Diet")

        else:

            remarks.append("Improve Nutrition")

        conn.close()

        if score > 100:
            score = 100

        if score < 0:
            score = 0

        if score >= 90:

            status = "Excellent"

        elif score >= 75:

            status = "Good"

        elif score >= 60:

            status = "Average"

        else:

            status = "Poor"

        self.result.delete("1.0",tk.END)

        self.result.insert(
            tk.END,
            "=========== HEALTH REPORT ===========\n\n"
        )

        self.result.insert(
            tk.END,
            f"Pet ID : {self.pet_id.get()}\n\n"
        )

        self.result.insert(
            tk.END,
            f"Health Score : {score}/100\n\n"
        )

        self.result.insert(
            tk.END,
            f"Health Status : {status}\n\n"
        )

        self.result.insert(
            tk.END,
            "Recommendations\n"
        )

        self.result.insert(
            tk.END,
            "--------------------------\n"
        )

        for item in remarks:

            self.result.insert(
                tk.END,
                "• "+item+"\n"
            )

        self.result.insert(
            tk.END,
            "\nKeep regular vaccination,\n"
        )

        self.result.insert(
            tk.END,
            "Provide healthy food,\n"
        )

        self.result.insert(
            tk.END,
            "Regular exercise,\n"
        )

        self.result.insert(
            tk.END,
            "Routine veterinary check-up.\n"
        )


# =======================================
# Open Window
# =======================================

def open_health_window(root):

    HealthAnalyzer(root)


# =======================================
# Run Independently
# =======================================

if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    HealthAnalyzer(root)

    root.mainloop()