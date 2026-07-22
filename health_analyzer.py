# ==========================================
# PetCareAI
# database.py (Part 1)
# ==========================================

import sqlite3

DB_NAME = "petcare.db"


# ==========================================
# Database Connection
# ==========================================

def connect_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    # -------------------------------
    # Pet Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets(

        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        species TEXT NOT NULL,

        breed TEXT,

        age INTEGER,

        gender TEXT,

        weight REAL,

        owner_name TEXT,

        contact TEXT

    )
    """)

    # -------------------------------
    # Medical Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical(

        record_id INTEGER PRIMARY KEY AUTOINCREMENT,

        pet_id INTEGER,

        vaccination TEXT,

        disease TEXT,

        medicine TEXT,

        veterinarian TEXT,

        visit_date TEXT,

        notes TEXT,

        FOREIGN KEY(pet_id)
        REFERENCES pets(pet_id)

    )
    """)

    # -------------------------------
    # Nutrition Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nutrition(

        nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT,

        pet_id INTEGER,

        food TEXT,

        quantity TEXT,

        calories INTEGER,

        water TEXT,

        feeding_time TEXT,

        FOREIGN KEY(pet_id)
        REFERENCES pets(pet_id)

    )
    """)

    # -------------------------------
    # Activity Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity(

        activity_id INTEGER PRIMARY KEY AUTOINCREMENT,

        pet_id INTEGER,

        activity TEXT,

        duration TEXT,

        calories_burned INTEGER,

        activity_date TEXT,

        FOREIGN KEY(pet_id)
        REFERENCES pets(pet_id)

    )
    """)

    # -------------------------------
    # Reminder Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminder(

        reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,

        pet_id INTEGER,

        reminder_type TEXT,

        reminder_date TEXT,

        description TEXT,

        FOREIGN KEY(pet_id)
        REFERENCES pets(pet_id)

    )
    """)

    conn.commit()

    return conn


# ==========================================
# PET CRUD
# ==========================================

# Add Pet
def add_pet(name, species, breed,
            age, gender, weight,
            owner_name, contact):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO pets(

    name,
    species,
    breed,
    age,
    gender,
    weight,
    owner_name,
    contact

    )

    VALUES(?,?,?,?,?,?,?,?)

    """,

    (

        name,
        species,
        breed,
        age,
        gender,
        weight,
        owner_name,
        contact

    ))

    conn.commit()

    conn.close()


# ==========================================
# View All Pets
# ==========================================

def get_all_pets():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM pets

    ORDER BY pet_id

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# Get One Pet
# ==========================================

def get_pet(pet_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM pets WHERE pet_id=?",

        (pet_id,)

    )

    row = cursor.fetchone()

    conn.close()

    return row


# ==========================================
# Search Pet
# ==========================================

def search_pet(keyword):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM pets

    WHERE

    name LIKE ?

    OR species LIKE ?

    OR breed LIKE ?

    OR owner_name LIKE ?

    """,

    (

        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'

    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# Update Pet
# ==========================================

def update_pet(

        pet_id,

        name,

        species,

        breed,

        age,

        gender,

        weight,

        owner_name,

        contact

):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    UPDATE pets

    SET

    name=?,

    species=?,

    breed=?,

    age=?,

    gender=?,

    weight=?,

    owner_name=?,

    contact=?

    WHERE pet_id=?

    """,

    (

        name,

        species,

        breed,

        age,

        gender,

        weight,

        owner_name,

        contact,

        pet_id

    ))

    conn.commit()

    conn.close()


# ==========================================
# Delete Pet
# ==========================================

def delete_pet(pet_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM pets WHERE pet_id=?",

        (pet_id,)

    )

    conn.commit()

    conn.close()


# ==========================================
# Run Database
# ==========================================

if __name__ == "__main__":

    connect_db()

    print("Database Created Successfully.")
    # ==========================================
# MEDICAL CRUD
# ==========================================

# ------------------------------------------
# Add Medical Record
# ------------------------------------------

def add_medical(
    pet_id,
    vaccination,
    disease,
    medicine,
    veterinarian,
    visit_date,
    notes
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO medical(

        pet_id,
        vaccination,
        disease,
        medicine,
        veterinarian,
        visit_date,
        notes

    )

    VALUES(?,?,?,?,?,?,?)

    """,

    (
        pet_id,
        vaccination,
        disease,
        medicine,
        veterinarian,
        visit_date,
        notes
    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# View All Medical Records
# ------------------------------------------

def get_medical_records():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM medical

    ORDER BY record_id

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Get One Medical Record
# ------------------------------------------

def get_medical_record(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM medical WHERE record_id=?",

        (record_id,)

    )

    row = cursor.fetchone()

    conn.close()

    return row


# ------------------------------------------
# Search Medical Records
# ------------------------------------------

def search_medical(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM medical

    WHERE

    pet_id LIKE ?

    OR vaccination LIKE ?

    OR disease LIKE ?

    OR medicine LIKE ?

    OR veterinarian LIKE ?

    """,

    (

        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%'

    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Update Medical Record
# ------------------------------------------

def update_medical(

    record_id,
    pet_id,
    vaccination,
    disease,
    medicine,
    veterinarian,
    visit_date,
    notes

):

    conn = connect_db()

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

        pet_id,
        vaccination,
        disease,
        medicine,
        veterinarian,
        visit_date,
        notes,
        record_id

    ))

    conn.commit()

    conn.close()


# ------------------------------------------
# Delete Medical Record
# ------------------------------------------

def delete_medical(record_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM medical WHERE record_id=?",

        (record_id,)

    )

    conn.commit()

    conn.close()


