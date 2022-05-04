from datetime import date
import json
data_base = {}

def user_existe(username):
    with open('data.json', 'r') as r:
        data_base = json.load(r)
        r.close()
    user_existe = False
    self_user = ""

    for user in data_base:
        if username in data_base[user]['name']:
            user_existe = True
            self_user = user
    if user_existe:
        return [user_existe, data_base[self_user]]
    else:
        return [user_existe]

def add_user_for_database(number_of_user, data_user):
    with open('data.json', "r") as r:
        update_data_base = json.load(r)
        update_data_base[number_of_user] = data_user
        r.close()

    with open('data.json', "w") as w:
        json.dump(update_data_base, w)
        r.close()

def get_numbers_of_users():
    with open("data.json", 'r') as r:
        data = json.load(r)
        r.close()
        return len(data)

def test(username, password, log_or_reg):
    # Condition pour créer uhn nouvelle utilisateur
    date1 = date.today()
    cond = {'bol' :True, 'message': f"information entrer valide, {username} vous etez inscrit le {date1}"}

    if 30 >= len(username) >= 3:
        if 30 >= len(password) >= 6:
            # si il y'a au moins un lettre en majuscule dans le password
            if if_x_in_list(password, 'maj'):
                # si il y'a au moins un numero dans le password
                if if_x_in_list(password, 'num'):
                    # si il y'a au moins un caractère spiciaux dans le password
                    if if_x_in_list(password, 'caract'):
                        if log_or_reg == 'register':
                            if user_existe(username)[0]:
                                cond["bol"] = False
                                cond['message'] = 'username déja utiliser, il faut changer le nom'

                    else:
                        cond["bol"] = False
                        cond['message'] = 'password invalid, il faut un caractère spiciaux au minimaum'
                else:
                    cond["bol"] = False
                    cond['message'] = 'password invalid, il faut un numero au minimaum'
            else:
                cond["bol"] = False
                cond['message'] = 'password invalid, il faut un lettre en majuscule au minimaum'
        else:
            cond["bol"] = False
            cond['message'] = 'password invalid, il faut 6 caractère au minimaum et 30 au maximaum'
    else:
        cond["bol"] = False
        cond['message'] = 'username invalid, il faut 3 caractère au minimaum et 30 au maximaum'

    return cond

# si le password y'a t'il au moins un chifre ou un caractère spiciaux
def if_x_in_list(password, type):
    bol = False
    for i in password:
        if type == 'num':
            if ord(i) >= 48 and ord(i) <= 57 :
                bol = True
        if type == 'caract':
            if ord(i) >= 33 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 65 or ord(i) >= 91 and ord(i) <= 96:
                bol = True
        if type == 'maj':
            if ord(i) >= 65 and ord(i) <= 90 :
                bol = True
    return bol