import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

# Función para obtener los datos de la base de datos SQLite
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

# Función para inicializar la gráfica
def initialize_graph():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title('Voltage vs. Time idBattery')
    ax.set_xlabel('Time')
    ax.set_ylabel('Voltage')
    ax.grid(True)
    return fig, ax

# Función para actualizar la gráfica en tiempo real
def update_graph(i):
    dates_idBattery = get_dates()
    ax.clear()
    for idBattery, data in dates_idBattery.items():
        dateTime = data['dateTime']
        voltages = data['voltages']
        ax.plot(dateTime, voltages, marker='o', linestyle='-', label=f'idBattery {idBattery}')
    ax.set_title('Voltage vs. Time idBattery')
    ax.set_xlabel('Time')
    ax.set_ylabel('Voltage')
    ax.grid(True)
    ax.legend()

# Crear la figura y el eje inicial
fig, ax = initialize_graph()

# Crear la animación para actualizar la gráfica cada 30 segundos
ani = FuncAnimation(fig, update_graph, interval=30000)  # 30000 milisegundos = 30 segundos

# Mostrar la gráfica
plt.show()