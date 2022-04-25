import Login
import Register

# met deux lien 'Login' et 'Register' dans le Gui et utiliser ce fonction ou un autre comme celui'ci

user = int(input('Enter 0 pour inscrire or 1 pour connecter : '))
if user == 0:
    name = input('Entrer Votre Nom : ')
    password = input('Entrer Votre password : ')
    Register.CreerUser(name, password)
else:
    name = input('Entrer Votre Nom : ')
    password = input('Entrer Votre password : ')
    Login.Connexion(name, password)