import os

#funzione menu'
def mostra_menu():
    print("0) uscita")
    print("1) registrazione")
    print("2) accedi")
    risposta = eval(input("scegli una opzione: "))
    return risposta

FILE_DATI = "utenti.csv"
SEPARATORE = ","

while True:
    risp = mostra_menu()
    if (risp == 0):
        print("Uscita avvenuta correttamente !")
        break
    if (risp == 1):
        #leggi dati utente
        nome = input("inserisci nome: ")
        cognome = input("inserisci cognome: ")
        email = input("inserisci e-mail: ")
        password = input("inserisci password: ")
        password2 = input("conferma password: ")

        flag_ok = True
        if (password != password2):
            print("Le password non coincidono !")
            flag_ok = False
        if (os.path.isfile(FILE_DATI) == True):
            in_file = open(FILE_DATI,"r")
            
            righe = in_file.readlines()

            for i in range(0, len(righe)):
                utente = righe[i]
                u_nome,u_cognome,u_email,u_pass1 = utente.split(SEPARATORE) 
                if (u_email==email): 
                    flag_ok = False 
                    print("Esiste altro utente con stessa mail!")
                    break
            in_file.close()

        if (flag_ok == True): 
            out_file = open(FILE_DATI,"a")
            str_dati = nome+SEPARATORE+cognome
            str_dati = str_dati + SEPARATORE + email
            str_dati = str_dati + SEPARATORE + password + "\n"
            out_file.write(str_dati)
            out_file.close()
       
        
    if (risp == 2):
        flag_ok=True
        controlla_email=input("inserisci l'email: ")
        controlla_password=input("inserisci la password: ")
        if(os.path.isfile(FILE_DATI)==True):
            in_file=open(FILE_DATI,"r")
            righe=in_file.readlines()

            for i in range(0,len(righe)):
                utente=righe[i]
                u_nome,u_cognome,u_email,u_pass1 = utente.split(SEPARATORE)
                if (controlla_email==u_email):
                    if (controlla_password==u_password):
                        print("accesso effetuato !")
                    
                if (controlla_email!=u_email):
                    print("Email errata")
                    break
