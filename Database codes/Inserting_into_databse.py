import sqlite3
import random

conn = sqlite3.connect('database.db')
c = conn.cursor()

saudi_cities = ['Riyadh', 'Jeddah', 'Mecca', 'Medina', 'Dammam', 'Taif', 'Tabuk', 'Al-Khobar', 'Abha', 'Buraidah']

for _ in range(10):
    bank_account = random.randint(100000, 999999)
    first_name = "DonorFirstName" + str(_)
    middle_name = "DonorMiddleName" + str(_)
    last_name = "DonorLastName" + str(_)
    c.execute('''INSERT INTO DONOR (Bank_Account, First_Name, Middle_Name, Last_Name)
                 VALUES (?, ?, ?, ?)''', (bank_account, first_name, middle_name, last_name))

for _ in range(10):
    snumber = random.randint(1000, 9999)
    first_name = "VolunteerFirstName" + str(_)
    middle_name = "VolunteerMiddleName" + str(_)
    last_name = "VolunteerLastName" + str(_)
    c.execute('''INSERT INTO VOLUNTEER (SNumber, First_Name, Middle_Name, Last_Name)
                 VALUES (?, ?, ?, ?)''', (snumber, first_name, middle_name, last_name))

for _ in range(10):
    snumber = random.randint(1000, 9999)
    capacity = random.randint(50, 200)
    coordination = "Coordination" + str(_)
    nearest_doors = "NearestDoors" + str(_)
    c.execute('''INSERT INTO SUFRA (SNumber, Capacity, Coordination, Nearest_Doors)
                 VALUES (?, ?, ?, ?)''', (snumber, capacity, coordination, nearest_doors))

for _ in range(10):
    snumber = random.randint(1000, 9999)
    first_name = "SupervisorFirstName" + str(_)
    middle_name = "SupervisorMiddleName" + str(_)
    last_name = "SupervisorLastName" + str(_)
    c.execute('''INSERT INTO SUPERVISOR (SNumber, First_Name, Middle_Name, Last_Name)
                 VALUES (?, ?, ?, ?)''', (snumber, first_name, middle_name, last_name))

for _ in range(10):
    food_type = random.choice(['Rice', 'Wheat', 'Vegetables', 'Fruits'])  
    city = random.choice(saudi_cities)
    road = f"Street {random.randint(1, 100)}"
    address = f"{road}, {city}, Saudi Arabia"
    c.execute('''INSERT INTO SUPPLIER (FOOD_type, City, Road, Address)
                 VALUES (?, ?, ?, ?)''', (food_type, city, road, address))

for _ in range(10):
    snumber = random.randint(1000, 9999)
    first_name = "WorkerFirstName" + str(_)
    middle_name = "WorkerMiddleName" + str(_)
    last_name = "WorkerLastName" + str(_)
    c.execute('''INSERT INTO WORKER (SNumber, First_Name, Middle_Name, Last_Name)
                 VALUES (?, ?, ?, ?)''', (snumber, first_name, middle_name, last_name))

conn.commit()
conn.close()

print("Data inserted successfully.")