import tkinter as tk
from tkinter import Toplevel, Label, Entry, messagebox, Listbox, END
from ttkbootstrap import Style, Button
from controllers.cliente_controller import crear_cliente
from controllers.propiedad_controller import agregar_propiedad, obtener_propiedades, obtener_propiedad_por_id, agregar_a_visitas
from controllers.renta_controller import rentar_propiedad

def crear_cliente_formulario():
    form = Toplevel()
    form.title("Registrar Cliente")
    form.geometry("400x300")

    Label(form, text="Nombre").pack(pady=5)
    nombre_entry = Entry(form, width=30)
    nombre_entry.pack()

    Label(form, text="Correo").pack(pady=5)
    correo_entry = Entry(form, width=30)
    correo_entry.pack()

    Label(form, text="Contraseña").pack(pady=5)
    clave_entry = Entry(form, show="*", width=30)
    clave_entry.pack()

    def registrar():
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        clave = clave_entry.get()
        if not nombre or not correo or not clave:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
            return
        crear_cliente(nombre, correo, clave)
        messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        form.destroy()

    Button(form, text="Registrar", bootstyle="success", command=registrar).pack(pady=20)

def agregar_propiedad_formulario():
    form = Toplevel()
    form.title("Agregar Propiedad")
    form.geometry("400x350")

    Label(form, text="ID Dueño").pack(pady=5)
    duenio_entry = Entry(form, width=30)
    duenio_entry.pack()

    Label(form, text="Dirección").pack(pady=5)
    direccion_entry = Entry(form, width=30)
    direccion_entry.pack()

    Label(form, text="Tipo").pack(pady=5)
    tipo_entry = Entry(form, width=30)
    tipo_entry.pack()

    Label(form, text="Valor").pack(pady=5)
    valor_entry = Entry(form, width=30)
    valor_entry.pack()

    def registrar():
        try:
            agregar_propiedad(
                int(duenio_entry.get()),
                direccion_entry.get(),
                tipo_entry.get(),
                float(valor_entry.get())
            )
            messagebox.showinfo("Éxito", "Propiedad agregada correctamente.")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(form, text="Registrar", bootstyle="success", command=registrar).pack(pady=20)

def rentar_propiedad_formulario():
    form = Toplevel()
    form.title("Rentar Propiedad")
    form.geometry("400x250")

    Label(form, text="ID Cliente").pack(pady=5)
    cliente_entry = Entry(form, width=30)
    cliente_entry.pack()

    Label(form, text="ID Propiedad").pack(pady=5)
    propiedad_entry = Entry(form, width=30)
    propiedad_entry.pack()

    def rentar():
        try:
            rentar_propiedad(cliente_entry.get(), propiedad_entry.get())
            messagebox.showinfo("Éxito", "Propiedad rentada correctamente.")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(form, text="Rentar", bootstyle="success", command=rentar).pack(pady=20)

def buscar_propiedades_formulario():
    form = Toplevel()
    form.title("Buscar Propiedades")
    form.geometry("500x300")

    propiedades = obtener_propiedades()

    lista = Listbox(form, width=80)
    for p in propiedades:
        lista.insert(END, f"ID: {p[0]} | Tipo: {p[1]} | Dirección: {p[2]} | Valor: {p[3]}")
    lista.pack(pady=20)

def ver_propiedad_formulario():
    form = Toplevel()
    form.title("Ver Propiedad")
    form.geometry("400x250")

    Label(form, text="ID Propiedad").pack(pady=5)
    id_entry = Entry(form, width=30)
    id_entry.pack()

    def mostrar():
        try:
            datos = obtener_propiedad_por_id(id_entry.get())
            if datos:
                messagebox.showinfo("Detalles", f"ID: {datos[0]}\nTipo: {datos[1]}\nDirección: {datos[2]}\nValor: {datos[3]}")
            else:
                messagebox.showwarning("No encontrado", "Propiedad no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(form, text="Ver Detalles", bootstyle="info", command=mostrar).pack(pady=20)

def agregar_a_visitas_formulario():
    form = Toplevel()
    form.title("Agregar a Lista de Visitas")
    form.geometry("400x250")

    Label(form, text="ID Cliente").pack(pady=5)
    cliente_entry = Entry(form, width=30)
    cliente_entry.pack()

    Label(form, text="ID Propiedad").pack(pady=5)
    propiedad_entry = Entry(form, width=30)
    propiedad_entry.pack()

    def agregar():
        try:
            agregar_a_visitas(cliente_entry.get(), propiedad_entry.get())
            messagebox.showinfo("Éxito", "Propiedad agregada a la lista de visitas.")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(form, text="Agregar", bootstyle="success", command=agregar).pack(pady=20)

def crear_ventana():
    style = Style(theme="darkly")
    ventana = style.master
    ventana.title("Sistema de Alquiler de Propiedades")
    ventana.geometry("500x650")

    label = tk.Label(ventana, text="Bienvenido al SAP", font=("Arial", 20), bg="#212529", fg="white")
    label.pack(pady=20)

    botones = [
        ("Crear Cuenta (Cliente)", crear_cliente_formulario),
        ("Agregar Propiedad (Dueño)", agregar_propiedad_formulario),
        ("Buscar Propiedades", buscar_propiedades_formulario),
        ("Ver Propiedad", ver_propiedad_formulario),
        ("Agregar a Lista de Visitas", agregar_a_visitas_formulario),
        ("Rentar Propiedad", rentar_propiedad_formulario)
    ]

    for texto, comando in botones:
        btn = Button(
            ventana,
            text=texto,
            command=comando,
            width=40,
            bootstyle="primary"
        )
        btn.pack(pady=5)

    ventana.mainloop()
