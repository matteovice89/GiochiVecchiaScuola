'''Sto rifacendo il giochino precedente ma in oop'''
#ATTENZIONE ANCORA IN LAVORAZIONE
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
