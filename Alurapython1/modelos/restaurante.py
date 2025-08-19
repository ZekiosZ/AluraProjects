class Restaurante:
    #Método Construtor, Ou função para definir parametros para os objetos
    def __init__(self, nome, categoria):
        self.nome=""
        self.categoria=""
        self.ativo = False
restaurante_praca=Restaurante("Praça", "Bistrô")



#Antigos testes
'''restaurante_praca.nome="Bistrô"
restaurante_praca.categoria="Italiana"
restaurante_praca.ativo=True'''

restaurante_pizza=Restaurante("Pizza Place", "Fast Food")


#Antigos testes
'''restaurante_pizza.nome="Pizza Place"
restaurante_pizza.categoria="Fast Food"
restaurante_pizza.ativo=True'''
#separação

'''categoria=Restaurante.categoria'''

#Os Testes vou colocar em comentarios
'''if restaurante_praca.ativo==False:
    print("O restaurante esta inativo")
else:
    print("O restaurante esta ativo")
    '''
#Print teste
print("Nome do restaurante:",restaurante_praca.nome,"\nCategoria do restaurante:", restaurante_praca.categoria)
#Codigo Dir antes do print ajuda a identificar possiveis comandos no objeto
#Codigo Vars ajuda a "printar", mostrar oque esta definido dentro de determinado objeto