import sqlite3
import sys

output_file = "output_jc.txt"
sys.stdout = open(output_file, "w", encoding="utf-8")

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS

    print("ALL TESTS")
    cursor.execute("SELECT * FROM concrete_tests")
    rows = cursor.fetchall()

    for r in rows:
        project = r["project_name"]
        strength = r["actual_strength"]
        status = "PASS" if r["passed"] == 1 else "FAIL"
        print(f"{project}: {strength} PSI - {status}")
    print() 

    # 2. FAILED TESTS

    print("FAILED TESTS")
    cursor.execute("""
        SELECT *
        FROM concrete_tests
        WHERE passed = 0
    """)
    failed = cursor.fetchall()

    for r in failed:
        print(f"{r['project_name']} on {r['test_date']}")
        print(f"  Required: {r['required_strength']} PSI")
        print(f"  Actual: {r['actual_strength']} PSI")
        print()


    # 3. TESTS PER PROJECT

    print("TESTS PER PROJECT")
    cursor.execute("""
        SELECT project_name,
               SUM(passed) AS passed_tests,
               COUNT(*) AS total_tests
        FROM concrete_tests
        GROUP BY project_name
    """)
    summary = cursor.fetchall()

    for r in summary:
        print(f"{r['project_name']}: {r['passed_tests']}/{r['total_tests']} passed")
        
sys.stdout.close()
sys.stdout = sys.__stdout__