import streamlit as st
import numpy as np

# Ejercicio 1: Fabricante
def ejercicio_fabricante():
    D = np.array([4, 5, 6, 3])  # Demanda de productos
    P = np.array([10, 12, 15, 8])  # Precio por unidad
    total_ingreso = np.dot(D, P)  # Cálculo de ingreso total
    return D, P, total_ingreso


# Ejercicio 2: Joyería
def ejercicio_joyeria():
    ordenes = np.array([3, 5, 2, 6])  # Cantidad de órdenes
    tiempos = np.array([2, 4, 3, 5])  # Horas por orden
    total_horas = np.dot(ordenes, tiempos)  # Cálculo de horas totales
    return ordenes, tiempos, total_horas


# Ejercicio 3: Turista
def ejercicio_turista():
    cantidades = np.array([2, 3, 1])  # Cantidades de productos comprados
    valores = np.array([50, 30, 100])  # Precios en dólares
    total_dolares = np.dot(cantidades, valores)  # Cálculo del total en dólares
    return cantidades, valores, total_dolares


# Ejercicio 4: Gran Compañía
def ejercicio_gran_compania():
    ventas = np.array([[100, 200, 300, 400], [150, 250, 350, 450]])  # Ventas por mes
    utilidades = np.array([0.1, 0.2])  # Utilidades por producto
    impuestos = np.array([0.05, 0.07])  # Impuestos por producto

    utilidades_totales = np.dot(ventas.T, utilidades)  # Cálculo de utilidades totales
    impuestos_totales = np.dot(ventas.T, impuestos)  # Cálculo de impuestos totales

    return ventas, utilidades, impuestos, utilidades_totales, impuestos_totales
