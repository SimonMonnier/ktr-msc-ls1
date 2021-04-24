#Importation des librairies
from tkinter import *
from functools import partial
import csv


#Variable global
user1 = "user1"
user2 = "user2"
user3 = "user3"

passUser1 = "user1"
passUser2 = "user2"
passUser3 = "user3"



#Création de la méthode saveData
def saveData(entryName, entryCompany, entryEmail, entryPhone, userNb):
    file = open(userNb + 'dataSave.csv', 'a')
    data = entryName.get() + "," + entryCompany.get() + "," + entryEmail.get() + "," + entryPhone.get() + "\n"
    file.write(data)
    file.close()


#Création de la fenetre LogWindow
def LogWindow ():
    #Création de la fenetre
    windows = Tk()
    #Dimension de la fenetre
    windows.geometry("350x200")

    #Création des labels
    labelUser = Label(windows, text="User :")
    labelUser.place(x = 50, y = 50)
    
    labelPass = Label(windows, text="Pass :")
    labelPass.place(x = 50, y = 100)
    
    #Création des entrées
    entryUser = Entry(windows)
    entryUser.place(x = 135, y = 50)

    entryPass = Entry(windows)
    entryPass.place(x = 135, y = 100)
    
    #╣Création du bouton login
    buttonLogin = Button(windows, text = "Login", command = partial(login, entryUser, entryPass, windows))
    buttonLogin.place(x = 165, y = 150)
    
    #Lancement de la fenetre
    windows.mainloop()
    
    
#Création de la méthode login
def login(entryUser, entryPass, windows):
    if entryUser.get() == user1 and entryPass.get() == passUser1:
        windows.destroy()
        connectedWindow (user1)
    if entryUser.get() == user2 and entryPass.get() == passUser2:
        windows.destroy()
        connectedWindow (user2)
    if entryUser.get() == user3 and entryPass.get() == passUser3:
        windows.destroy()
        connectedWindow (user3)
        
#Création de la méthode logout
def logout(windows):
    windows.destroy()
    LogWindow()


#Création de la méthode library
def library(windows, userNb):
    windows.destroy()
    libraryWindow(userNb)


#Création de la fenetre libraryWindow
def libraryWindow (userNb):
    #Création de la fenetre
    windows = Tk()
    #Dimension de la fenetre
    windows.geometry("350x300")
    
    #Ouverture du fichier data 
    cr = csv.reader(open(userNb + 'dataSave.csv'))
    i = 50
    #Création des labels
    labelUser = Label(windows, text = "Login at " + userNb)
    labelUser.place(x = 150, y = 10)
    for row in cr:
        labelUser = Label(windows, text = row)
        labelUser.place(x = 50, y = i)
        i = i + 25
    

    #╣Création du bouton addCard
    buttonAddCard = Button(windows, text = "Add", command = partial(connectedWindow, userNb))
    buttonAddCard.place(x = 150, y = 250)
    
    #╣Création du bouton logout
    buttonSave = Button(windows, text = "Logout", command = partial(logout, windows))
    buttonSave.place(x = 200, y = 250) 
    
    #Lancement de la fenetre
    windows.mainloop()


#Création de la fenetre connectedWindow
def connectedWindow (userNb):
    #Création de la fenetre
    windows = Tk()
    #Dimension de la fenetre
    windows.geometry("350x300")
    
    #Création des labels
    labelUser = Label(windows, text = "Login at " + userNb)
    labelUser.place(x = 150, y = 10)
    
    labelName = Label(windows, text="Name :")
    labelName.place(x = 50, y = 50)

    labelCompany = Label(windows, text="Company :")
    labelCompany.place(x = 50, y = 100)
    
    labelEmail = Label(windows, text="Email :")
    labelEmail.place(x = 50, y = 150)
    
    labelPhone = Label(windows, text="Phone :")
    labelPhone.place(x = 50, y = 200)

    #Création des entrées
    entryName = Entry(windows)
    entryName.place(x = 135, y = 50)
        
    entryCompany = Entry(windows)
    entryCompany.place(x = 135, y = 100)

    entryEmail = Entry(windows)
    entryEmail.place(x = 135, y = 150)

    entryPhone = Entry(windows)
    entryPhone.place(x = 135, y = 200)

    #╣Création du bouton save
    buttonSave = Button(windows, text = "Save", command = partial(saveData, entryName, entryCompany, entryEmail, entryPhone, userNb))
    buttonSave.place(x = 150, y = 250)
    
    #╣Création du bouton logout
    buttonSave = Button(windows, text = "Logout", command = partial(logout, windows))
    buttonSave.place(x = 200, y = 250)
    
    #╣Création du bouton library
    buttonLibrary = Button(windows, text = "Library", command = partial(library, windows, userNb))
    buttonLibrary.place(x = 85, y = 250)
    
    #Lancement de la fenetre
    windows.mainloop()
    

LogWindow()