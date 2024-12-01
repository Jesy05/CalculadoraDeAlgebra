from tkinter import *
from tkinter import ttk, messagebox
import sympy as sp
import re

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    funciones_math = {
        'sen': 'sin',
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan',
        'cot': '1/tan',
        'sec': '1/cos',
        'csc': '1/sin',
        'log': 'log10',
        'ln': 'log',
        'exp': 'exp',
        'sqrt': 'sqrt',
        'pi': 'pi',
        'e': 'E'
    }
    try:
        funcion = funcion.replace('^', '**').replace(' ', '')
        funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)
        funcion = re.sub(r'(\))(?=\d|[a-zA-Z])', r')*', funcion)
        for key, val in funciones_math.items():
            funcion = re.sub(r'\b' + key + r'\b', val, funcion)
        return funcion
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")

# Método de la Secante
def metodo_secante(funcion, x0, x1, tolerancia, max_iter):
    resultados = []
    f = sp.sympify(funcion)
    x0, x1 = float(x0), float(x1)
    ea = None  # Inicializamos el error aproximado
    
    for i in range(max_iter):
        y0 = f.subs('x', x0)
        y1 = f.subs('x', x1)

        if y1 - y0 == 0:
            raise ZeroDivisionError("La división por cero ocurrió en el método de la secante.")

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        ea = abs((x2 - x1) / x2) * 100 if i > 0 else None
        resultados.append([i + 1, x0, x1, x2, ea, y0, y1])

        # Detener el método si el error aproximado es menor que la tolerancia
        if ea is not None and ea < tolerancia:
            break

        x0, x1 = x1, x2

    # Conclusión final
    resultado_final = f"La raíz aproximada es {x2:.6f}, el error aproximado es {ea:.6f}%, el método converge a {i + 1} iteraciones."
    return resultados, resultado_final

# Mostrar resultados en la tabla
def mostrar_resultados(resultados, columnas, resumen):
    for widget in resultados_frame.winfo_children():
        widget.destroy()
    
    tree = ttk.Treeview(resultados_frame, columns=columnas, show='headings')
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)
    for row in resultados:
        tree.insert('', 'end', values=row)
    tree.pack(expand=True, fill=BOTH)
    
    resultado_label.config(text=resumen)

# Limpiar pantalla
def limpiar_pantalla():
    funcion_entry.delete(0, END)
    xi_entry.delete(0, END)
    xu_entry.delete(0, END)
    tolerancia_entry.delete(0, END)
    iteraciones_entry.delete(0, END)
    for widget in resultados_frame.winfo_children():
        widget.destroy()
    resultado_label.config(text="")

# Ejecutar el método seleccionado
def calcular():
    metodo = metodo_var.get()
    funcion = funcion_entry.get()
    try:
        funcion = preparar_funcion(funcion)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    
    xi = xi_entry.get()
    xu = xu_entry.get()
    tol = tolerancia_entry.get()
    max_iter = iteraciones_entry.get()
    
    if not funcion or not xi or not xu or not tol or not max_iter:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    
    try:
        tol = float(tol)
        max_iter = int(max_iter)
        if metodo == "Secante":
            resultados, resumen = metodo_secante(funcion, xi, xu, tol, max_iter)
            columnas = ['Iteración', 'x0', 'x1', 'x2', 'Ea', 'y0', 'y1']
        else:
            messagebox.showinfo("Aviso", "Método no implementado.")
            return
        mostrar_resultados(resultados, columnas, resumen)
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

# Configuración de la interfaz
root = Tk()
root.title("Métodos Numéricos - Secante")
root.geometry("1000x650")

metodo_var = StringVar(value="Secante")

Label(root, text="Función:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
funcion_entry = Entry(root, width=40)
funcion_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(root, text="x0:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
xi_entry = Entry(root, width=10)
xi_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

Label(root, text="x1:").grid(row=3, column=0, padx=5, pady=5, sticky=W)
xu_entry = Entry(root, width=10)
xu_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

Label(root, text="Tolerancia:").grid(row=4, column=0, padx=5, pady=5, sticky=W)
tolerancia_entry = Entry(root, width=10)
tolerancia_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

Label(root, text="Máx. Iteraciones:").grid(row=5, column=0, padx=5, pady=5, sticky=W)
iteraciones_entry = Entry(root, width=10)
iteraciones_entry.grid(row=5, column=1, padx=5, pady=5, sticky=W)

Button(root, text="Calcular", command=calcular).grid(row=6, column=0, pady=10)
Button(root, text="Limpiar", command=limpiar_pantalla).grid(row=6, column=1, pady=10)

resultados_frame = Frame(root)
resultados_frame.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

resultado_label = Label(root, text="", fg="black", font=("Arial", 12))
resultado_label.grid(row=8, column=0, columnspan=4, pady=10)

root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
