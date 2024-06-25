import random
from datetime import time, date
import mysql.connector

def generate_time_pairs(n):
    time_pairs = []
    for _ in range(n):
        hour_from = random.randint(0, 23)
        minute_from = random.randint(0, 59)
        second_from = random.randint(0, 59)
        time_from = time(hour_from, minute_from, second_from)
        
        total_seconds_from = hour_from * 3600 + minute_from * 60 + second_from
        remaining_seconds = 24 * 3600 - total_seconds_from - 1
        added_seconds = random.randint(1, remaining_seconds)
        
        total_seconds_to = total_seconds_from + added_seconds
        hours_to = total_seconds_to // 3600
        minutes_to = (total_seconds_to % 3600) // 60
        seconds_to = total_seconds_to % 60
        time_to = time(hours_to, minutes_to, seconds_to)
        
        time_pairs.append((time_from, time_to))
    return time_pairs

# Generate 91 time pairs
time_pairs = generate_time_pairs(64)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'parking'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Insert query template
insert_query = """
    INSERT IGNORE INTO  bookingslot(BSlotID, Date, TimeFrom, TimeTo)
    VALUES (%s, %s, %s, %s)
"""

# Example date for insertion
insert_date = date(2024, 6, 22)

# Insert data
for bslot_id, (time_from, time_to) in enumerate(time_pairs, start=1):
    cursor.execute(insert_query, (bslot_id, insert_date, time_from, time_to))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

