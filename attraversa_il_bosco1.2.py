class Mappa:
    def __init__(self, mappa):
        self.mappa = mappa

    def stampa(self):
        for r in self.mappa:
            print(" ".join(r))


class Giocatore:
    def __init__(self, nome, posizione, vita,direzione):
        self.nome = nome
        self.posizione = posizione
        self.vita = vita

    def muovi(self):
        if self.direzione=='nord':
            if self.posizione[0]==0:
                print('Sei sul confine non puoi avvanzare verso nord')
            else:
                nord=self.posizione[0]
                self.posizione[0]=nord-1 
                #print(self.posizione) #serve per il debug 
    def guarda(self):  # al posto di aggiornare la mappa in questa versione ci si guarda attorno e ci si orienta
        #print(self.posizione)
        verticale=self.posizione[0]
        orizzontale=self.posizione[1]
        #print(verticale)
        #print(orizzontale)
        try:
            nord=cartina.mappa[verticale-1][orizzontale]
            print('a nord è presente', nord)
        except IndexError:
            print('A nord c\'è il confine')
        try:
            sud = cartina.mappa[verticale + 1][orizzontale]
            print('a sud è presente', sud)
        except IndexError:
            print('A sud c\'è il confine')
        try:
            est = cartina.mappa[verticale][orizzontale-1]
            print('a est è presente', est)
        except IndexError:
            print('A est c\'è il confine')
        try:
            ovest = cartina.mappa[verticale][orizzontale+1]
            print('a ovest è presente', ovest)
        except IndexError:
            print('A ovest c\'è il confine')


    def abbatti(self):  # usa l'ascia e abbatte cespugli, rovi ecc
        pass


class Elementi:  # questa serve per ragruppare gli elementi come alberi cespugli e altro
    def __init__(self, genere, vivo, posizione):
        self.genere = genere
        self.vivo = vivo  # esempio il cespuglio se viene abbattuto diventa vivo false
        self.posizione = posizione


class Gioco:  # la classe non è essenziale ora ma se implemento nuove cose è già pronta
    def __init__(self, inizio, fine):
        self.inizio = inizio
        self.fine = fine


cartina = Mappa([
    ["*", "S", "S", "U", "A"],
    ["A", "C", "A", "A", "A"],
    ["A", "S", "S", "S", "A"],
    ["S", "S", "A", "S", "A"],
    ["A", "A", "S", "I", "A"]
])

partita = Gioco([4, 3], [0, 4])
partenza = partita.inizio
nomepl1 = str(input('Benvenuto, inserisci il tuo nome\n'))
player1 = Giocatore(nomepl1, partenza, 10,'')
print('Ottimo', nomepl1, 'Dovrai riusciure ad uscire dal bosco, Per orientarti usa la cartina che vedi qui sotto\n')
cartina.stampa()
print(
    '\n Per guardati attorno ti basterà scrivere guarda, e per muoverti usa i punti cardinali nord, sud, ovest ed est\n')
print(
    'ad esempio digita vai a nord per muoverti di una posizione verso nord ecc..se ti trovi nei cespugli usa il comando usa ascia per liberarti\n')
print('Spero di averti detto tutto..ah si usa comando mappa se non sai dove sei..in bocca al lupo e partiamo\n')
comando = 'inizio'

while comando != 'end':
    comando = str(input(''))
    if 'mappa' in comando:  # se scrivo usa la mappa o guarda la mappa comunque funziona
        cartina.stampa()
    elif 'guarda' in comando:
        player1.guarda()
    elif 'nord' in comando:
        player1.direzione='nord'
        player1.muovi()
