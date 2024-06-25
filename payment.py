from faker import Faker
import random
import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Should be 'user' instead of 'username'
    password='root',
    database='parking'
)
cursor = conn.cursor()  # Fix: add parentheses to call the method

fake = Faker()

def generate_payments(num_entries):
    payments = []
    Total_Price = [13, 15, 18, 8]
    modeOfPayment = ['Card', 'Cash', 'Net-Banking', 'UPI']
    for PaymentID in range(num_entries):  # Fix: iterate exactly num_entries times
        TotalPrice = random.choice(Total_Price)
        mode = random.choice(modeOfPayment)
        ReferenceNo = fake.credit_card_security_code()
        payments.append((PaymentID, TotalPrice, mode, ReferenceNo))
    return payments

def insert_into_mysql_data(payments):
    try:
        insert_query = '''INSERT IGNORE INTO payment (PaymentID, TotalPrice, mode, ReferenceNo) VALUES (%s, %s, %s, %s)'''
        cursor.executemany(insert_query, payments)
        conn.commit()  # Fix: commit the connection, not the cursor
    except mysql.connector.Error as e:
        conn.rollback()  # Roll back the transaction in case of error
        print(f"Error: {e}")
    finally:
        cursor.close()  # Close cursor after operations
        conn.close()  # Close connection after operations

num_entries = 64 
payment_data = generate_payments(num_entries)
insert_into_mysql_data(payment_data)

