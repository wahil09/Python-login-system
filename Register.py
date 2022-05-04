from filter_data import *

class Register:
    number_of_user = get_numbers_of_users()
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.AddUser()

    def AddUser(self):
        cond = test(self.__username, self.__password, 'register')['bol']
        message = test(self.__username, self.__password, 'register')['message']
        if cond:
            add_user_for_database(f"user{Register.number_of_user}", {"name": self.__username, "password": self.__password})
            print(message)
        else:
            print(message)
            name = input('Entrer Votre Nom : ')
            password = input('Entrer Votre password : ')
            CreerUser(name, password)

    @classmethod
    def GetAllUser(cls) -> dict:
        return data_base

    @classmethod
    def GetNumberOfUser(cls):
        return len(data_base)

# function pour créer un nouvelle utilisateur
def CreerUser(name, password):
    Register(name, password)




