import sqlite3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def obtener_datos():
    conn = sqlite3.connect("DischargeBattery")
    cursor = conn.cursor()
    cursor.execute("SELECT id, idBattery, Voltage FROM DischargeBattery")
    data = cursor.fetchall()
    conn.close()
    return data


def actualizar_grafico(i):
    data = obtener_datos()
    
    datos_por_bateria = {}
    for fila in data:
        id_bateria = fila[1]
        voltaje = fila[2]
        
        if id_bateria not in datos_por_bateria:
            datos_por_bateria[id_bateria] = {'ids': [], 'voltajes': []}
        
        datos_por_bateria[id_bateria]['ids'].append(fila[0])
        datos_por_bateria[id_bateria]['voltajes'].append(voltaje)

    plt.clf()
    for id_bateria, datos in datos_por_bateria.items():
        plt.plot(datos['ids'], datos['voltajes'], marker='.', label=f'ID de Batería {id_bateria}')

    plt.xlabel('ID')
    plt.ylabel('Voltaje')
    plt.title('Gráfico de Voltaje vs. ID por ID de Batería')
    plt.legend()
    plt.grid(True)


ani = FuncAnimation(plt.gcf(), actualizar_grafico, interval=36000)  #

plt.show()
