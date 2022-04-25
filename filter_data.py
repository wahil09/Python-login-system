from datetime import date
data_base = {'oussama': 'Oussama.09', 'oweiss': 'Oweiss.09'}

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
                            if username in data_base:
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