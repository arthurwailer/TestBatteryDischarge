import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import time 
from matplotlib.animation import FuncAnimation


def get_dates():

	conn = sqlite3.connect("DischargeBattery") 
	cursor = conn.cursor()
	cursor.execute("SELECT idBattery, date, Voltage FROM DischargeBattery ORDER BY date")
	result = cursor.fetchall()
	conn.close()
	dates_idBattery = {}
	for row in result:
		idBattery = row[0]
		dateTime = row[1]
		voltage = row[2]
		if idBattery not in dates_idBattery:
			dates_idBattery[idBattery] = {'dateTime': [], 'voltages': []}
		dates_idBattery[idBattery]['dateTime'].append(dateTime)
		dates_idBattery[idBattery]['voltages'].append(voltage)
	return dates_idBattery


def update_grafic(dates_idBattery):

	plt.figure(figsize=(10, 6))
	for idBattery, datos in dates_idBattery.items():
		dateTime = datos['dateTime']
		voltages = datos['voltages']
		plt.plot(dateTime, voltages, marker='o', linestyle='-', label=f'idBattery {idBattery}')
	plt.gcf().autofmt_xdate()
	plt.title('Voltage vs. Time idBattery')
	plt.xlabel('Time')
	plt.ylabel('Voltage')
	plt.grid(True)
	plt.legend()
	plt.pause(1) 



while True:

	dates_idBattery = get_dates()
	update_grafic(dates_idBattery)
	plt.show()
	plt.clf() 
	time.sleep(60)




