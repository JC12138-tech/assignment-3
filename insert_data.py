import sqlite3

with sqlite3.connect('concrete.db') as conn:
    cursor = conn.cursor()
    
    # The data (copy from table above)
    tests = [
        ('Bridge Repair', '2024-11-01', 4000, 4200, 1),
        ('Bridge Repair', '2024-11-02', 4000, 3900, 0),
        ('Bridge Repair', '2024-11-03', 4000, 4100, 1),
        ('Parking Garage', '2024-11-01', 3000, 3200, 1),
        ('Parking Garage', '2024-11-02', 3000, 3100, 1),
        ('Office Building', '2024-11-01', 5000, 5300, 1),
        ('Office Building', '2024-11-02', 5000, 4800, 0),
        ('Office Building', '2024-11-03', 5000, 5100, 1)
    ]
    cursor.executemany('''
        INSERT INTO concrete_tests (
        project_name, test_date, required_strength, actual_strength, passed
        ) VALUES (?, ?, ?, ?, ?)
    ''', tests)

    conn.commit()

    

print(f"Inserted {cursor.rowcount} tests!")
