import sqlite3
from datetime import datetime

DB_NAME = "../disaster_management.db"


# -----------------------------------
# CONNECT DATABASE
# -----------------------------------
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor


# -----------------------------------
# CREATE ALL TABLES
# -----------------------------------
def create_tables():
    conn, cursor = connect_db()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT UNIQUE,
        password_hash TEXT,
        role TEXT,
        phone_number TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # DISASTERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disasters (
        disaster_id INTEGER PRIMARY KEY AUTOINCREMENT,
        disaster_type TEXT,
        location TEXT,
        latitude REAL,
        longitude REAL,
        severity_level TEXT,
        status TEXT,
        description TEXT,
        disaster_time TIMESTAMP
    )
    """)

    # UPLOADED IMAGES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS uploaded_images (
        image_id INTEGER PRIMARY KEY AUTOINCREMENT,
        disaster_id INTEGER,
        uploaded_by INTEGER,
        image_path TEXT,
        image_type TEXT,
        upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # AI ANALYSIS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ai_analysis (
        analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_id INTEGER,
        damage_percentage REAL,
        buildings_destroyed INTEGER,
        roads_damaged INTEGER,
        flood_water_level REAL,
        confidence_score REAL,
        analysis_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # AFFECTED AREAS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS affected_areas (
        area_id INTEGER PRIMARY KEY AUTOINCREMENT,
        disaster_id INTEGER,
        area_name TEXT,
        population_affected INTEGER,
        houses_damaged INTEGER,
        casualties INTEGER,
        relief_needed TEXT
    )
    """)

    # RELIEF OPERATIONS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relief_operations (
        operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        disaster_id INTEGER,
        team_name TEXT,
        resources_sent TEXT,
        operation_status TEXT,
        updated_time TIMESTAMP
    )
    """)

    # ALERTS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
        disaster_type TEXT,
        predicted_risk TEXT,
        alert_message TEXT,
        issued_time TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("All tables created successfully.")


# -----------------------------------
# INSERT SAMPLE DATA
# -----------------------------------
def insert_sample_data():
    conn, cursor = connect_db()

    # USERS
    users_data = [
        (
            "Harshit Gupta",
            "harshit@gmail.com",
            "hashed_password",
            "Admin",
            "9876543210"
        ),
        (
            "Ananya Sharma",
            "ananya@gmail.com",
            "hashed_password",
            "Rescue Officer",
            "9876501234"
        )
    ]

    cursor.executemany("""
    INSERT INTO users (
        full_name,
        email,
        password_hash,
        role,
        phone_number
    )
    VALUES (?, ?, ?, ?, ?)
    """, users_data)

    # DISASTERS
    disasters_data = [
        (
            "Flood",
            "Assam",
            26.2,
            91.7,
            "High",
            "Active",
            "Heavy flooding due to continuous rainfall",
            datetime.now()
        ),
        (
            "Earthquake",
            "Nepal Border",
            28.3,
            84.1,
            "Medium",
            "Monitoring",
            "6.4 magnitude earthquake detected",
            datetime.now()
        ),
        (
            "Cyclone",
            "Odisha Coast",
            20.2,
            86.4,
            "Severe",
            "Emergency",
            "Cyclone landfall expected within 12 hours",
            datetime.now()
        )
    ]

    cursor.executemany("""
    INSERT INTO disasters (
        disaster_type,
        location,
        latitude,
        longitude,
        severity_level,
        status,
        description,
        disaster_time
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, disasters_data)

    # UPLOADED IMAGES
    images_data = [
        (1, 1, "uploads/flood_assam_1.jpg", "Drone"),
        (1, 2, "uploads/flood_assam_2.jpg", "Satellite"),
        (2, 1, "uploads/earthquake_nepal.jpg", "Ground"),
        (3, 2, "uploads/cyclone_odisha.jpg", "Drone")
    ]

    cursor.executemany("""
    INSERT INTO uploaded_images (
        disaster_id,
        uploaded_by,
        image_path,
        image_type
    )
    VALUES (?, ?, ?, ?)
    """, images_data)

    # AI ANALYSIS
    ai_data = [
        (
            1,
            82.5,
            58,
            1,
            6.8,
            0.96
        ),
        (
            2,
            74.2,
            41,
            1,
            5.3,
            0.92
        ),
        (
            3,
            68.9,
            33,
            1,
            0.0,
            0.90
        ),
        (
            4,
            91.4,
            77,
            1,
            0.0,
            0.98
        )
    ]

    cursor.executemany("""
    INSERT INTO ai_analysis (
        image_id,
        damage_percentage,
        buildings_destroyed,
        roads_damaged,
        flood_water_level,
        confidence_score
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, ai_data)

    # AFFECTED AREAS
    affected_data = [
        (
            1,
            "Dhemaji",
            12000,
            2500,
            34,
            "Food, Shelter, Medicine"
        ),
        (
            1,
            "Lakhimpur",
            18000,
            3400,
            52,
            "Rescue Boats, Food"
        ),
        (
            2,
            "Kathmandu Region",
            9000,
            1700,
            21,
            "Medical Aid"
        ),
        (
            3,
            "Puri District",
            22000,
            4100,
            67,
            "Evacuation Support"
        )
    ]

    cursor.executemany("""
    INSERT INTO affected_areas (
        disaster_id,
        area_name,
        population_affected,
        houses_damaged,
        casualties,
        relief_needed
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, affected_data)

    # RELIEF OPERATIONS
    relief_data = [
        (
            1,
            "NDRF Team Alpha",
            "Food Kits, Medical Supplies",
            "Ongoing",
            datetime.now()
        ),
        (
            2,
            "Army Rescue Unit",
            "Medical Teams, Tents",
            "Completed",
            datetime.now()
        ),
        (
            3,
            "Odisha Coastal Force",
            "Evacuation Vehicles, Water",
            "Ongoing",
            datetime.now()
        )
    ]

    cursor.executemany("""
    INSERT INTO relief_operations (
        disaster_id,
        team_name,
        resources_sent,
        operation_status,
        updated_time
    )
    VALUES (?, ?, ?, ?, ?)
    """, relief_data)

    # ALERTS
    alerts_data = [
        (
            "Flood",
            "High",
            "Extreme flood risk in Assam within next 6 hours",
            datetime.now()
        ),
        (
            "Earthquake",
            "Medium",
            "Possible aftershocks expected near Nepal border",
            datetime.now()
        ),
        (
            "Cyclone",
            "Severe",
            "Cyclone warning issued for Odisha coastal region",
            datetime.now()
        )
    ]

    cursor.executemany("""
    INSERT INTO alerts (
        disaster_type,
        predicted_risk,
        alert_message,
        issued_time
    )
    VALUES (?, ?, ?, ?)
    """, alerts_data)

    conn.commit()
    conn.close()

    print("Sample data inserted successfully.")


# -----------------------------------
# VIEW DATA
# -----------------------------------
def view_disasters():
    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM disasters")

    rows = cursor.fetchall()

    print("\n========== DISASTER RECORDS ==========\n")

    for row in rows:
        print(row)

    conn.close()


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------
if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    view_disasters() 