import sqlite3
import matplotlib.pyplot as plt

def plot_supply_line_chart(c):
    c.execute("SELECT FOOD_type, COUNT(*) FROM SUPPLIER GROUP BY FOOD_type")
    data = c.fetchall()
    food_types = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.plot(food_types, counts, marker='o')
    plt.title('Supply Data')
    plt.xlabel('Food Type')
    plt.ylabel('Number of Suppliers')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_sufra_related_to_supervisors_and_suppliers(c):

    c.execute("SELECT COUNT(DISTINCT SUFRA_ID) FROM SUPERVISOR_SUPERVISION_SUFRA")
    supervisor_sufra_count = c.fetchone()[0]

    c.execute("SELECT COUNT(DISTINCT SUFRA_ID) FROM SUPPLIER_SUPPLY_SUFRA")
    supplier_sufra_count = c.fetchone()[0]

    plt.bar(['Supervisors', 'Suppliers'], [supervisor_sufra_count, supplier_sufra_count], color=['blue', 'green'])
    plt.title('Number of SUFRA Related to Supervisors and Suppliers')
    plt.xlabel('Category')
    plt.ylabel('Number of SUFRA')
    plt.grid(axis='y')

conn = sqlite3.connect('database.db')
c = conn.cursor()

fig, axes = plt.subplots(2, 1, figsize=(10, 12))

plot_supply_line_chart(c)
plt.subplot(2, 1, 1)

plot_sufra_related_to_supervisors_and_suppliers(c)
plt.subplot(2, 1, 2)

plt.tight_layout()
plt.show()

conn.close()
