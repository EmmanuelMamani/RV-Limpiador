from email.mime import audio
import webbrowser
import speech_recognition as sp
from tkinter import * 
from time import sleep
ventana= Tk()
ventana.title("Edificio academico")
ventana.geometry("1200x400")

#Tercer piso
salto3=Label(ventana,text=" ")
salto3.grid(column=0,row=0)

A10765= Label(ventana,text="\tAula 10765",font=("Arial Bold",15),fg="red")
A10765.grid(column=0,row=1)

A12890= Label(ventana,text="\tAula 12890",font=("Arial Bold",15),fg="red")
A12890.grid(column=1,row=1)

A13876= Label(ventana,text="\tAula 13876",font=("Arial Bold",15),fg="red")
A13876.grid(column=2,row=1)

A1489= Label(ventana,text="\tAula 1489",font=("Arial Bold",15),fg="red")
A1489.grid(column=3,row=1)

A15000= Label(ventana,text="\tAula 15000",font=("Arial Bold",15),fg="red")
A15000.grid(column=4,row=1)

#segundo piso
salto2=Label(ventana,text=" ")
salto2.grid(column=0,row=2)

A6982= Label(ventana,text="\tAula 6982",font=("Arial Bold",15),fg="red")
A6982.grid(column=0,row=3)

A8450= Label(ventana,text="\tAula 8450",font=("Arial Bold",15),fg="red")
A8450.grid(column=1,row=3)

A9123= Label(ventana,text="\tAula 9123",font=("Arial Bold",15),fg="red")
A9123.grid(column=2,row=3)

#Primer piso
salto1=Label(ventana,text=" ")
salto1.grid(column=0,row=4)

A1045= Label(ventana,text="\tAula 1045",font=("Arial Bold",15),fg="red")
A1045.grid(column=0,row=5)

A2670= Label(ventana,text="\tAula 2670",font=("Arial Bold",15),fg="red")
A2670.grid(column=1,row=5)

A3456= Label(ventana,text="\tAula 3456",font=("Arial Bold",15),fg="red")
A3456.grid(column=2,row=5)

A4983= Label(ventana,text="\tAula 4983",font=("Arial Bold",15),fg="red")
A4983.grid(column=3,row=5)

A5266= Label(ventana,text="\tAula 5266",font=("Arial Bold",15),fg="red")
A5266.grid(column=4,row=5)

#Planta baja
salto0=Label(ventana,text=" ")
salto0.grid(column=0,row=6)

A324= Label(ventana,text="\tAula 324",font=("Arial Bold",15),fg="red")
A324.grid(column=0,row=7)

A456= Label(ventana,text="\tAula 456",font=("Arial Bold",15),fg="red")
A456.grid(column=1,row=7)

A678= Label(ventana,text="\tAula 678",font=("Arial Bold",15),fg="red")
A678.grid(column=2,row=7)

A899= Label(ventana,text="\tAula 899",font=("Arial Bold",15),fg="red")
A899.grid(column=3,row=7)

#opciones
salto4=Label(ventana,text=" ")
salto4.grid(column=0,row=8)

mensaje=Label(ventana,text="\tEsperando ordenes\t", fg="black", font=("Arial Bold",16))
mensaje.grid(column=0,row=9)

def escuchar():
    reconocedor = sp.Recognizer()
    with sp.Microphone()as source:
        print("Hola soy tu asistente de voz")
        audio = reconocedor.listen(source)

        texto = reconocedor.recognize_google(audio)
        if "10765" in texto:
            print(texto)
            A10765.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "12890" in texto:
            print(texto)
            A12890.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "13876" in texto:
            print(texto)
            A13876.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "1489" in texto:
            print(texto)
            A1489.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "15000" in texto:
            print(texto)
            A15000.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "6982" in texto:
            print(texto)
            A6982.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "8450" in texto:
            print(texto)
            A8450.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "9123" in texto:
            print(texto)
            A9123.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "1045" in texto:
            print(texto)
            A1045.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "2670" in texto:
            print(texto)
            A2670.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "3456" in texto:
            print(texto)
            A3456.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "4983" in texto:
            print(texto)
            A4983.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "5266" in texto:
            print(texto)
            A5266.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "324" in texto:
            print(texto)
            A324.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "456" in texto:
            print(texto)
            A456.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "678" in texto:
            print(texto)
            A678.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")
        if "899" in texto:
            print(texto)
            A899.config(fg="black")
            mensaje.configure(text="\tEsperando ordenes\t")

ordenar=Button(ventana,text="Ordenar", command=escuchar)
ordenar.grid(column=1,row=9)
ventana.mainloop()

#Reconocedor de voz


