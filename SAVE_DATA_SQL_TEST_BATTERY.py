import serial
import sqlite3
import random
import time
import datetime
import matplotlib.pyplot as plt

def CrearTabla():
    conn = sqlite3.connect("DischargeBattery")
    if conn:
        print ("connecting succefull")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE DischargeBattery(
                        id INTEGER PRIMARY KEY,
                        idBattery INTEGER,
                        date varchar(50) NULL,
                        Voltage Float 
                       )''')
        print("Create table succefull")
        
def insertBBDD(idBattery,date,Voltage):
    try:
        conn = sqlite3.connect("DischargeBattery")
        if conn:
            print("Connecting Succefull")
            cursor = conn.cursor()
            print("Insert Date into BBDD")
            consulta = '''INSERT INTO DischargeBattery(
                        idBattery,
                        date,
                        Voltage)
                        VALUES(?,?,?);'''
            cursor.execute(consulta,(idBattery,date,Voltage))
            print("Insert Dates Succefull")
    except Exception as e:
        print("Error Connecting BBDD... try again")
    finally:
        conn.commit()
        cursor.close()
        conn.close()


PuertoSerie = serial.Serial('COM3', 9600)


while True:
    sArduino = PuertoSerie.readline().decode('utf-8').strip()
    sArduino = sArduino.split("|")
    print(sArduino[0],sArduino[1])

    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.strftime("%d/%m/%Y %H:%M")
    
    insertBBDD(sArduino[0],current_datetime,sArduino[1])
    