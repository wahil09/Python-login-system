from filter_data import *

def Choix():
    name = input('Entrer Votre Nom : ')
    password = input('Entrer Votre password : ')
    Connexion(name, password)

def Connexion(username, password):
    cond = test(username, password, 'connexion')
    if cond['bol'] == True:
        if user_existe(username)[0]:
            if user_existe(username)[1]['password'] == password:
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
