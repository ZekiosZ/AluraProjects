class Restaurante:
    #Método Construtor, Ou função para definir parametros para os objetos
    def __init__(self, nome, categoria, ativo):
        self.nome=nome
        self.categoria=categoria
        self.ativo = ativo
#self é a referência da instância que estamos usando naquele momento. Então, sempre que precisarmos da parte textual de um objeto, usaremos self.
#E definido igual uma função, funciona parecido mas não são iguais, o __str__ e um metodo Construtor especial
    def __str__(self):
            return f'Restaurante de nome: {self.nome} de categoria: {self.categoria} esta atualmente: {self.ativo}'


restaurante_praca=Restaurante("Praça", "Bistrô", "Funcionando")

#Antigos testes
'''restaurante_praca.nome="Bistrô"
restaurante_praca.categoria="Italiana"
restaurante_praca.ativo=True'''

restaurante_pizza=Restaurante("Pizza Place", "Fast Food", "Fora de serviço")


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
print(restaurante_pizza)
print(restaurante_praca)
#Codigo Dir antes do print ajuda a identificar possiveis comandos no objeto
#Codigo Vars ajuda a "printar", mostrar oque esta definido dentro de determinado objeto