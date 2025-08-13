mappa = [
    ["*", "S", "S", "U", "A"],
    ["A", "C", "A", "A", "A"],
    ["A", "S", "S", "S", "A"],
    ["S", "S", "A", "S", "A"],
    ["A", "A", "S", "I", "A"]
]
comando = "INIZIO"


def instruzioni():
    print('DIGITA UNO DEI SEGUENTI COMANDI\n')
    print('ECCO I COMANDI\n')
    print('MAPPA --> visvualizza la mappa\n')
    print('NORD --> vai a nord\nSUD--> vai a sud\nEST--> vai a est,\nOVEST--> vai a ovest\n')
    print('ASCIA --> abbatte un cespuglio\n')
    print('END --> interrompo il gioco')


def confini(posizione):
    if posizione[0] < 0 or posizione[0] > 4 or posizione[1] < 0 or posizione[1] > 4:
        print('SEI SUL CONFINE')
        controllo = 0
        return (controllo)


def ostacoli(controllo):
    if controllo == "A":
        print('ATTENZIONE HA SBATTUTO CONTRO UN ALBERO')
        controllo = 0
        return (controllo)


def stampa(cartina):
    for r in range(len(cartina)):
        print(cartina[r])


posizione = [4, 3]  # la posizione C( una lista dove i valori sono le cordinate nella matrice

inizio = [4, 3]
fine = [0, 3]  # stessa cosa per inizio e fine
print('BENVENUTO NEL BOSCO\n RIUSCIRAI A TROVARE L''USCITA??\n DIGITA UN COMANDO\n PROVA SUBITO ISTRUZIONI PER AVERE L''ELENCO\n')
while comando != "END":
    comando = str(input('PROSSIMO COMANDO?\n'))
    if posizione == fine:
        print('COMPLIMENTI SEI USCITO DAL BOSCO ED HAI TERMINATO IL LIVELLO')
        comando='END'
    if comando == 'ISTRUZIONI':
        instruzioni()
    elif comando == 'MAPPA':
        stampa(mappa)
        print('\n OTTIMA IDEA CONSULTARE UNA MAPPA, NON VORRAI MICA ANDARE CONTRO UN ALBEO..\n')
    elif comando == 'NORD':
         posizione[0] = posizione[0] - 1
         if confini(posizione) != 0 and ostacoli(mappa[posizione[0]][posizione[1]]) != 0:
            mappa[posizione[0]][posizione[1]] = 'P'
            print('\n TI SEI MOSS* VERSO NORD E NON SEI USCITO DAL SENTIERO\n')
         else:
            posizione[0] = posizione[0] + 1

    elif comando == 'SUD':
         posizione[0] = posizione[0] + 1
         if confini(posizione) != 0 and ostacoli(mappa[posizione[0]][posizione[1]]) != 0:
            mappa[posizione[0]][posizione[1]] = 'P'
            print('\n TI SEI MOSS* VERSO SUD E NON SEI USCITO DAL SENTIERO\n')
         else:
            posizione[0] = posizione[0] - 1

    elif comando == 'EST':
         posizione[1] = posizione[1] + 1
         if confini(posizione) != 0 and ostacoli(mappa[posizione[0]][posizione[1]]) != 0:
            mappa[posizione[0]][posizione[1]] = 'P'
            print('\n TI SEI MOSS* VERSO EST E NON SEI USCITO DAL SENTIERO\n')
         else:
            posizione[1] = posizione[1] - 1

    elif comando == 'OVEST':
         posizione[1] = posizione[1] - 1
         if confini(posizione) != 0 and ostacoli(mappa[posizione[0]][posizione[1]]) != 0:
            mappa[posizione[0]][posizione[1]] = 'P'
            print('\n TI SEI MOSS* VERSO NORD E NON SEI USCITO DAL SENTIERO\n')
         else:
            posizione[1] = posizione[1] + 1

    if posizione == fine:
        print('COMPLIMENTI SEI USCIT* DAL BOSCO ED HAI TERMINATO IL LIVELLO')
        comando='END'
