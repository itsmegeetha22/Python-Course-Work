# ==========================================
# PetCareAI - Main Dashboard
# main.py
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

# Import project modules
try:
    import pet
    import owner
    import medical
    import nutrition
    import activity
    import reminder
    import reports
    import visualization
    import health_analyzer
except ImportError:
    pass


class PetCareAI:

    def __init__(self, root):

        self.root = root
        self.root.title("PetCareAI")
        self.root.geometry("1000x650")
        self.root.configure(bg="#EAF7FF")

        self.create_header()
        self.create_menu()
        self.create_dashboard()
        self.create_statusbar()

    # ---------------- Header ---------------- #

    def create_header(self):

        title = tk.Label(
            self.root,
            text="🐶 PetCareAI",
            font=("Arial", 28, "bold"),
            bg="#2196F3",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

    # ---------------- Menu ---------------- #

    def create_menu(self):

        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(
            label="About",
            command=self.about
        )

        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

    # ---------------- Dashboard ---------------- #

    def create_dashboard(self):

        frame = tk.Frame(self.root, bg="#EAF7FF")
        frame.pack(pady=30)

        buttons = [

            ("Pet Management", self.pet_window),

            ("Medical Records", self.medical_window),
            ("Nutrition Tracker", self.nutrition_window),

            ("Activity Tracker", self.activity_window),
            ("Reminder", self.reminder_window),

            ("Health Analyzer", self.health_window),
            ("Visualization", self.visual_window),

            ("Reports", self.report_window),
            ("Exit", self.root.quit)

        ]

        row = 0
        col = 0

        for text, command in buttons:

            btn = tk.Button(
                frame,
                text=text,
                width=25,
                height=2,
                bg="#4CAF50",
                fg="white",
                font=("Arial", 12, "bold"),
                command=command
            )

            btn.grid(row=row, column=col, padx=20, pady=20)

            col += 1

            if col == 2:
                col = 0
                row += 1

    # ---------------- Status Bar ---------------- #

    def create_statusbar(self):

        status = tk.Label(
            self.root,
            text="Welcome to PetCareAI",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#D9EDF7"
        )

        status.pack(side=tk.BOTTOM, fill=tk.X)

    # ---------------- About ---------------- #

    def about(self):

        messagebox.showinfo(
            "About",
            "PetCareAI\n\nDeveloped using Python Tkinter"
        )

    # ---------------- Button Functions ---------------- #

    def pet_window(self):

        try:
            pet.open_pet_window(self.root)
        except:
            messagebox.showinfo("Info", "Pet Module Not Created Yet")


    def medical_window(self):

        try:
            medical.open_medical_window(self.root)
        except:
            messagebox.showinfo("Info", "Medical Module Not Created Yet")

    def nutrition_window(self):

        try:
            nutrition.open_nutrition_window(self.root)
        except:
            messagebox.showinfo("Info", "Nutrition Module Not Created Yet")

    def activity_window(self):

        try:
            activity.open_activity_window(self.root)
        except:
            messagebox.showinfo("Info", "Activity Module Not Created Yet")

    def reminder_window(self):

        try:
            reminder.open_reminder_window(self.root)
        except:
            messagebox.showinfo("Info", "Reminder Module Not Created Yet")

    def health_window(self):

        try:
            health_analyzer.open_health_window(self.root)
        except:
            messagebox.showinfo("Info", "Health Analyzer Module Not Created Yet")

    def visual_window(self):

        try:
            visualization.open_visualization_window(self.root)
        except:
            messagebox.showinfo("Info", "Visualization Module Not Created Yet")

    def report_window(self):

        try:
            reports.open_report_window(self.root)
        except:
            messagebox.showinfo("Info", "Reports Module Not Created Yet")


# ---------------- Main ---------------- #

if __name__ == "__main__":

    root = tk.Tk()

    app = PetCareAI(root)

    root.mainloop()