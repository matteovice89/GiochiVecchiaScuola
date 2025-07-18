class Mappa:
    def __init__(self, mappa):
        self.mappa = mappa
    
    def stampa(self):
        for r in self.mappa:
            print(" ".join(r))
    
    
class Giocatore:
    def __init__(self,nome,posizione,vita):
        self.nome=nome
        self.posizione=posizione
        self.vita=vita
        
    def muovi(self):
        pass
    
    def guarda(self):#al posto di aggiornare la mappa in questa versione ci si guarda attorno e ci si orienta 
        pass
    
    def abbatti(self): #usa l'ascia e abbatte cespugli, rovi ecc
        pass

class Elementi: #questa serve per ragruppare gli elementi come alberi cespugli e altro
    def __init__(self,genere,vivo,posizione):
        self.genere=genere
        self.vivo=vivo #esempio il cespuglio se viene abbattuto diventa vivo false
        self.posizione=posizione
        
    
class Gioco:#la classe non è essenziale ora ma se implemento nuove cose è già pronta
    def __init__(self,inizio,fine):
        self.inizio=inizio
        self.fine=fine
    
    
        
    
cartina=Mappa([
    ["*", "S", "S", "U", "A"],
    ["A", "C", "A", "A", "A"],
    ["A", "S", "S", "S", "A"],
    ["S", "S", "A", "S", "A"],
    ["A", "A", "S", "I", "A"]
])


partita=Gioco([4,3],[0,4])
partenza=partita.inizio
nomepl1=str(input('Benvenuto, inserisci il tuo nome\n'))
player1=Giocatore(nomepl1,partenza,10)
print('Ottimo',nomepl1,'Dovrai riusciure ad uscire dal bosco, Per orientarti usa la cartina che vedi qui sotto\n')
cartina.stampa()
print('\n Per guardati attorno ti basterà scrivere guarda, e per muoverti usa i punti cardinali nord, sud, ovest ed est\n')
print('ad esempio digita vai a nord per muoverti di una posizione verso nord ecc..se ti trovi nei cespugli usa il comando usa ascia per liberarti\n')
print('Spero di averti detto tutto..ah si usa comando mappa se non sai dove sei..in bocca al lupo e partiamo\n')
