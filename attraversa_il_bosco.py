mappa=[
    ["*","S","S","U","A"],
    ["A","C","A","A","A"],
    ["A","S","S","S","A"],
    ["S","S","A","S","A"],
    ["A","A","S","I","A"]
    ]
comando="INIZIO"

def instruzioni():
    print('ECCO I COMANDI\n')
    print('MAPPA --> visvualizza la mappa\n')
    print('NORD --> vai a nord\SUD vai a sud\nEST vai a est,\nOVEST vai a ovest\n')
    print('ASCIA --> abbatte un cespuglio\n')
    print('END --> interrompo il gioco')
    

while comando!= "END":
    comando=str(input('INSERISCI UN COMANDO (SCRIVI ISTRUZIONI PER SAPERE COSA FARE)\n'))
    if comando == 'ISTRUZIONI':
        instruzioni()
    elif comando=='MAPPA':
        for r in range(len(mappa)):
             print(mappa[r])
