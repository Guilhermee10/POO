class carro:
    modelo = 'ford'
    cor = 'azul'
    cilindradas = '1000 cavalos'

    def ligar_carro(self):
        print('carro ligando.....')

    def acelerar(self):
        print("vrum")

car = carro()

car.acelerar()

car.ligar_carro()