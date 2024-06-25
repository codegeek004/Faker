from faker import Faker
import mysql.connector

fake = Faker()

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='parking'
)
cursor = conn.cursor()

def fake_phone_number(fake: Faker) -> str:
    return f'{fake.msisdn()[3:]}'

def Owner(num_entries):
    owner = []
    for OwnerID in range(1, num_entries+1):  # Adjusting to start from 83
        Name = fake.name()
        address = fake.address().replace('\n', ', ')  # Remove new lines
        contact = fake_phone_number(fake)
        owner.append((OwnerID, Name, address, contact))
    return owner

def InsertIntoMySqlData(owner):
    try:
        insert_query = '''
        INSERT IGNORE INTO owner (OwnerID, Name, address, contact)
        VALUES (%s, %s, %s, %s)
        '''
        
        print("Inserting the following data:")  # Debug statement
        for entry in owner:
            print(entry)  # Print each tuple to be inserted
        
        cursor.executemany(insert_query, owner)
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Number of entries to insert
num_entries = 64
owner_data = Owner(num_entries)
InsertIntoMySqlData(owner_data)

