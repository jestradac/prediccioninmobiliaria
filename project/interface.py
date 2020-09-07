from tkinter import *

raiz = Tk()

raiz.title("Predicción Inmobiliaria")

#raiz.resizable(True, False)

#raiz.geometry("650x350")

raiz.config(bg="black")

varFrame = Frame()

varFrame.pack(fill="both", expand="True")

varFrame.config(bg="white")

varFrame.config(width="650", height="400")

Label(varFrame, text="Predicción de Precios Inmobiliarios", bg="white", fg="black", font=(14)).place(x=225, y=10)

Label(varFrame, text="Zona :", bg="white", font=(12)).place(x=20, y=60)

Label(varFrame, text="Tipo de Inmueble :", bg="white", font=(12)).place(x=20, y=100)

Label(varFrame, text="Metros Terreno :", bg="white", font=(12)).place(x=20, y=140)

Label(varFrame, text="Metros Construidos :", bg="white", font=(12)).place(x=20, y=180)

Label(varFrame, text="Distancia Avenida :", bg="white", font=(12)).place(x=20, y=220)

Label(varFrame, text="Garaje :", bg="white", font=(12)).place(x=20, y=260)

txbTerreno = Entry(varFrame)
txbTerreno.place(x=180, y=140)

txbConstruido = Entry(varFrame)
txbConstruido.place(x=180, y=180)

txbDistancia = Entry(varFrame)
txbDistancia.place(x=180, y=220)

txbGaraje = Entry(varFrame)
txbGaraje.place(x=180, y=260)

btnCotizar = Button(varFrame, text="Cotizar")
btnCotizar.place(x=200, y=340)

#lblTitulo = Label(varFrame, text="Predicción de Precios Inmobiliarios")
#lblTitulo.place(x=225, y=20)

raiz.mainloop()