class Passaro:
    def voar(self):
        print("Voandooo")

class Pardal(Passaro):
    def voar(self):
        return super().voar()        

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz Não pode Voar") 

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)

plano_voo(Avestruz())