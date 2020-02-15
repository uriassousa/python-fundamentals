#-+- = coding: UTF-8 -*-

# class Carro():
#     def __init__(self):
#         self.rodas = 4
#         self.motor = True

#     def ligar(self):
#         print('ligado')

#     palio = Carro()
#     palio.ligar()

# class Servidor():
#     valor = None    
#     def __init__(self, servico, disco, processador, memoria):
#         self.servico = servico
#         self.disco = disco
#         self.processador = processador
#         self.memoria = memoria

#     def addMemoria(self, addM):
#         self.memoria += addM

#     def addArmazenamento(self, addD):
#        self.disco += addD

#     def mudaServico(self, new_service):
#         self.servico = new_service

# servidorWeb = Servidor('Nginx', 250, 'I7 9 Geracao', 16, 'IIS')

# servidorWeb.addMemoria(8)
# servidorWeb.addArmazenamento(128)
# servidorWeb.mudaServico('IIS')

# print(servidorWeb.memoria)

class Servidor(): 
    teste = 'teste01'

    def __init__(self):
        self.servico = None
        self.disco = 150
        self.processador = 'Intel Xeon'
        self.memoria = 16

class servidorWeb(Servidor):

    def __init__(self):
        super().__init__()
        self.servico = 'Nginx'

Vader = servidorWeb()

print(Vader.memoria)

