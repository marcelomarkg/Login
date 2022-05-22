#importar as bibliotecas
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import left, width
from webbrowser import BackgroundBrowser

#Criar janela
jan = Tk()
jan.title("DP Sysems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

#=====Carrgando imagens
logo = PhotoImage(file="Icons\logo.png")

#====Widgtes==========

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gthic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=149, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gthic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=149, y=160)

#Botoes
LoginButton= ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

RegisterButton= ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x=125, y=260)


jan.mainloop()