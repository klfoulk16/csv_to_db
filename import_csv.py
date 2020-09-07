"""Imports data from two different CSV's to a database so you can query them."""

import sqlite3
import pandas as pd
from pandas import DataFrame

# Creates database if it doesn't already exist
conn = sqlite3.connect('jul17_retention.db')
c = conn.cursor()

# Read data from the first CSV into a 'recipients' table
read_recipients = pd.read_csv (r'jul-17-inactive.csv')
# Insert the values from the csv file into the table 'recipients'
read_recipients.to_sql('recipients', conn, if_exists='append', index = False)

# Reads data from second CSV into 'results' table
read_results = pd.read_csv (r'matt-data.csv')
read_results.to_sql('results', conn, if_exists='replace', index = False)

conn.close()
