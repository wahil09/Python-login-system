import Login
import Register

# met deux lien 'Login' et 'Register' dans le Gui et utiliser ce fonction ou un autre comme celui'ci

def main_menu():
    try:
        user = int(input('Enter 0 pour inscrire or 1 pour connecter : '))

    except:
        print('Entrer un numero 0 ou 1 !!!')
        main_menu()
    if user == 0:
        name = input('Entrer Votre Nom : ')
        password = input('Entrer Votre password : ')
        Register.CreerUser(name, password)
    else:
        name = input('Entrer Votre Nom : ')
        password = input('Entrer Votre password : ')
        Login.Connexion(name, password)
main_menu()
