import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE GPH (
                GPH_ID INTEGER PRIMARY KEY,
                Number TEXT
             )''')

c.execute('''CREATE TABLE DONOR (
                Donor_ID INTEGER PRIMARY KEY,
                Bank_Account TEXT,
                First_Name TEXT,
                Middle_Name TEXT,
                Last_Name TEXT
             )''')

c.execute('''CREATE TABLE VOLUNTEER (
                Volunteer_ID INTEGER PRIMARY KEY,
                SNumber TEXT,
                First_Name TEXT,
                Middle_Name TEXT,
                Last_Name TEXT
             )''')

c.execute('''CREATE TABLE SUFRA (
                SUFRA_ID INTEGER PRIMARY KEY,
                SNumber TEXT,
                Capacity INTEGER,
                Coordination TEXT,
                Nearest_Doors TEXT
             )''')

c.execute('''CREATE TABLE SUPERVISOR (
                Supervisor_ID INTEGER PRIMARY KEY,
                SNumber TEXT,
                First_Name TEXT,
                Middle_Name TEXT,
                Last_Name TEXT
             )''')

c.execute('''CREATE TABLE SUPPLIER (
                Supplier_ID INTEGER PRIMARY KEY,
                FOOD_type TEXT,
                City TEXT,
                Road TEXT,
                Address TEXT
             )''')

c.execute('''CREATE TABLE WORKER (
                Worker_ID INTEGER PRIMARY KEY,
                SNumber TEXT,
                First_Name TEXT,
                Middle_Name TEXT,
                Last_Name TEXT
             )''')


c.execute('''CREATE TABLE GPH_MANAGE_SUPPLIER (
                GPH_ID INTEGER,
                Supplier_ID INTEGER,
                FOREIGN KEY (GPH_ID) REFERENCES GPH (GPH_ID),
                FOREIGN KEY (Supplier_ID) REFERENCES SUPPLIER (Supplier_ID)
             )''')

c.execute('''CREATE TABLE GPH_INSTRUCT_SUPERVISOR (
                GPH_ID INTEGER,
                Supervisor_ID INTEGER,
                FOREIGN KEY (GPH_ID) REFERENCES GPH (GPH_ID),
                FOREIGN KEY (Supervisor_ID) REFERENCES SUPERVISOR (Supervisor_ID)
             )''')

c.execute('''CREATE TABLE GPH_ASSIGN_VOLUNTEER (
                GPH_ID INTEGER,
                Volunteer_ID INTEGER,
                FOREIGN KEY (GPH_ID) REFERENCES GPH (GPH_ID),
                FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER (Volunteer_ID)
             )''')

c.execute('''CREATE TABLE DONOR_DONATE_GPH (
                Donor_ID INTEGER,
                GPH_ID INTEGER,
                FOREIGN KEY (Donor_ID) REFERENCES DONOR (Donor_ID),
                FOREIGN KEY (GPH_ID) REFERENCES GPH (GPH_ID)
             )''')

c.execute('''CREATE TABLE SUPPLIER_SUPPLY_SUFRA (
                Supplier_ID INTEGER,
                SUFRA_ID INTEGER,
                FOREIGN KEY (Supplier_ID) REFERENCES SUPPLIER (Supplier_ID),
                FOREIGN KEY (SUFRA_ID) REFERENCES SUFRA (SUFRA_ID)
             )''')

c.execute('''CREATE TABLE VOLUNTEER_WORKS_ON_SUFRA (
                Volunteer_ID INTEGER,
                SUFRA_ID INTEGER,
                FOREIGN KEY (Volunteer_ID) REFERENCES VOLUNTEER (Volunteer_ID),
                FOREIGN KEY (SUFRA_ID) REFERENCES SUFRA (SUFRA_ID)
             )''')

c.execute('''CREATE TABLE WORKER_WORKS_ON_SUFRA (
                Worker_ID INTEGER,
                SUFRA_ID INTEGER,
                FOREIGN KEY (Worker_ID) REFERENCES WORKER (Worker_ID),
                FOREIGN KEY (SUFRA_ID) REFERENCES SUFRA (SUFRA_ID)
             )''')

c.execute('''CREATE TABLE SUPERVISOR_SUPERVISION_SUFRA (
                Supervisor_ID INTEGER,
                SUFRA_ID INTEGER,
                FOREIGN KEY (Supervisor_ID) REFERENCES SUPERVISOR (Supervisor_ID),
                FOREIGN KEY (SUFRA_ID) REFERENCES SUFRA (SUFRA_ID)
             )''')

conn.commit()
conn.close()
