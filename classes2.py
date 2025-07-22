class Celular:
    marca = 'nokia'
    modelo = 'tijolao'
    cor = 'azivis'
    tem_camera = False
    bateria = 'infinita'

    def fazer_ligaçao(self):
        print('fazendo ligaçao..')
    
    def jogar_cobrinha(self):
        print('Jogando cobrinha..')
    
    def despertador(self):
        print('Despertando..')
    
    def calcular(self, v1, v2):
        return v1 + v2

celular = Celular()

print (celular.marca)
celular.despertador()
print (celular.calcular(20,10))