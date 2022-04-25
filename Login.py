from filter_data import *

def Choix():
    name = input('Entrer Votre Nom : ')
    password = input('Entrer Votre password : ')
    Connexion(name, password)

def Connexion(username, password):
    cond = test(username, password, 'connexion')
    if cond['bol'] == True:
        if username in data_base:
            if data_base[username] == password:
                print(f'{username} bienvenue dans votre compte')
            else:
                print("Mote de pass incorrect !")
                Choix()
        else:
            print(f"{username} vous n'etez pas inscrie ! ")
            Choix()
    else:
        print(cond['message'])
        Choix()
