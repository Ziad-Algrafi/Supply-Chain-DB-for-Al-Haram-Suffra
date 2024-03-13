import sqlite3



conn = sqlite3.connect('database.db')
c = conn.cursor()

def check_missing_suppliers():
   
    c.execute('''SELECT SUFRA_ID FROM SUFRA 
                 WHERE SUFRA_ID NOT IN (SELECT SUFRA_ID FROM SUPPLIER_SUPPLY_SUFRA)''')
    missing_suppliers = c.fetchall()
    if missing_suppliers:
        print("Alert: The following SUFRA(s) do not have assigned suppliers:")
        for sufra_id in missing_suppliers:
            print(f"SUFRA_ID: {sufra_id[0]}")

def check_missing_supervisors():

    c.execute('''SELECT SUFRA_ID FROM SUFRA 
                 WHERE SUFRA_ID NOT IN (SELECT SUFRA_ID FROM SUPERVISOR_SUPERVISION_SUFRA)''')
    missing_supervisors = c.fetchall()
    if missing_supervisors:
        print("Alert: The following SUFRA(s) do not have assigned supervisors:")
        for sufra_id in missing_supervisors:
            print(f"SUFRA_ID: {sufra_id[0]}")

check_missing_suppliers()

check_missing_supervisors()

conn.close()
