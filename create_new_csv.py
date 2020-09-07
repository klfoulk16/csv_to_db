"""Writes new CSV's based on SQL queries to a database"""

# Make sure you've activated the venv
import sqlite3 as db
import csv

# Get headers
with db.connect('retention.db') as conn:
    conn.row_factory = db.Row
    cursor = conn.execute('select * from recipients join results on recipients.email = results.email')
    row = cursor.fetchone()
    headers = row.keys()

# Run the query and store result as `data`
with db.connect('retention.db') as conn:
    cur = conn.cursor()
    sql = "select * from recipients join results on recipients.email = results.email"
    cur.execute(sql)
    data = cur.fetchall()

# Create the new csv file
with open('since_2019_retention.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Print headers
    writer.writerow(headers)
    # Iterate over `data`  and  write to the csv file
    for row in data:
        writer.writerow(row)
