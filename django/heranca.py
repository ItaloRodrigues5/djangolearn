class Carro:
    numero_rodas = 4
    passageiros = 5

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')

class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

uno = Uno()
uno.acelerar()
uno.buzinar()
uno.frear()
print('{} rodas'.format(uno.numero_rodas))
print('{} passageiros'.format(uno.passageiros))