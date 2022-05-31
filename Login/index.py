#importar as bibliotecas
from ast import Pass
from csv import excel
from email import message
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import back, left, width
from webbrowser import BackgroundBrowser
import DataBase


#Criar janela
jan = Tk()
jan.title("DP Sysems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="Icons\LogoIcon.ico")

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

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=149, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login info", message="Acesso confirmado, Bem vindo!")
    except:
        messagebox.showinfo(title="Login info", message="Acesso Negado. Verifique os dados")

#Botoes
LoginButton= ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo widgets de Login

    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #inserindo widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=99, y=16)

    Emaillabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    Emaillabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=99, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos. Não deixe nenhum vazio!")
        else:            
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?,?,?,?)
            """, (Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removendo widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        Emaillabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        #Trazendo de volta os botões de login
        LoginButton.place(x=99)
        RegisterButton.place(x=125)
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton= ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)


jan.mainloop()