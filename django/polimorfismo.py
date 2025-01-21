class Animal:
    def emitir_som(self):
        print('Qualquer som...')

    def emitir_som(self):
        print('xuxa')

class Cachorro(Animal):
    
    def emitir_som(self):
        print('Au Au!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau!')

    # def emitir_som(self):
    #     return super().emitir_som()

class Xuxa(Animal):

    def emitir_som(self):
        return super().emitir_som()
        
cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()

xuxa = Xuxa()
xuxa.emitir_som()