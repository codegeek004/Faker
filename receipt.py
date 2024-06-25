from faker import *
import random
import mysql.connector
fake = Faker()
conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'parking'
        )
cursor = conn.cursor()
def receiptNo(num_receipt):
    receipt = []
    for ReceiptID in range(0, num_receipt+1):

        TokenNo = fake.pyint()
        receipt.append((ReceiptID, TokenNo))
    return receipt

def InsertDataIntoMySql(receipt):
    insert_query = 'INSERT ignore INTO receipt(ReceiptID, TokenNo) values (%s, %s)'
    cursor.executemany(insert_query, receipt)
    conn.commit()

num_receipt = 64 
Receipt_data = receiptNo(num_receipt)
InsertDataIntoMySql(Receipt_data)
cursor.close()
conn.close()