# ------------------------------------------
# Medical Records by Pet
# ------------------------------------------

def get_medical_by_pet(pet_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM medical WHERE pet_id=?",

        (pet_id,)

    )

    rows = cursor.fetchall()

    conn.close()

    return rows

# ==========================================
# NUTRITION CRUD
# ==========================================

# ------------------------------------------
# Add Nutrition
# ------------------------------------------

def add_nutrition(
    pet_id,
    food,
    quantity,
    calories,
    water,
    feeding_time
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO nutrition(

        pet_id,
        food,
        quantity,
        calories,
        water,
        feeding_time

    )

    VALUES(?,?,?,?,?,?)

    """, (

        pet_id,
        food,
        quantity,
        calories,
        water,
        feeding_time

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# View All Nutrition
# ------------------------------------------

def get_nutrition():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM nutrition
        ORDER BY nutrition_id
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Search Nutrition
# ------------------------------------------

def search_nutrition(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM nutrition

    WHERE

    pet_id LIKE ?

    OR food LIKE ?

    OR feeding_time LIKE ?

    """, (

        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%'

    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Update Nutrition
# ------------------------------------------

def update_nutrition(

    nutrition_id,
    pet_id,
    food,
    quantity,
    calories,
    water,
    feeding_time

):

    conn = connect_db()
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

    """, (

        pet_id,
        food,
        quantity,
        calories,
        water,
        feeding_time,
        nutrition_id

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# Delete Nutrition
# ------------------------------------------

def delete_nutrition(nutrition_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM nutrition WHERE nutrition_id=?",

        (nutrition_id,)

    )

    conn.commit()
    conn.close()


# ==========================================
# ACTIVITY CRUD
# ==========================================

# ------------------------------------------
# Add Activity
# ------------------------------------------

def add_activity(

    pet_id,
    activity,
    duration,
    calories,
    activity_date

):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO activity(

        pet_id,
        activity,
        duration,
        calories_burned,
        activity_date

    )

    VALUES(?,?,?,?,?)

    """, (

        pet_id,
        activity,
        duration,
        calories,
        activity_date

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# View All Activities
# ------------------------------------------

def get_activities():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM activity

    ORDER BY activity_id

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Search Activity
# ------------------------------------------

def search_activity(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM activity

    WHERE

    pet_id LIKE ?

    OR activity LIKE ?

    OR activity_date LIKE ?

    """, (

        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%'

    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Update Activity
# ------------------------------------------

def update_activity(

    activity_id,
    pet_id,
    activity,
    duration,
    calories_burned,
    activity_date

):

    conn = connect_db()
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

    """, (

        pet_id,
        activity,
        duration,
        calories_burned,
        activity_date,
        activity_id

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# Delete Activity
# ------------------------------------------

def delete_activity(activity_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM activity WHERE activity_id=?",

        (activity_id,)

    )

    conn.commit()
    conn.close()

    # ==========================================
# REMINDER CRUD
# ==========================================

# ------------------------------------------
# Add Reminder
# ------------------------------------------

def add_reminder(
    pet_id,
    reminder_type,
    reminder_date,
    description
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO reminder(

        pet_id,
        reminder_type,
        reminder_date,
        description

    )

    VALUES(?,?,?,?)

    """, (

        pet_id,
        reminder_type,
        reminder_date,
        description

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# View All Reminders
# ------------------------------------------

def get_reminders():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM reminder

    ORDER BY reminder_id

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Get One Reminder
# ------------------------------------------

def get_reminder(reminder_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM reminder WHERE reminder_id=?",

        (reminder_id,)

    )

    row = cursor.fetchone()

    conn.close()

    return row


# ------------------------------------------
# Search Reminder
# ------------------------------------------

def search_reminder(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM reminder

    WHERE

    pet_id LIKE ?

    OR reminder_type LIKE ?

    OR reminder_date LIKE ?

    OR description LIKE ?

    """, (

        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%',
        '%' + str(keyword) + '%'

    ))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ------------------------------------------
# Update Reminder
# ------------------------------------------

def update_reminder(

    reminder_id,
    pet_id,
    reminder_type,
    reminder_date,
    description

):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    UPDATE reminder

    SET

    pet_id=?,
    reminder_type=?,
    reminder_date=?,
    description=?

    WHERE reminder_id=?

    """, (

        pet_id,
        reminder_type,
        reminder_date,
        description,
        reminder_id

    ))

    conn.commit()
    conn.close()


# ------------------------------------------
# Delete Reminder
# ------------------------------------------

def delete_reminder(reminder_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM reminder WHERE reminder_id=?",

        (reminder_id,)

    )

    conn.commit()
    conn.close()


# ------------------------------------------
# Get Reminders by Pet
# ------------------------------------------

def get_reminders_by_pet(pet_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM reminder WHERE pet_id=?",

        (pet_id,)

    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

def total_pets():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pets")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def total_medical():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM medical")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def total_nutrition():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM nutrition")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def total_activity():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM activity")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def total_reminders():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reminder")

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================================
# CLOSE DATABASE
# ==========================================

def close_db(conn):

    if conn:

        conn.close()


# ==========================================
# INITIALIZE DATABASE
# ==========================================

if __name__ == "__main__":

    connect_db()

    print("=" * 50)
    print(" PetCareAI Database Created Successfully ")
    print("=" * 50)

    print("Total Pets :", total_pets())
    print("Total Medical Records :", total_medical())
    print("Total Nutrition Records :", total_nutrition())
    print("Total Activities :", total_activity())
    print("Total Reminders :", total_reminders())