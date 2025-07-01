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

def confini(posizone):
    if posizione[0]>4 or posizione[0]<0:
        print('SEI SUL CONFINE NON PUOI PROCEDERE')
        
    
    
posizione=[1,0] #la posizione è una lista dove i valori sono le cordinate nella matrice
inizio=[4,3]
fine=[0,3] #stessa cosa per inizio e fine

while comando!= "END":
    comando=str(input('INSERISCI UN COMANDO (SCRIVI ISTRUZIONI PER SAPERE COSA FARE)\n'))
    if comando == 'ISTRUZIONI':
        instruzioni()
    elif comando=='MAPPA':
        for r in range(len(mappa)):
             print(mappa[r])
    elif comando == 'NORD':
        posizione[0]=posizione[0]-1
        if confini(posizione)==True:
           posizione[0]=posizione[0]+1  
    print(posizione)
