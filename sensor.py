import random
import mysql.connector

# Database connection details
conn = mysql.connector.connect(
    host='localhost',
    user='root',   # Use 'user' instead of 'username'
    password='root',
    database='parking'
)

# Create a cursor object
cursor = conn.cursor()

# List of possible values for parking status
list1 = [0, 1]

# Function to generate sensor data
def sensorData(num_entries):
    Sensorlist = []
    start_id = 1  # Start ID can be adjusted as needed
    for SensorID in range(start_id, start_id + num_entries):
        isParked = random.choice(list1)
        Sensorlist.append((SensorID, isParked))
    return Sensorlist

# Function to insert sensor data into MySQL table
def InsertIntoMySqlData(Sensorlist):
    insert_query = 'INSERT IGNORE INTO sensor (SensorID, isParked) VALUES (%s, %s)'
    cursor.executemany(insert_query, Sensorlist)
    conn.commit()

# Generate sensor data for 91 entries
num_entries = 91
SensorData1 = sensorData(num_entries)

# Insert generated data into the database
InsertIntoMySqlData(SensorData1)

# Close the cursor and connection
cursor.close()
conn.close()

