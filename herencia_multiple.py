class alimento:
    def comer(self):
        return "esta comiendo"

class Volador:
    def volar(self):
        return "esta volando"

class pajaro(alimento, Volador): 
    def dormir(self):
        return "esta durmiendo"

pajaro = pajaro()

print(pajaro.comer())  
print(pajaro.volar())      
print(pajaro.dormir())