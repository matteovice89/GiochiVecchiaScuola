mappa = [
    ["*", "S", "S", "U", "A"],
    ["A", "C", "A", "A", "A"],
    ["A", "S", "S", "S", "A"],
    ["S", "S", "A", "S", "A"],
    ["A", "A", "S", "I", "A"]
]
comando = "INIZIO"


def instruzioni():
    print('ECCO I COMANDI\n')
    print('MAPPA --> visvualizza la mappa\n')
    print('NORD --> vai a nord\nSUD vai a sud\nEST vai a est,\nOVEST vai a ovest\n')
    print('ASCIA --> abbatte un cespuglio\n')
    print('END --> interrompo il gioco')


def confini(posizione):
    if posizione[0] < 0 or posizione[0] > 4 or posizione[1] < 0 or posizione[1] > 4:
        print('SEI SUL CONFINE')
        controllo=0
        return (controllo)


posizione = [4, 3]  # la posizione è una lista dove i valori sono le cordinate nella matrice
posizionev = posizione  # varibile di comodo per gestire i confini
inizio = [4, 3]
fine = [0, 3]  # stessa cosa per inizio e fine

while comando != "END":
    comando = str(input('INSERISCI UN COMANDO (SCRIVI ISTRUZIONI PER SAPERE COSA FARE)\n'))
    if comando == 'ISTRUZIONI':
        instruzioni()
    elif comando == 'MAPPA':
        for r in range(len(mappa)):
            print(mappa[r])
    if comando == 'NORD':
        posizione[0] = posizione[0] - 1
        ascisse = posizione[0]
        ordinate = posizione[1]

        if confini(posizione) != 0:
            mappa[ascisse][ordinate] = 'P'
            posizionev = posizione
            for r in range(len(mappa)):
                print(mappa[r])
        else:
            posizione = posizionev

    
