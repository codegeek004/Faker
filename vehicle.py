import random
from faker import *
from faker import Faker
import rstr
import re
import mysql.connector
from faker_vehicle import VehicleProvider
fake = Faker()
fake.add_provider(VehicleProvider)
conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password =  'root',
        database =  'parking'
        )
cursor = conn.cursor()
def vehicle_data(num_vehicle):
    vehicle = []
    for VehicleID in range(61, num_vehicle + 1):
        VehicleType = fake.vehicle_category()
        VehicleCompany = fake.vehicle_make()
        VehicleName = fake.vehicle_model()
        VehicleNumber = rstr.xeger(r"MP[0-6][0-9][A-Z]{2}\d{4}")
        vehicle.append((VehicleID, VehicleType, VehicleNumber))
    return vehicle
def insertVehicleDataIntoMysql(vehicle):
#    cursor.execute('DROP TABLE IF EXISTS vehicle')
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicle( 
          `VehicleID` int NOT NULL AUTO_INCREMENT,
          `VehicleType` varchar(15) DEFAULT NULL,
          `VehicleNumber` varchar(35) DEFAULT NULL,
          PRIMARY KEY (`VehicleID`)
        )''')
    insert_query = '''INSERT INTO vehicle (VehicleID, VehicleType,  VehicleNumber) VALUES(%s,%s,%s)'''
    cursor.executemany(insert_query, vehicle)
    conn.commit()

num_vehicle  = 60 
vehicle_data1 = vehicle_data(num_vehicle)
insertVehicleDataIntoMysql(vehicle_data1)
cursor.close()
conn.close()
