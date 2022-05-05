import Login
import Register

# Mettez deux liens "Login" et "Register" dans l'interface graphique et utilisez cette fonction ou une autre fonction similaire.
def main():
    try:
        user = int(input('Enter 0 pour inscrire or 1 pour connecter : '))
    except:
        print('Entrer un numero 0 ou 1 !!!')
        main()
    if user == 0:
        name = input('Entrer Votre Nom : ')
        password = input('Entrer Votre password : ')
        Register.CreerUser(name, password)
    else:
        name = input('Entrer Votre Nom : ')
        password = input('Entrer Votre password : ')
        Login.Connexion(name, password)

if __name__ == '__main__':
    main()
 